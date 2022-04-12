<?php
$method = $_GET['method'];

// Status Check
if ($method == 'checkSqlStatus') {
	$conn = new mysqli('localhost', 'denispolevin_dragonfire', 'connectdf', 'denispolevin_dragonfire');
	if (!$conn) {
		http_response_code(500);
		$conn->close();
	}
	http_response_code(200);
	$conn->close();
}
elseif ($method == 'checkWebServerStatus') {
	$filename = 'callbackApi.php';

	if(file_exists($filename)) {
		http_response_code(200);
	}else {
		http_response_code(500);
	}
}
// Redirect to API Documentation
elseif ($method == 'documentationRedirect') {
	echo "Redirecting...";
	echo 'Response code: 202';
	http_response_code(202);
	header('Location: documentation.html');
}
// Your own response code
elseif ($method == 'ownReponseCode') {
	$responseCode = $_GET['responseCode'];
	echo "Response code: " + $responseCode;
	http_response_code($responseCode);
}
// Cookie check
elseif ($method == 'cookieCheck') {
	setcookie("cookieCheck", 'cookieOkDF');
	if ($_COOKIE["cookieCheck"] == 'cookieOkDF') {
		echo 'Response code: 200 (Ok)';
		http_response_code(200);
	}
	else {
		echo 'An error has occurred. Error Code: 406 (Not Acceptable)';
		echo '<br/>Failed to set cookie';
		http_response_code(406);
	}
}
// API check
elseif ($method == 'testApi') {
	echo 'Response code: 202';
	http_response_code(202);
}
// Error if argument is missing or invalid
else {
	echo 'An error has occurred. Error Code: 400 (Bad Request)';
	http_response_code(400);
}
?>