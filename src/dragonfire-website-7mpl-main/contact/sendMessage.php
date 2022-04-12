<?php
$link = mysql_connect('localhost', 'denispolevin_dragonfire', 'connectdf', 'denispolevin_dragonfire');
mysql_select_db('denispolevin_dragonfire', $link);

error_reporting(E_ALL);
ini_set('display_errors', 1);

$username = $_POST['username'];
$email = $_POST['email'];
$message = $_POST['message'];

$sql = "INSERT INTO messages (username, email, message) VALUES ('".$username."', '".$email."', '".$message."')";

if(!mysql_query($sql))
{
      echo 'Error'.mysql_error();
}
else
{
      echo '$sql';
}

mysql_close($link);
echo 'Done';
?>