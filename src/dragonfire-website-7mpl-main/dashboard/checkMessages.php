<?php
$conn = new mysqli('localhost', 'denispolevin_dragonfire', 'connectdf', 'denispolevin_dragonfire');

if($conn->connect_error){
    die("Error: " . $conn->connect_error);
}
$sql = "SELECT * FROM messages";
      
if($result = $conn->query($sql)){
    $rowsCount = $result->num_rows;
    echo '<div class="main">';
    echo '<p>Objects received: </p>';
    echo $rowsCount;
    echo "<table><tr><th>Username</th><th>Email</th><th>Message</th></tr>";
    foreach($result as $row){
        echo "<tr>";
        echo "<td>" . $row["username"] . "</td>";
        echo "<td>" . $row["email"] . "</td>";
        echo "<td>" . $row["message"] . "</td>";
        echo "</tr>";
    }
    echo "</table></div>";
    $result->free();
} else{
    echo "Error: " . $conn->error;
}
$conn->close();
?>