<?php $deny = array("127.0.0.1");
if (in_array ($_SERVER['REMOTE_ADDR'], $deny)) {
   header("location: https://example.com/");
   exit();
}
?>