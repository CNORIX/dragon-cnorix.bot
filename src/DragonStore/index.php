<?php
$lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
if ($lang = 'ru')
{
    header('Location: ./ru');
}
if ($lang = 'en')
{
    header('Location: ./en');
}
else
{
    echo "Sorry, but the page was not translated into your language";
}
?>