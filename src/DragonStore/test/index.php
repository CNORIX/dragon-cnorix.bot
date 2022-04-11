<?php
error_reporting(False);
setcookie("antiBotByDF", "antiBotSecure58x");
echo 'Warning: DragonStore working in TEST MODE. Me currently testing php version of site for performance etc.';

if ($_COOKIE['antiBotByDF'] == "antiBotSecure58x") {
  echo '<title>DragonStore</title><meta name="viewport" content="width=device-width, initial-scale=1"><meta charset="utf-8">';
  echo '<style>@import url("main.css");</style>';

  // echo 'Warning: DragonStore working in TEST MODE. Me currently testing php version of site for performance etc.';

  $page = $_GET['page'];
  $storePageName = $_GET['storePageName'];

  echo '<div class="topnav">
    <a href="index.php?page=home">Home</a>
    <a href="index.php?page=apps">Apps</a>
    <a href="index.php?page=games">Games</a>
    <a href="index.php?page=music">Music</a>
    <a href="index.php?page=about">About DragonStore</a>
  </div>';

  if ($page == "home") {

  }
  if ($page == "apps") {

  }
  if ($page == "games") {

  }
  if ($page == "music") {
    echo '<img src="./images/1065750.png" width="30" height="30" align="left"></img><a href="index.php?page=storePage&storePageName=sadbeatbyromik19" align="top" style="padding-left:40px">Sad Beat</a>';
  }
  if ($page == "meisreallyangrydragon") {
    echo '<p>The Easter egg has been found!</p><p>Wow! You made this! But... Please keep it in a secret... Shh...</p>';
  }
  if ($page == "about") {
    echo '<div style="padding-left:16px"><h2>About DragonStore</h2><p>Version 1.2</p></div>';
  }
  if (!$page) {
    header("Location: index.php?page=home");
  }

  if ($page == "storePage") {
    if ($storePageName == "sadbeatbyromik19") {
      echo '<div style="padding-left:16px">
      <img src="./images/1065750.png" width="30" height="30" align="left"></img>
      <h2 align="top" style="padding-left:40px">Sad Beat</h2>
      
      <h2>Information</h2>
      <p>Composer: Romik19</p>
      <p>Published: 11.08.2021</p>
      <h2>Description</h2>
      <p>Opps, DragonStore is owner cant translate this line, sorry</p>
      <h2>Listen</h2>
      <audio src="./music/Romik19_-_Sad_Beat.mp3" controls></audio>
      <h2>Download</h2>
      <a href="https://www.newgrounds.com/audio/listen/1065750">Newgrounds</a>
    </div>';
    }
  }
}
else {
  die("<br/>Failed to verify: Try reload page and enable cookies");
}
?>