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
          <span class="mdl-layout-title">View Appointments</span>
            <div class="mdl-layout-spacer"></div>
            <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable">
                <label class="mdl-button mdl-js-button mdl-button--icon" for="search">
                    <i class="material-icons">search</i>
                </label>
                <div class="mdl-textfield__expandable-holder">
                    <input class="mdl-textfield__input" type="text" id="search">
                    <label class="mdl-textfield__label" for="search">Enter your query...</label>
                </div>
            </div>
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
			  if(isset($_POST["search"]))
			  {
				  $Test=$_POST["ViewAppt"];
			  }
			  else
			  {
				$Test = $_GET["ViewAppt"];
			  }
              $sql="SELECT * from appointment where AppointmentID = $Test";
              $row = $conn->query($sql);
              $result = $row->fetch_assoc();
          ?>
		   <?php
        if (isset($_POST["search"]))
        {
			
			$appt = $result["AppointmentID"];
			$TDate = $_POST['Date'];
			$TDate=date('Y-m-d',strtotime($TDate));
			$Time = $_POST["Time"];
			$Time=date('H:i:s',strtotime($Time));
			$remarks=$_POST["remarks"];
			$query = "UPDATE appointment SET Date='$TDate',Time='$Time',Remarks='$remarks' where AppointmentID=$appt";
			if ($flag=$conn->query($query) === TRUE) {
					
					$sql="SELECT * from appointment where AppointmentID = $Test";
					$row = $conn->query($sql);
					$result = $row->fetch_assoc();
				} else {
					echo "Error: " . $query . "<br>" . $conn->error;
				}
        }
		if(isset($_POST["delete"]))
		{
			$appt = $result["AppointmentID"];
			$sql="delete from appointment where AppointmentID=$appt";
			$res = $conn->query($sql);
			if($res)
			{
				Echo "Appointment Deleted.<br>";
				die("<a href='ScheduleAppointment.php' class='mdl-chip'>
                <span class='mdl-chip__text'>Go Back</span>
              </a> </div>

        </form>       
       
            
      </main>
    </div>
          <script src='https://code.getmdl.io/1.3.0/material.min.js'></script>
  </body>
</html>");
			}
			
		}
        ?>
        <form id="editdata" method="POST">
          <input type="hidden" name="ViewAppt" value = <?php echo $Test; ?> >
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="number" id="Appointment_ID" name="Appointment_ID" value= "<?php echo $result["AppointmentID"]; ?>" disabled>
            <label class="mdl-textfield__label" for="Appointment_ID">Appointment_ID...</label>         
          </div>
          <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="number" id="Patient_ID" name="Patient_ID" value= "<?php echo $result["PatientID"]; ?>" disabled>
            <label class="mdl-textfield__label" for="Patient_ID">PatientID...</label>         
          </div>
          <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="text" id="Patient_Name" name="Patient_Name" value= "<?php echo $result["PatientName"]; ?>" disabled>
            <label class="mdl-textfield__label" for="Patient_Name">Name...</label>
          </div>
		  <br>
		  <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="text" id="Patient_Name" name="Patient_Name" value= "<?php echo $result["RefDoctorName"]; ?>" disabled>
            <label class="mdl-textfield__label" for="Patient_Name">Referral Doctor Name...</label>
          </div>
        <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="date" id="Date" name="Date" value="<?php echo $result["Date"];?>">
            <label class="mdl-textfield__label" for="Date">Date...</label>          
          </div>
        <br>
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="time" id="Time" name="Time" value= "<?php echo $result["Time"]; ?>">
            <label class="mdl-textfield__label" for="Time">Time...</label>          
          </div>
        <br>
		<div class="mdl-textfield mdl-js-textfield">
				<textarea class="mdl-textfield__input" type="text" rows= "3" id="sample5"  name="remarks"><?php echo $result["Remarks"]; ?></textarea>
				<label class="mdl-textfield__label" for="sample5">Appointment Remarks...</label>
			</div><br>
          <div>
		  <?php
		  if (isset($_POST["search"]))
        {
		  if ($flag == TRUE) {
		  echo "Appointment Updated<br>";
		  }
		}
		  ?>
              <button type="submit" class="mdl-chip" form="editdata" name="search" id="search">
                <span class="mdl-chip__text">Edit</span>
              </button>
			  <button type="submit" class="mdl-chip" form="editdata" name="delete" id="delete">
                <span class="mdl-chip__text">Delete</span>
              </button>
			  <a href="ScheduleAppointment.php" class="mdl-chip">
                <span class="mdl-chip__text">Go Back</span>
              </a>
          </div>

        </form>       
       
            
      </main>
    </div>
          <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
