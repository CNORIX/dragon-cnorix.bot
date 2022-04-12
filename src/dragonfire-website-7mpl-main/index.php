<?php
$lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
if ($lang = 'ru')
{
    header('Location: http://dragonfire.7m.pl/ru');
}
if ($lang = 'en')
{
    header('Location: http://dragonfire.7m.pl/en');
}
else
{
    echo "Sorry, but the page was not translated into your language";
}
?>