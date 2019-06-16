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
    <title>Material Design Lite</title>

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
		 <form id="viewpatient" method="get" action="ViewPatientInfo.php"></form>
		<form id="page" method="get" action="ViewPatients.php"></form>
		<form id="search" method="post" action="ViewPatients.php"></form>
		<form id="sendpage" method="post" action="ViewPatientInfo.php"></form>
          <span class="mdl-layout-title">View Patients
		  <?php
		  $servername = "localhost";
				$username = "root";
				$password = "";

				// Create connection
				$conn = new mysqli($servername, $username, $password,"clinic");

				// Check connection
				if ($conn->connect_error) {
					die("Connection failed: " . $conn->connect_error);
				} 
				
				
				
		
				$sqlpage="SELECT count(*) AS pagecount from patientmaster";
				$pageresult= $conn->query($sqlpage);
				$countarray=$pageresult->fetch_assoc();
				$k=0;
				$k3=0;
				if(isset($_GET["pagenumber"]))
				{
					$k=$_GET["pagenumber"];
				}
				if(isset($_POST["pagenumber"]))
				{
					$k=$_POST["pagenumber"];
				}
				for($k3;$k3<$countarray["pagecount"];$k3=$k3+12)
				{
				}
			
				$k1=$k-12;
				$k2=$k+12;
			?>
		    <div class="mdl-textfield mdl-js-textfield">
			<input class="mdl-textfield__input" type="text" id="search" form="search" name="searchterm">
			<label class="mdl-textfield__label" for="search">Search Term</label>
			</div>
			<button type="submit" form="search" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect" name="search">
				Search
			</button>
			
		  </span>
          <div class="mdl-layout-spacer"></div>
          
          <button class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--icon" id="hdrbtn">
            <i class="material-icons">more_vert</i>
          </button>
          <ul class="mdl-menu mdl-js-menu mdl-js-ripple-effect mdl-menu--bottom-right" for="hdrbtn">
            <li class="mdl-menu__item">About</li>
            <li class="mdl-menu__item">Contact</li>
            <li class="mdl-menu__item">Legal information</li>
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
			if(isset($_POST["submit"]))
				{
					$patientid=$_POST["patientid"];
					$patientname=$_POST["patientname"];
					//$sex=$_POST["sex"];
					$address=$_POST["address"];
					$city=$_POST["city"];
					$state=$_POST["state"];
					$sex=$_POST["sex"];
					$country=$_POST["country"];
					$pin=$_POST["pin"];
					$date=$_POST["date"];
					$email=$_POST["email"];
					$mobile=$_POST["mobile"];
					$residence=$_POST["residence"];
					$office=$_POST["office"];
					$remarks=$_POST["remarks"];
					$sql1="update patientmaster set Name='$patientname', Address='$address', Sex='$sex', City='$city', State='$state', Country='$country', Pin='$pin', DateOfBirth='$date', Email='$email', Mobile='$mobile', Residence='$residence', Office='$office', Remarks='$remarks' where PatientID='$patientid'";
					$res1=$conn->query($sql1);
						if($res1)
						{
							echo "<b>Patient Info Updated</b><br>";
						}
						else
						{
							echo "<b>Patient Info Not Updated</b><br>";
						}
				}
				
				if(!isset($_POST["search"]))
				{
				echo "Page ";
				echo floor($k/12)+1;
				echo " of ";
				echo floor($k3/12);
				}
				
				$sql="select * from patientmaster order by Name asc limit 0,12";
				if(isset($_GET["pagenumber"]))
				{
					$p=$_GET["pagenumber"];
					//$sql="SELECT * FROM big_giftshop.products order by products.category1, products.price limit $p,12";
					$sql="select * from patientmaster order by Name limit $p,12";
				
				}
				if(isset($_POST["pagenumber"]))
				{
					$p=$_POST["pagenumber"];
					if($p<=0)
					{
						$p=0;
					}
					$sql="select * from patientmaster order by Name limit $p,12";			
				}
				if(isset($_POST["search"]))
				{
					$s=$_POST["searchterm"];
					$sql="select * from patientmaster where Name like '%$s%'";
				}
				if(!isset($p))
						{
							$p=0;
							
						}
				echo "<input type='hidden' form='viewpatient' value='$p' name='pagenumber'/>";
					$res=$conn->query($sql);
					if($res->num_rows>0)
					{
						echo "<table  class='mdl-data-table mdl-js-data-table'>";
						echo "<tr><th>Patient Name</th><th>Sex</th><th>Age</th><th>Phone Number</th><th>Email Address</th><th></th></tr>";
						while($row=$res->fetch_assoc())
						{
							$pid=$row["PatientID"];
							echo "<tr>";
							echo "<td>" . $row["Name"] . "</td>";
							echo "<td>" . $row["Sex"] . "</td>";
							$from = new DateTime($row["DateOfBirth"]);
							$to   = new DateTime('today');
							echo "<td>" .  $from->diff($to)->y . "</td>";
							echo "<td>" . $row["Mobile"] . "</td>";
							echo "<td>" . $row["Email"] . "</td>";
							
							echo "<td><button type='submit' name='pid' class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect' value=$pid form='viewpatient'>View Patient</button></td></tr>";
						
						}
						echo "</table>";
						
						
				$k;
				$n=1;
				if(!isset($_POST["search"]))
				{
					echo "<div id='pagenos'><br>";
					if($k!=0)
					{
						echo "<button type='submit' name='pagenumber' value='$k1' form='page' class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--primary mybutton2'>Previous</button>";
					}
					echo "&nbsp";
					if($k!=$k3-12)
					{
						echo "<button type='submit' name='pagenumber' value='$k2' form='page' class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--primary mybutton2'>Next</button>";
					}
					echo "</div>";
					}
				}
				?>
      </main>
    </div>
      </svg>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
