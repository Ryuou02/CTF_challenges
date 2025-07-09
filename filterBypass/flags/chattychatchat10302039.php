<?php
if (isset($_POST['message'])) {
    $message = htmlspecialchars(urldecode($_POST['message']));
    //$webpage= file_get_contents("https://blog.reedsy.com/short-story/tr8sda/");
    $webpage= file_get_contents("ThisIsAveryLongFileNameThatHopefullyWontBeBruteforce038192");
	$webpage = preg_replace("/[\w\s\W]*<article class\=\"font-alt submission-content space-top-xs-md space-bottom-xs-lg\">/","",$webpage);
	$webpage = preg_replace("/<\/article>[\w\s\W]*/","",$webpage);
    $webpage = preg_replace("/<[\w]*>|<\/[\w]*>/","",$webpage);	
	$sentences = explode(".",$webpage);

	if(preg_match("/[^a-z\s]/i",$message) === 1)
		die("only lowercase alphabets are allowed");

	$message = preg_replace("/naughty|bad|useless|flag/i","",$message);

	if($message == "")
		die("don't say only bad things. The words - nau**ty, bad, use***ss, fl*g are bad words");
	$pattern = "/".$message."/i";
	for($i = 0; $i < count($sentences); $i++){
		if(preg_match_all($pattern,$sentences[$i]) >0)
			die($sentences[$i]);
	}
	echo "looks like there is nothing for me to say to that!";
} else {
    echo 'No message received';
}
?>
