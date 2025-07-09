<html>
    <head>
        <style>
		@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;900&display=swap');

          input {
            caret-color: red;
          }

          body {
            margin: 0;
            width: 110vw;
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
            width: 800px;
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


          h1 {
            position: absolute;
            top: 0;
            left: 0;
          }

        </style>
        <title>
            search the link
        </title>
    </head>
<body>
<form action="index.php" METHOD="POST">
<div class="container">
  <div class="inputs">
    <label>FLAG</label>
    <input type="text" placeholder="mimimimi" name='flag'>
    <button type="submit">check</button>
  </div>
</form>
<!-- 'help' is a nice flag-->
<!-- none of the video links contain the flag -->
<?php
    include('conn.php');
    if(isset($_REQUEST['flag']))
    {
    	  $flag = $_REQUEST['flag'];
    	  try{
          $sql = $conn->query('SELECT * from flags where flag = "'.$flag.'";');
          echo ("
          <table border=1>
          <tr>
            <th>flag</th>
            <th>video link</th>
          </tr>
          ");
			    while($result = $sql->fetch())
			    {
            echo "<tr><td>".$result['flag']."</td>";
            echo "<td><a href=".$result['vl'].">click here</a></td></tr>";
          }
      echo("
      </table>
      ");
      }
		catch(PDOException $e){
			echo "error".$e;
		}
	  $mysqli -> close();
	    
  }  
?>
</div>
</body>
</html>
