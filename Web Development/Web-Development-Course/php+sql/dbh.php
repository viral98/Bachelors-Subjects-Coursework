<?php

$conn = mysqli_connect("localhost","root","","elearntest");

if(!$conn) {
    die("Connection Failed: ".mysqli_connect_error()); //remove mysqli
    echo "Please try again";
}
?>