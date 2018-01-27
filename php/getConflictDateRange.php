<?php

// $a_start = new DateTime("2017-01-01 00:00:00");
// $a_end = new DateTime("2017-05-01 15:00:00");
// $b_start = new DateTime("2017-01-03 02:00:01");
// $b_end = new DateTime("2017-05-20 00:00:00");

function getConflictDateRange($inputDate1, $inputDate2) {
  $dateFir = explode("~", $inputDate1);
  $dateScd = explode("~", $inputDate2);
  $re1 = null;
  $re2 = null;

  for ($i = 0; $i < count($dateFir); $i++)  {
      $dateFir[$i] = new DateTime(trim($dateFir[$i]));
      $dateScd[$i] = new DateTime(trim($dateScd[$i]));
  }

  if ($dateFir[0] < $dateScd[0]) {
    if ($dateFir[1] < $dateScd[0]) {
      return echo "your input value is not right Date Value :) try again please!";
    } else {
      $re1 = $dateScd[0];
      if ($dateFir[1] < $dateScd[1]) {
        $re2 = $dateFir[1];
      } else {
        $re2 = $dateScd[1];
      }
    }
  } else {
    if ($dateScd[1] < $dateFir[0]) {
      return echo "your input value is not right Date Value :) try again please!";
    } else {
      $re1 = $dateFir[0];
      if ($dateScd[1] < $dateFir[1]){
          $re2 = $dateScd[1];
      } else {
          $re2 = $dateFir[1];
      }
    }
  }
  if ($re1 !=null || $re2 !=null) {
    return echo "Date Value : ".date_format($re1,'Y-m-d H:i:s')." ~ ".date_format($re2,'Y-m-d H:i:s');
  }
}

getConflictDateRange("2017-01-01 00:00:00 ~ 2017-05-01 15:00:00","2017-01-03 02:00:01 ~ 2017-05-20 00:00:00");

?>
