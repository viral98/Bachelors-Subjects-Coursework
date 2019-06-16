<?php
include('session.php');
?>
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
          <span class="mdl-layout-title">Add Visit</span>
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
                <a class="mdl-navigation__link" href="ViewVisits.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">inbox</i>Visits</a>
                <a class="mdl-navigation__link" href=""><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">delete</i>Reports</a>
                <a class="mdl-navigation__link" href="AddPatient.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">report</i>Patients</a>
                <a class="mdl-navigation__link" href="ViewDoctor.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">forum</i>Doctors</a>
                <a class="mdl-navigation__link" href="NewPayment.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">flag</i>Payments</a>
                <a class="mdl-navigation__link" href="ScheduleAppointment.php"><i class="mdl-color-text--blue-grey-400 material-icons" role="presentation">local_offer</i>Schedule Appointments</a>
            </nav>
        </div>
      <main class="mdl-layout__content mdl-color--grey-100">
        <div class="mdl-grid demo-content">
          <form id="senddata" method="_GET">
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="number" id="Patient_ID" name="Patient_ID">
            <label class="mdl-textfield__label" for="Patient_ID">Patient ID...</label>         
          </div>
          <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="number" id="PhoneNo" name="PhoneNo">
            <label class="mdl-textfield__label" for="PhoneNo">Phone Number...</label>         
          </div>
          <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="text" id="Patient_Name" name="Patient_Name">
            <label class="mdl-textfield__label" for="Patient_Name">Name...</label>
          </div>
        <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="text" id="Visit_Remarks" name="Visit_Remarks">
            <label class="mdl-textfield__label" for="Visit_Remarks">Remarks...</label>          
          </div>
        <br>
        
          <div>
              <button type="submit" class="mdl-chip" form="senddata" name="visitdata" id="visitdata" formmethod="_GET">
                <span class="mdl-chip__text">Submit</span>
              </button>
          </div>

        </form>           
        <div>
        <?php
          error_reporting(0);
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

         // $datestring = "%Y:%m:%d %h:%i:%s";
          //$time = time();
          $createdate = date('Y-m-d H:i:s');

          if (isset($_GET["visitdata"])){
            $query = "Select VisitID from visitmaster ORDER BY VisitID DESC LIMIT 1";
            $result= $conn->query($query);
            $rows=$result->fetch_assoc();
            $CurrentVisitID = $rows["VisitID"];
            if ($CurrentVisitID < 0){
              $NextVisitID=1;
            }
            else{
            $NextVisitID = $CurrentVisitID +1;
            }

            $Remarks=$_GET["Visit_Remarks"];
            $PhoneNumber=$_GET["PhoneNo"];
            $Name=$_GET["Patient_Name"];
            $ID=$_GET["Patient_ID"];

            //To get the patient ID from the provided details
            $getID = "Select * from patientmaster where Name = '$Name' OR PatientID = '$ID' OR Mobile = '$PhoneNumber'";
            $patientres= $conn->query($getID);
            
             echo "<br><br><table class='mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp'>",
                          "<tr><th>PatientID</th><th>Patient Name</th><th>Mobile Number</th><th>Date of Birth</th><th></th></tr>";
                    echo "<form name='ViewPatient' method='_GET'>";  
					echo "<input type='hidden' name='visitid' value = $NextVisitID>";
                     if($patientres->num_rows > 0){
                    while ($row=$patientres->fetch_assoc()) {  
                               $PatientID = $row["PatientID"];       
                            echo "<tr>". "<td>" ."" .$row["PatientID"]."</td><td>". $row["Name"]."</td><td>". $row["Mobile"]."</td><td>". $row["DateOfBirth"]."</td><td><button  class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect' type='Submit' name='ViewPatientID'  value=$PatientID id='ViewPatientID'>SELECT
              </button></td></tr>";
                                
                       }
                }
                echo "</form>";
           

            
          }
		  $UserID = 1;
		  if (!empty($_GET["ViewPatientID"])){
              $PID = $_GET["ViewPatientID"];
			  $NextVisitID = $_GET["visitid"];
              $sql="INSERT INTO visitmaster values ('$NextVisitID','$PID','$UserID','17-06-19','22:00:00','$Remarks')";
              if ($conn->query($sql) === TRUE) {
                  echo "New record created successfully";
              } else {
                   echo "Error: " . $sql . "<br>" . $conn->error;
              }
            }
        $conn->close();
       ?>
    </div>
       
        </div>
      </main>
    </div>

    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
