<?php
function getUnderbarCase($string) {

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

getUnderbarCase("testVer");
