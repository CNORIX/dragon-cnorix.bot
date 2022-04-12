<?php
 $server = 'dragoncloud.7m.pl';
 $port = 80;
 $status = 'unavailable';
 $timeout = 10;
 $fp = @fsockopen ($server, $port, $errno, $errstr, $timeout);
 if ($fp) {
  $status = '204 No Content';
  @fwrite ($fp, "HEAD / HTTP/1.0\r\nHost: $server:$port\r\n\r\n");
  if (strlen(@fread($fp,1024))>0) $status = '200 OK';
  fclose ($fp);
 }
 echo "$server http status code: $status"; 
?>