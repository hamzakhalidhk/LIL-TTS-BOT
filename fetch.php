<?php
$servername = "localhost";
$username = "root";
$password = "";
$db = "Robo";
$link = mysqli_connect($servername,$username,$password,$db) or die("Failed to connect");
$sql= "SELECT * FROM Robo ORDER BY id DESC LIMIT 1";
$query=mysqli_query($link,$sql);
while($row=mysqli_fetch_array($query)){
	echo $row['Message'];	
}
?>
