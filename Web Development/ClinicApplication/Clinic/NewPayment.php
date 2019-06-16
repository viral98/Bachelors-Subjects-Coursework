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
          <span class="mdl-layout-title">New Payment</span>
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
            <input class="mdl-textfield__input" type="date" id="Visit_Date" name="Visit_Date">
            <label class="mdl-textfield__label" for="Visit_Date">Date...</label>
          </div>
        <br>
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="time" id="Visit_Time" name="Visit_Time">
            <label class="mdl-textfield__label" for="Visit_Time">Time...</label>
          </div>
        <br>
          <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
            <input class="mdl-textfield__input" type="number" id="Amount_Paid" name="Amount_Paid">
            <label class="mdl-textfield__label" for="Amount_Paid">Paid...</label>          
          </div>
        <br>
        
          <div>
              <button type="submit" class="mdl-chip" form="senddata" name="paymentdata" id="paymentdata" formmethod="_GET">
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

          if (isset($_GET["paymentdata"])){
            $query = "Select PaymentID,BillNo from paymentmaster ORDER BY PaymentID DESC LIMIT 1";
            $result= $conn->query($query);
            $rows=$result->fetch_assoc();
            $CurrentPaymentID = $rows["PaymentID"];
            if ($CurrentPaymentID < 0){
               $NextPaymentID=1;
            }
            else{
             $NextPaymentID = $CurrentPaymentID +1;
            }
         
            $_SESSION['Paid']=$_GET["Amount_Paid"];
            $_SESSION['PhoneNumber']=$_GET["PhoneNo"];
            $_SESSION['Name']=$_GET["Patient_Name"];
            $_SESSION['PID']=$_GET["Patient_ID"];
            $_SESSION['Date'] = $_GET["Visit_Date"];
            $_SESSION['Time'] = $_GET["Visit_Time"];
            $_SESSION['NextPaymentID'] = $NextPaymentID;
            $Name = $_SESSION['Name'];
            $ID=  $_SESSION['PID'];
            $PhoneNumber =  $_SESSION['PhoneNumber'];
            //To get the patient ID from the provided details
            $getID = "Select * from patientmaster where Name = '$Name' OR PatientID = '$ID' OR Mobile = '$PhoneNumber'";
            $patientres= $conn->query($getID);
            
             echo "<br><br><table class='mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp'>",
                          "<tr><th>PatientID</th><th>Patient Name</th><th>Mobile Number</th><th>Date of Birth</th><th></th></tr>";
                    echo "<form name='ViewPatient' method='_GET'>";  

          echo "<input type='hidden' name='PaymentID1' value = $NextPaymentID>";
          echo "<input type='hidden' name='Date1' value = $Date>";
          echo "<input type='hidden' name='Time1' value = $Time>";
          echo "<input type='hidden' name='Amount_Paid1' value = $Paid>";

                     if($patientres->num_rows > 0){
                    while ($row=$patientres->fetch_assoc()) {  
                               $PatientID = $row["PatientID"];       
                            echo "<tr>". "<td>" ."" .$row["PatientID"]."</td><td>". $row["Name"]."</td><td>". $row["Mobile"]."</td><td>". $row["DateOfBirth"]."</td><td><button  class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect' type='Submit' name='ViewPatientID'  value=$PatientID id='ViewPatientID'>SELECT
              </button></td></tr>";
                                
                       }
                }
                echo "</form>";
           

            
          }
      
      if (!empty($_GET["ViewPatientID"])){
            $_SESSION["PID"] = $_GET["ViewPatientID"];
            $PID =  $_SESSION["PID"];

              $getVisitID = "Select * from visitmaster where PatientID = '$PID'";
            $patientres= $conn->query($getVisitID);

            echo "<input type='hidden' name='PaymentID2' value = $NextPaymentID>";
            echo "<input type='hidden' name='PatientID2' value = $PID>";
            echo "<input type='hidden' name='Date2' value = $Date>";
          echo "<input type='hidden' name='Time2' value = $Time>";
          echo "<input type='hidden' name='Amount_Paid2' value = $Paid>";



             echo "<br><br><table class='mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp'>",
                          "<tr><th>PatientID</th><th>Date</th><th>Remarks</th></tr>";
                    echo "<form name='ViewVisit' method='_GET'>";  
                     if($patientres->num_rows > 0){
                    while ($row=$patientres->fetch_assoc()) {  
                               $VisitID = $row["VisitID"];       
                            echo "<tr>". "<td>" ."" .$row["PatientID"]."</td><td>". $row["Date"]."</td><td>". $row["Remarks"]."</td><td><button  class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect' type='Submit' name='ViewVisitID'  value=$VisitID id='ViewVisitID'>SELECT
              </button></td></tr>";
                                
                       }
                }
                echo "</form>";
           

      }
      if (!empty($_GET["ViewVisitID"])){
        $PatID = $_SESSION["PID"];
        $VisID = $_GET["ViewVisitID"];
        $PDate = $_SESSION['Date'];
        $PTime = $_SESSION['Time'];
        $PaymentID =$_SESSION['NextPaymentID'];
        $AmountPaid=$_SESSION['Paid'];

        $BillID = $_SESSION['NextPaymentID'];
        $UserID = 1;
        
              $sql="INSERT INTO paymentmaster values ('$PaymentID','$VisID','$PatID','$UserID','$PDate','$PTime','$AmountPaid','$BillID')";
              if ($conn->query($sql) === TRUE) {
                  echo "Payment added!";
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
      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" style="position: fixed; left: -1000px; height: -1000px;">
        <defs>
          <mask id="piemask" maskContentUnits="objectBoundingBox">
            <circle cx=0.5 cy=0.5 r=0.49 fill="white" />
            <circle cx=0.5 cy=0.5 r=0.40 fill="black" />
          </mask>
          <g id="piechart">
            <circle cx=0.5 cy=0.5 r=0.5 />
            <path d="M 0.5 0.5 0.5 0 A 0.5 0.5 0 0 1 0.95 0.28 z" stroke="none" fill="rgba(255, 255, 255, 0.75)" />
          </g>
        </defs>
      </svg>
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 500 250" style="position: fixed; left: -1000px; height: -1000px;">
        <defs>
          <g id="chart">
            <g id="Gridlines">
              <line fill="#888888" stroke="#888888" stroke-miterlimit="10" x1="0" y1="27.3" x2="468.3" y2="27.3" />
              <line fill="#888888" stroke="#888888" stroke-miterlimit="10" x1="0" y1="66.7" x2="468.3" y2="66.7" />
              <line fill="#888888" stroke="#888888" stroke-miterlimit="10" x1="0" y1="105.3" x2="468.3" y2="105.3" />
              <line fill="#888888" stroke="#888888" stroke-miterlimit="10" x1="0" y1="144.7" x2="468.3" y2="144.7" />
              <line fill="#888888" stroke="#888888" stroke-miterlimit="10" x1="0" y1="184.3" x2="468.3" y2="184.3" />
            </g>
            <g id="Numbers">
              <text transform="matrix(1 0 0 1 485 29.3333)" fill="#888888" font-family="'Roboto'" font-size="9">500</text>
              <text transform="matrix(1 0 0 1 485 69)" fill="#888888" font-family="'Roboto'" font-size="9">400</text>
              <text transform="matrix(1 0 0 1 485 109.3333)" fill="#888888" font-family="'Roboto'" font-size="9">300</text>
              <text transform="matrix(1 0 0 1 485 149)" fill="#888888" font-family="'Roboto'" font-size="9">200</text>
              <text transform="matrix(1 0 0 1 485 188.3333)" fill="#888888" font-family="'Roboto'" font-size="9">100</text>
              <text transform="matrix(1 0 0 1 0 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">1</text>
              <text transform="matrix(1 0 0 1 78 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">2</text>
              <text transform="matrix(1 0 0 1 154.6667 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">3</text>
              <text transform="matrix(1 0 0 1 232.1667 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">4</text>
              <text transform="matrix(1 0 0 1 309 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">5</text>
              <text transform="matrix(1 0 0 1 386.6667 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">6</text>
              <text transform="matrix(1 0 0 1 464.3333 249.0003)" fill="#888888" font-family="'Roboto'" font-size="9">7</text>
            </g>
            <g id="Layer_5">
              <polygon opacity="0.36" stroke-miterlimit="10" points="0,223.3 48,138.5 154.7,169 211,88.5
              294.5,80.5 380,165.2 437,75.5 469.5,223.3   "/>
            </g>
            <g id="Layer_4">
              <polygon stroke-miterlimit="10" points="469.3,222.7 1,222.7 48.7,166.7 155.7,188.3 212,132.7
              296.7,128 380.7,184.3 436.7,125   "/>
            </g>
          </g>
        </defs>
      </svg>
      <a href="https://github.com/google/material-design-lite/blob/mdl-1.x/templates/dashboard/" target="_blank" id="view-source" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored mdl-color-text--white">View Source</a>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
