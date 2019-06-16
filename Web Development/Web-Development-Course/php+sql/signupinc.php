<?php
session_start();
include 'dbh.php';

$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$email = $_POST['email'];
$pwd = $_POST['pwd'];

$sql = "SELECT * from user WHERE email='$email'" ;
$result = mysqli_query($conn,$sql);

if (!$row = mysqli_fetch_assoc($result)) {
    $sql = "INSERT INTO user (firstname,lastname,email,pwd) 
    VALUES ('$firstname','$lastname', '$email ' , '$pwd')";
    
    $result = mysqli_query($conn,$sql);
    
    $_SESSION['id'] = null;
    $_SESSION['name'] = null;
    header("Location: ./login.html");
} else {
        header("Location: ./signuperror.html");
}
