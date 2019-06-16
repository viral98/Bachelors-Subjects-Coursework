<?php
    session_start();
    include 'dbh.php';

    $email = $_POST['email'];
    $pwd = $_POST['pwd'];

    $sql = "SELECT * from user WHERE email='$email' AND pwd='$pwd' " ;

    $result = mysqli_query($conn,$sql);

    if (!$row = mysqli_fetch_assoc($result)) {
        header("Location: ../loginerror.html"); //WILL GIVE 404 
    } 
    else {
            $_SESSION['id'] = $row['id'];
            $_SESSION['name'] = $row['firstname'];
            if(!$_SESSION['from_url']){
            header("Location: ../index.php"); //WILL GIVE 404
            }
            else{
                header("Location: ".$_SESSION['from_url']);
                $_SESSION['from_url'] = null;
            }
    }
?>
