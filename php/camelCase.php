<?php

function insertCamelCase($string) {

  $val = "";

  for ($i = 0; $i < strlen($string); $i++) {
    if (preg_match('/[A-Za-z]+/', $string[$i])) {
      $val = $val.strtolower($string[$i]);
    } elseif (preg_match('/[!#$%^&*()?+=\/_]+/', $string[$i])) {
        $val = $val.strtoupper($string[$i+1]);
        $i = $i + 1;
    }
  }

  echo $val;
}

insertCamelCase("TEST_VAR");
?>
