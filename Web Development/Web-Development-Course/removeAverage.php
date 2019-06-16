<?php

//Our array, which contains a set of numbers.
$array = array(1, 7, 9, 3, 20, 12, 2, 9);
//Calculate the average.
$average = array_sum($array) / count($array);
//Print out the average.
echo $average;
$average =0;
//------Same Operation, Using constants--------//
define ("numberss", serialize (array (1, 7, 9, 3, 20, 12, 2, 9)));
$my_numbers = unserialize (numberss);
$average = array_sum($my_numbers) / count($my_numbers);
//Print out the average.
echo "<br> Printing const array average <br>";
echo $average;

?>