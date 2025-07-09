 <?php
$servername = "localhost";
$username = "chall2";
$password = "bi0s_chall002";

try {
  $conn = new PDO("mysql:host=$servername;dbname=db", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} 

catch(PDOException $e) 
{
  echo "<h1>Connection failed</h1><br> " . $e->getMessage();
}

?> 
