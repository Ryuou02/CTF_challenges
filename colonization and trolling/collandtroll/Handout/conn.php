 <?php
$servername = "sql.freedb.tech";
$username = "freedb_chall2";
$password = "DDyce!5nhyCYmr&";

try {
  $conn = new PDO("mysql:host=$servername;dbname=freedb_challenge", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} 

catch(PDOException $e) 
{
  echo "<h1>Connection failed</h1><br> " . $e->getMessage();
}

?> 
