<html>
	<head>	
		<style>
		@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;900&display=swap');

input {
  caret-color: red;
}

body {
  margin: 0;
  width: 100vw;
  height: 100vh;
  background: #ecf0f3;
  display: flex;
  align-items: center;
  text-align: center;
  justify-content: center;
  place-items: center;
  overflow: hidden;
  font-family: poppins;
}

.container {
  position: relative;
  width: 350px;
  height: 500px;
  border-radius: 20px;
  padding: 40px;
  box-sizing: border-box;
  background: #ecf0f3;
  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;
}

.brand-logo {
  height: 100px;
  width: 100px;
  background: url("https://img.icons8.com/color/100/000000/twitter--v2.png");
  margin: auto;
  border-radius: 50%;
  box-sizing: border-box;
  box-shadow: 7px 7px 10px #cbced1, -7px -7px 10px white;
}

.brand-title {
  margin-top: 10px;
  font-weight: 900;
  font-size: 1.8rem;
  color: #1DA1F2;
  letter-spacing: 1px;
}

.inputs {
  text-align: left;
  margin-top: 30px;
}

label, input, button {
  display: block;
  width: 100%;
  padding: 0;
  border: none;
  outline: none;
  box-sizing: border-box;
}

label {
  margin-bottom: 4px;
}

label:nth-of-type(2) {
  margin-top: 12px;
}

input::placeholder {
  color: gray;
}

input {
  background: #ecf0f3;
  padding: 10px;
  padding-left: 20px;
  height: 50px;
  font-size: 14px;
  border-radius: 50px;
  box-shadow: inset 6px 6px 6px #cbced1, inset -6px -6px 6px white;
}

button {
  color: white;
  margin-top: 20px;
  background: #1DA1F2;
  height: 40px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 900;
  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;
  transition: 0.5s;
}

button:hover {
  box-shadow: none;
}

a {
  position: absolute;
  font-size: 8px;
  bottom: 4px;
  right: 4px;
  text-decoration: none;
  color: black;
  background: yellow;
  border-radius: 10px;
  padding: 2px;
}

h1 {
  position: absolute;
  top: 0;
  left: 0;
}
		</style>
		<title>The Video</title>
	</head>
<body>
<?php
	if(isset($_REQUEST['username'])&&isset($_REQUEST['password']))	
	{
		if($_REQUEST['username'] == 'admin')
		{
			if($_REQUEST['password'] == 'IamTheADMIN!')
			{
        if(isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
          if($_SERVER['HTTP_X_FORWARDED_FOR'] === '0.0.0.0')
          {
            echo "<h1>good job with all the effort, here's the flag:<br>flag{I_kn0w_y0uR_LOC4T10N}<br></h1><br><h2>also, here's a bonus video:</h2>";
            echo "<img src='https://www.youtube.com/watch?v=D9-voINFkCg&pp=ygUec2FtaXIgeW91J3JlIGJyZWFraW5nIHRoZSBjYXIg'>";
          }
        }
				else{
					echo "<h1>hahaha, you thought if you had admin password it would be enough?</h1><br><h2>the admin always logs in with the IP address 0.0.0.0</h2><br>";
					echo "<img src='https://imgs.search.brave.com/TrAr-VGcDswex5hWcSUq4Vwc4GAzJeoGVNwkq78qB-Y/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS50ZW5vci5jb20v/Y0lLcll3ZkZ0ZTRB/QUFBai9tci1iZWFu/LWxhdWdoLmdpZg.gif'>";
				}
			}
			else{
				echo "<h1>incorrect password</h1>";
			}
		}
		else{
			echo "<h1>please login as an admin</h1>";
		}
	}
	else{
?>

<form method="POST" action="index.php">
<div class="container">
  <div class="inputs">
    <label>USERNAME</label>
    <input type="username" placeholder="username" name='username'>
    <label>PASSWORD</label>
    <input type="password" placeholder="password" name='password'>
    <button type="submit">LOGIN</button>
  </div>
<!-- I have kept the admin password here so that I don't forget
password:IamTheADMIN!
-->
</div>
</form>
<?php	}
?>
</body>
</html>
