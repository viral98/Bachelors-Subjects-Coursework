<?php
include '../includes/connect.php';
$success=false;

$username = $_POST['username'];
$password = $_POST['password'];

$result = mysqli_query($con, "SELECT * FROM employee WHERE username='$username' AND password='$password' AND not deleted;");
while($row = mysqli_fetch_array($result))
{
	$success = true;
	$user_id = $row['id'];
	$name = $row['name'];
	$role= $row['role'];
}
if($success == true)
{
	session_start();
	$_SESSION['admin_sid']=session_id();
	$_SESSION['user_id'] = $user_id;
	$_SESSION['role'] = $role;
	$_SESSION['name'] = "Employee";

	header("location: ../admin-page.php");
}
else
{
	$result = mysqli_query($con, "SELECT * FROM customer WHERE username='$username' AND password='$password' AND not deleted;");
	while($row = mysqli_fetch_array($result))
	{
	$success = true;
	$user_id = $row['id'];
	$name = $row['name'];
	$role= $row['role'];
	}
	if($success == true)
	{
		session_start();
		$_SESSION['customer_sid']=session_id();
		$_SESSION['user_id'] = $user_id;
		$_SESSION['role'] = $role;
		$_SESSION['name'] = "Customer";
		header("location: ../index.php");
	}
	else
	{
		header("location: ../login.php");
	}
}
?>
