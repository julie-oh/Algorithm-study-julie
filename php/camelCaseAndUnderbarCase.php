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

function insertUnderBar($string) {

  $val = "";

  for ($i = 0; $i < strlen($string); $i++) {
    if(preg_match('/[A-Z]+/', $string[$i])) {
      $val = $val."_".strtolower($string[$i]);
    } else {
      $val = $val.strtolower($string[$i]);
    }
  }

  echo $val;
}

insertUnderBar("testVer");

// for ($i = 0; $i < strlen($a); $i++) {
//     if(preg_match('/[A-Z]+/', $a[$i])) {
//         $val = $val."_".strtolower($a[$i]);
//     } elseif (preg_match('/[!#$%^&*()?+=\/_]/', $a[$i])) {
//         $val = $val.strtoupper($a[$i+1]);
//         $i = $i + 1;
//     } else {
//         $val = $val.$a[$i];
//     }
// }
//
// echo $val;
