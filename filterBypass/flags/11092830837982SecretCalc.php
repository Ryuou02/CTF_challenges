<!DOCTYPE html>
<!-- hint : see how the eval() function can be used to retrieve the flag variable -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .calculator {
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .calculator input[type="text"], .calculator select {
            width: 100%;
            padding: 10px;
            margin: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .calculator button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
        }
        .calculator button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 10px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>Simple Calculator</h1>
        <form id="calculatorForm" method="get">
            <input type="text" id="num1" name='code' placeholder="Enter first number" required>
            <button type="submit">Calculate</button>
        </form>
        <div class="result" id="result">
<!-- code written in php:
        if(isset($_GET['code'])){
                $flag = "flag{this_is_not_real_flag}";
                $num = $_GET['code'];
                if(preg_match("/flag/i",$num) === 1)
                        die("<h1>stealing flag is not allowed</h1>");
                $num = eval("return ".$num.";");
                echo "<h3>".$num."</h3>";
                $num = eval("return ".$num.";");        // in case of other mathematical functions being used.
                echo "<h2>".$num."</h2>";
        }
-->
        <?php
        if(isset($_GET['code'])){
                $flag = "flag{the_c4lcul4t0r_is_v3ry_good_02195}";
                $num = $_GET['code'];

                if(preg_match("/flag/i",$num) === 1)
                        die("<h1>stealing flag is not allowed</h1>");
                $num = eval("return ".$num.";");
                echo "<h3>".$num."</h3>";
                $num = eval("return ".$num.";");        // in case of other mathematical functions being used.
                echo "<h2>".$num."</h2>";
        }
		?>
        </div>
    </div>
</body>
</html>
