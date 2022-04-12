<?php
if ($username == 'admin')
{
    if ($password == 'connectdf') {
        $dashboardurl = 'dashboard.html';
        header('Location: '.$dashboardurl);
        ob_end_flush();
    }
    else {
        echo "Invalid username or password";
    }
}
else {
      echo "Invalid username or password";
}
?>