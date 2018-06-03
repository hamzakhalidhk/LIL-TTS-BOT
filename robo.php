<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet">
    <title>Robot</title>
  </head>
<body>
<div class="container">
<div class="row"><div class="col-sm-5">
<img width="400" src="eyes.png" alt="Robo Eyes"></div>
<div class="col-sm-7">
<br>
<h1 style="font-family:Oswald; font-size: 100px; color:#21618C;">Robo Hazel</h1>
</div>
</div>
<br><hr>
<div class="row">
<div class="col-sm-6">
<h4><b> To Be Announced: </b></h4></br><hr>
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "robo";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
$sql = "SELECT Message, datestamp FROM robo ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row["Message"], "<p style='color:#21618C;'>","<b>"," (" , $row["datestamp"], ")", "</b>","</p>";
    }
} else {
    echo "0 results";
}
?>
</br>
<iframe src="http://192.168.0.104/" width="200" height="80" frameborder="0" >Browser not compatible.</iframe>
</div>
<div class="col-sm-6">
<h4><b> Enter New Text to be Announced: </b></h4></br><hr>
<table width="300" border="0" align="left" cellpadding="0" cellspacing="1">
<tr>
<td><form name="form1" method="post" action="insert.php">
<table width="100%" border="0" cellspacing="1" cellpadding="3">


<textarea rows="5" cols="50" name="Message" type="text" id="Message" width="301"></textarea>


<tr>
<td colspan="3" align="right"><input type="submit" name="Submit" value="Enter"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</div>
</div></div>
</body>
</html>
