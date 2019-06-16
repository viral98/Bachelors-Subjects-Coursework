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
        <div class="demo-content">
	    <form id="senddata" method="POST">
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label search-box">
				<input class="mdl-textfield__input" type="text" id="Name" name="name" required>
				<label class="mdl-textfield__label" for="Doctor_ID">Patient Name...</label>         
			</div>
			<br>
			<br>
			<div>
				<button type="submit" class="mdl-chip" form="senddata" name="submit" id="submit">
                <span class="mdl-chip__text">Search</span>
				</button>
			</div>

        </form>	          
             <div>
		<form id='sendinfo' method="get" action="OldAddAppointment.php">
		</form>
        <?php
        //error_reporting(0);
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
		if(isset($_POST["name"]))
		{
			echo "<br><br>";
			$name=$_POST["name"];
			$sql="select * from patientmaster where Name like '%$name%' or PatientID='$name' or Mobile like '%$name%'"; //add ID and mobile no. search
			//$sql="select * from patientmaster";
			$res=$conn->query($sql);
			if ($res->num_rows > 0)
			{
				echo "<br><table class='mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp'>",
                          "<tr><th>PatientID</th><th>Patient Name</th><th>Sex</th><th>Date Of Birth</th><th>Mobile Number</th><th></th></tr>";
				while($row = $res->fetch_assoc())
				{
					$pid=$row["PatientID"];
					
					
					echo "<tr>";
					echo "<td>" . $row['PatientID'] . "</td>" . "<td>" . $row['Name'] . "</td>" . "<td>" . $row['Sex'] . "</td>";
					echo "<td>" . $row['DateOfBirth'] . "</td>" . "<td>" . $row['Mobile'] . "</td>";
					echo "<td><button type='submit'  class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect' form='sendinfo' name='id' value=$pid><i class='material-icons'>arrow_forward</i></button></td></tr>";
					if(isset($newtime))
					{
						echo "<input type='hidden' name='newtime' value='$newtime' form='sendinfo'></input>";
						
					}
					//echo "<button type='submit' class='mdl-chip' form='sendinfo' name='id' value=$pid>";
					//echo "<span class='mdl-chip__text'>" . $row["PatientID"] . " | " . $row['Name'] . "</span>";
					//echo "</button>";
				}
				echo "</table>";
			}
			
		}
		
		if(isset($_GET["id"]))
		{
			$patientid=$_GET["id"];
		?>
			<br>
			<form id="addappointment" method="post"></form>
			Date:
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="date" id="Date" name="date" form="addappointment"
				value="<?php
				echo date('Y-m-d');
				?>"
				>       
			</div>
			<br>
			Time:
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="time" id="Time" name="time" form="addappointment" 
				value="<?php
				if(isset($newtime))
				{
					echo $newtime;
				}
				else
				{
					echo date('H:i');
				}
				?>"
				>       
			</div>
			<input type="hidden" name="patientid" value="<?php echo $patientid;?>" form="addappointment">
			<br>
			<div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
				<input class="mdl-textfield__input" type="text" id="RefDocName" name="RefDocName" form="addappointment">
				<label class="mdl-textfield__label" for="RefDocName">Referral Doctor...</label>         
			</div>
			<br>
			<div class="mdl-textfield mdl-js-textfield">
				<textarea class="mdl-textfield__input" type="text" rows= "3" id="sample5"  name="remarks"></textarea>
				<label class="mdl-textfield__label" for="sample5">Appointment Remarks...</label>
			</div><br>
			
		<?php	
		
		
		$patientid=$_GET["id"];
		$namesql="select Name from patientmaster where PatientID=$patientid";
		$nameres=$conn->query($namesql);
		$namearr=$nameres->fetch_assoc();
		$name=$namearr["Name"];
		
		
		?>
		
		<div>
			<button type="submit" class="mdl-chip" form="addappointment" name="patientname" id="add" value="<?php echo $name;?>">
				<span class="mdl-chip__text">Add Appointment for <?php echo $name?></span>
			</button>
		</div>
		<?php
		}
		
		if(isset($_POST["patientname"]))
		{
			$patientid=$_POST["patientid"];
			$patientname=$_POST["patientname"];
			$date=$_POST["date"];
			$time=$_POST["time"];
			$appidsql="SELECT AppointmentID FROM appointment ORDER BY AppointmentID DESC LIMIT 1";
			$appidres= $conn->query($appidsql);
			$appidarr=$appidres->fetch_assoc();
			$refdocname=$_POST["RefDocName"];
			$appremarks=$_POST["remarks"];
			if($refdocname==NULL)
			{
				$refdocname="None";
			}
			if($appremarks==NULL)
			{
				$refdocname="None";
			}
			if($appidarr["AppointmentID"]<1)
				$appid=1;
			else
			  $appid = $appidarr["AppointmentID"]+1;
			
			$addsql="insert into appointment values($appid,$patientid,'$patientname','$date','$time','$refdocname','$appremarks')";
			if ($conn->query($addsql) === TRUE) {
				echo "Appointment Added.<br>";
            } 
			else {
				echo "Error: " . $addsql . "<br>" . $conn->error;
              }
		}
	
		
		
		
		
        $conn->close();
       ?>
    </div>
	
	<a href="ScheduleAppointment.php">
       <span class="mdl-chip">
			<span class="mdl-chip__text">Go Back</span>
		</span></a>
        </div>
      </main>
    </div>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
