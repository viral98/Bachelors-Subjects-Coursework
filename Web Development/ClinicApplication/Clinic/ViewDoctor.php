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
          <span class="mdl-layout-title">Doctors</span>
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
        <div class="demo-content">
        <form name = "date_select" method="GET" action="ViewDoctor.php">
         <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            Name:<input class="mdl-textfield__input" type="text" id="doctorname" name="doctorname">        
        </div>
        <br>
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            Speciality:<input class="mdl-textfield__input" type="text" id="speciality" name="speciality">        
        </div>
       
         <!--  Code which can be used but has some bugs as of now 
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
             $result = $conn->query("select DoctorID,speciality from doctormaster");
            echo "<select name='speciality'>";
            while ($row = $result->fetch_assoc()) {
              unset($speciality,$id);
              $speciality = $row['Speciality'];
              $id = $row['DoctorID'];
              echo '<option value="'.$id.'">'.$speciality.'</option>';
              echo "</select>"; 
            }
             $conn->close();
          ?>-->

         
       
        <div>
           <button type="submit" class="mdl-chip" name="search" id="search">
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
              $tdate = '0';
              if (isset($_GET["search"])){
                $id=$_GET["speciality"];
                $name = $_GET["doctorname"];
               // echo "pressed.";
              }
              else {
                
                $tdate = date('y-m-d');
             }
              $sql="SELECT * from doctormaster where Name = '$name'";
                   $result = $conn->query($sql);
					//show Doctor remarks, referring doctor and phone no.
                   echo "<br><br><table class='mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp'>";
				   echo "<tr><th>DoctorID</th><th>DoctorName</th><th>Active</th><th>PhoneNumber</th><th>Remarks</th><th>View Info</th></tr>";
                          
                    echo "<form name='ViewDoctor' method='_GET' action='ViewDoctorInfo.php'>";  
                     if($result->num_rows > 0){
                    while ($row=$result->fetch_assoc()) {  
                               echo "<tr>";
							   echo "<td>". $row['DoctorID']. "</td>";
							   $did=$row['DoctorID'];
							   echo "<td>". $row['Name']. "</td>";
							   /*$pid=$row['DoctorID'];
							   $namesql="select Name from doctormaster where DoctorID=$pid";
							   $nameres=$conn->query($namesql);
							   $namerow=$nameres->fetch_assoc();*/
							   echo "<td>". $row['Active']. "</td>";
							   echo "<td>". $row['PhoneNumber']. "</td>";
							   echo "<td>". $row['Remarks']. "</td>";
							   echo "<td><button  class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect' type='Submit' name='Doctor' value= $did id='ViewAppt'><span class='mdl-chip__text'>VIEW INFO</span>
              </button></td>";
                       }
                }
                echo "</form>";
				echo "</table>"; 
             ?>
          </div> 
          <div>
		  <br>
          </div>
        </div>
      </main>
    </div>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
