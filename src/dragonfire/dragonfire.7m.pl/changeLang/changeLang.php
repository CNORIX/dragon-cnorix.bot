<?php
$newLang = $_POST('newLang');
setcookie("lang", $newLang);
echo "Language changed. Redirecting in 5 seconds...";
sleep(5);
header("Location: ../")
?>