<html>
<title>
	Entry to the explicit words challenges
</title>
<body>
<h1>hello enter the password to get links to the bot</h1>
<form method = 'get'>
	<input type="text" name="pass">
	<button type="submit">try this</button>
</form>
<!-- if(md5($_GET['pass']) == 0){
	// gives flag
	part3 : _some_flags}
 }-->
<?php
	if(isset($_GET['pass'])){
		if(md5($_GET['pass']) == 0){
			echo "that's the correct password!<br>click <a href=secretChatBot.html>here</a> to go to talk to the story-bot!<br> since it may have been difficult to get this challenge, here's a flag to keep you going - flag{strcmp_is_easy_to_break_with_Arrays}";
		}
		else{
			die("wrong password");
		}
	}
?>
</body>
</html>
