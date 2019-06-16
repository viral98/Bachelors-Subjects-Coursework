<!doctype html>
<!--
  Material Design Lite
  Copyright 2015 Google Inc. All rights reserved.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License
-->
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="A front-end template that helps you build fast, modern mobile web apps.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <title>Clinic Application</title>

    <!-- Add to homescreen for Chrome on Android -->
    <meta name="mobile-web-app-capable" content="yes">
    <link rel="icon" sizes="192x192" href="images/android-desktop.png">

    <!-- Add to homescreen for Safari on iOS -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="Material Design Lite">
    <link rel="apple-touch-icon-precomposed" href="images/ios-desktop.png">

    <!-- Tile icon for Win8 (144x144 + tile color) -->
    <meta name="msapplication-TileImage" content="images/touch/ms-touch-icon-144x144-precomposed.png">
    <meta name="msapplication-TileColor" content="#3372DF">

    <link rel="shortcut icon" href="images/favicon.png">

    <!-- SEO: If your mobile URL is different from the desktop URL, add a canonical link to the desktop page https://developers.google.com/webmasters/smartphone-sites/feature-phones -->
    <!--
    <link rel="canonical" href="http://www.example.com/">
    -->

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:regular,bold,italic,thin,light,bolditalic,black,medium&amp;lang=en">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.cyan-light_blue.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
    #view-source {
      position: fixed;
      display: block;
      right: 0;
      bottom: 0;
      margin-right: 40px;
      margin-bottom: 40px;
      z-index: 900;
    }
    </style>
  </head>
  <body>
  <?php
  $servername = "localhost";
          $username = "root";
          $password = "";
          $dbname = "clinic";

          // Create connection
          $conn = new mysqli($servername, $username, $password, $dbname);
          // Check connection
          if ($conn->connect_error) {
              die("Connection failed: " . $conn->connect_error);
          } 
		  if(isset($_GET["newtime"]))
		{
			$newtime=$_GET["newtime"];
			
		}
	?>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      <header class="demo-header mdl-layout__header mdl-color--grey-100 mdl-color-text--grey-600">
        <div class="mdl-layout__header-row">
          <span class="mdl-layout-title">Add Appointment</span>
            <div class="mdl-layout-spacer"></div>
            
            <button class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--icon" id="hdrbtn">
                <i class="material-icons">more_vert</i>
            </button>
            <ul class="mdl-menu mdl-js-menu mdl-js-ripple-effect mdl-menu--bottom-right" for="hdrbtn">
                <a class="mdl-navigation__link" href="logout.php"><li class="mdl-menu__item">LogOut</li></a>
            </ul>
        </div>
      </header>
        <div class="demo-drawer mdl-layout__drawer mdl-color--blue-grey-900 mdl-color-text--blue-grey-50">
            <header class="demo-drawer-header">


            </header>
            <nav class="demo-navigation mdl-navigation mdl-color--blue-grey-800">
                <a class="mdl-navigation__link" href="ScheduleAppointment.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">home</i>Home</a>
                <a class="mdl-navigation__link" href="ViewPatients.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">people</i>View Patients</a>
                <a class="mdl-navigation__link" href="AddPatient.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">add</i>Add Patient</a>
            </nav>
        </div>
      <main class="mdl-layout__content mdl-color--grey-100">
        
	    <form id="senddata" method="POST">
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="text" id="Name" name="name" required>
				<label class="mdl-textfield__label" for="Doctor_ID">Patient Name...</label>         
			</div>
			<br>
			Sex:<br>
			<label class="mdl-radio mdl-js-radio mdl-js-ripple-effect" for="male">
				<input type="radio" id="male" class="mdl-radio__button" name="sex" value="Male" checked>
				<span class="mdl-radio__label">Male</span>
			</label>
			<label class="mdl-radio mdl-js-radio mdl-js-ripple-effect" for="female">
				<input type="radio" id="female" class="mdl-radio__button" name="sex" value="Female">
				<span class="mdl-radio__label">Female</span>
			</label>
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="text" id="Address" name="address" >
				<label class="mdl-textfield__label" for="Address">Address...</label>         
			</div>
			
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="text" id="City" name="city" >
				<label class="mdl-textfield__label" for="City">City...</label>         
			</div>
			
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="text" id="State" name="state" >
				<label class="mdl-textfield__label" for="State">State...</label>         
			</div>
			
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="text" id="Country" name="country" >
				<label class="mdl-textfield__label" for="Country">Country...</label>         
			</div>
			
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="number" id="Pin" name="pincode" >
				<label class="mdl-textfield__label" for="Pin">Pin Code...</label>         
			</div>
			<br>
			Date Of Birth:
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="date" id="Dob" name="dob"> 
			</div>
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="email" id="Email" name="email">
				<label class="mdl-textfield__label" for="Email">Email...</label>         
			</div>
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="number" id="Mobile" name="mobile" maxlength="10"  min="1000000000" max="9999999999" required>
				<label class="mdl-textfield__label" for="Mobile">Mobile Number...</label>         
				<span class="mdl-textfield__error">Enter a valid number!</span>
			</div>
			
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="number" id="Residence" name="residence">
				<label class="mdl-textfield__label" for="Residence">Residence Number...</label>         
			</div>
			
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="number" id="Office" name="office">
				<label class="mdl-textfield__label" for="Office">Office Number...</label>         
			</div>
			<br>
			
			<div class="mdl-textfield mdl-js-textfield">
				<textarea class="mdl-textfield__input" type="text" rows= "3" id="sample5"  name="remarks"></textarea>
				<label class="mdl-textfield__label" for="sample5">Patient Remarks...</label>
			</div>
			<br>
			
			<br>
			
			<div>
				<button type="submit" class="mdl-chip" form="senddata" name="submit" id="submit">
                <span class="mdl-chip__text">Submit</span>
				</button>
				<a href="ScheduleAppointment.php" class="mdl-chip">
                <span class="mdl-chip__text">Go Back</span>
              </a>
			</div>

        </form>	          
             <div>
        <?php
          //error_reporting(0);
          
          if (isset($_POST["submit"]))
          {
			$name =$_POST["name"];
			$sex =$_POST["sex"];
            $address =$_POST["address"];
            $city =$_POST["city"];
            $state =$_POST["state"];
            $country =$_POST["country"];
            $pin=$_POST["pincode"];
            $dob =$_POST["dob"];
            $email=$_POST["email"];
            $mobile=$_POST["mobile"];
            $residence=$_POST["residence"];
			
			if($residence<1)
			{
				$residence=0;
			}
			$office=$_POST["office"];
			if($office<1)
			{
				$office=0;
			}
			$remarks=$_POST["remarks"];
			
			$pidsql="SELECT PatientID FROM patientmaster ORDER BY PatientID DESC LIMIT 1";
			$pidres= $conn->query($pidsql);
			$pidarr=$pidres->fetch_assoc();
			if($pidarr["PatientID"]<1)
				$pid=1;
			else
			  $pid = $pidarr["PatientID"]+1;
			
			
			if($address==NULL)
			{
				$address="None";
			}
			if($city==NULL)
			{
				$city="None";
			}
			if($state==NULL)
			{
				$state="None";
			}
			if($country==NULL)
			{
				$country="None";
			}
			if($pin==NULL)
			{
				$pin=0;
			}
			if($email==NULL)
			{
				$email="None";
			}
			if($dob==0)
			{
				$dob=time();
				
			}
			$patientsql="insert into patientmaster values($pid,'$name','$sex','$address','$city','$state','$country',$pin,'$dob','$email',$mobile,$residence,$office,'$remarks')";
			if ($conn->query($patientsql) === TRUE) {
				echo "Patient Added.<br>";
            } 
			else {
				echo "Error: " . $patientsql . "<br>" . $conn->error;
              }
			 
			
			 
			$dbName = $_SERVER["DOCUMENT_ROOT"] . "/patients.mdb";
			if (!file_exists($dbName)) {
				die("Could not find database file.");
			}
			$db = new PDO("odbc:DRIVER={Microsoft Access Driver (*.mdb)}; DBQ=$dbName; Uid=; Pwd=;");

			$result=$db->query($patientsql);
			if($result)
			{
				echo "Done";
				
			}
			else
			{
				echo $patientsql . "<br>";
				print_r($db->errorInfo());
			}
			
		}
		  
		
              
          
          
	
        $conn->close();
       ?>
    </div>
       
        
      </main>
    </div>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
