<?php   
 //Above HTML  
 $name_error = '';  
 $email_error = '';  
 $password_error = '';  
 $output = '';  
 if(isset($_POST["submit"]))  
 {  
      if(empty($_POST["name"]))  
      {  
           $name_error = "<p>Please Enter Name</p>";  
      }  
      else  
      {  
           if(!preg_match("/^[a-zA-Z ]*$/", $_POST["name"]))  
           {  
                $name_error = "<p>Only Letters and whitespace allowed</p>";  
           }  
      }  
      if(empty($_POST["email"]))  
      {  
           $email_error = "<p>Please Enter Email</p>";  
      }  
      else  
      {  
           if(!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL))  
           {  
                $email_error = "<p>Invalid Email formate</p>";  
           }  
      }  
      if(empty($_POST["password"]))  
      {  
           $password_error = "<p>Enter Password.</p>";  
      }
      else{
        if(!preg_match("/(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,12})/", $_POST["password"]))  
           {  
                $password_error = "<p>Update password</p>";  
           }  
      }  
      if($name_error == "" && $email_error == "" && $password_error == "")  
      {  
           $output = '<p><label>Ouput-</label></p>  
           <p>Your Name is '.$_POST["name"].'</p>  
           <p>Your Email is '.$_POST["email"].'</p>  
           <p>Your Password is '.$_POST["password"].'</p>  
           ';  
      }       
 }  
 ?>  
 <!DOCTYPE html>  
 <html>  
      <head>  
           <title>Webslesson Tutorial | PHP Server Side Form Validation</title>  
           <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>  
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />  
           <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>  
      </head>  
      <body>  
           <br />  
           <div class="container" style="width:500px;">  
                <h3 class="text-center">PHP Server Side Form Validation</h3>  
                <form method="post">  
                     <div class="form-group">  
                          <label>Enter Name<span class="text-danger">*</span></label>  
                          <input type="text" name="name" class="form-control" maxlength="75" />  
                          <span class="text-danger"><?php echo $name_error; ?></span>  
                     </div>  
                     <div class="form-group">  
                          <label>Enter Email<span class="text-danger">*</span></label>  
                          <input type="text" name="email" class="form-control" maxlength="150" />  
                          <span class="text-danger"><?php echo $email_error; ?></span>  
                     </div>  
                     <div class="form-group">  
                          <label>Enter Password<span class="text-danger">*</span></label>  
                          <input type="text" name="password" class="form-control" maxlength="150" />  
                          <span class="text-danger"><?php echo $password_error; ?></span>  
                     </div>  
                     <div class="form-group">  
                          <input type="submit" name="submit" value="Submit" class="btn btn-info" />  
                     </div>  
                </form>  
                <div><?php echo $output; ?></div>  
           </div>  
           <br />  
      </body>  
 </html>  