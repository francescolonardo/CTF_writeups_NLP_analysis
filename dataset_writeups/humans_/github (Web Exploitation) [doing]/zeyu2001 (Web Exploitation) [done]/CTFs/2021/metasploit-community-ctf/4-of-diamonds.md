### Port 10010 \[Web]

When we log into the application, we can see the following data in the page source. There seems to be a `role` attribute that we need to change, in order to escalate our privileges.

```markup
<script>
    var current_account = {
    "id":3,
    "username":"username",
    "password":"password",
    "role":"user",
    "created_at":"2021-12-04T05:12:11.986Z",
    "updated_at":"2021-12-04T05:12:11.986Z"};
</script>
```

Taking a closer look at the registration fields, we see that we are submitting an `account` object with the `username` and `password` attributes.

```markup
<div>
  <label for="account_username">Username</label>
  <input type="text" name="account[username]" id="account_username" />
</div>

<div>
  <label for="account_password">Password</label>
  <input type="password" name="account[password]" id="account_password" />
</div>

<div>
  <input type="submit" name="commit" value="Register" class="btn btn-primary" data-disable-with="Register" />
</div>
```

Submitting with `account[role] = admin` changes our `role`, granting us access to `/admin`.
