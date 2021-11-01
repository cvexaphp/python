<?php
ini_set('display_errors', 1);

$baseUrl = 'http://api.weatherstack.com/';

$param = $_GET['city'] ?? 'Sofia';

print_r(file_get_contents($baseUrl.'current?access_key=c7a0375217eb9bdf535ebb72e6c195b8&query='.$param));