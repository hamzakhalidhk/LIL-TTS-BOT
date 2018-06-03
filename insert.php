<?php
 if(isset($_POST['Submit']))
{
	$Message=$_POST["Message"];
}
$servername = "localhost";
$database = "robo";
$username = "root";
$password = "";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
}
 
echo "Connected successfully";
 
$sql = "INSERT INTO robo (datestamp,Message) VALUES (NOW(), '$Message' )";
if (mysqli_query($conn, $sql)) {
	header('Location: robo.php');
      echo "New record created successfully";
} else {
      echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
mysqli_close($conn);
?>
