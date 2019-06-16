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

      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
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
                $tdate=$_GET["date"];
               // echo "pressed.";
              }
              else {
                
                $tdate = date('y-m-d');
             }
			
	  
	  ?>
    <div class="demo-layout mdl-layout mdl-js-layout mdl-layout--fixed-drawer mdl-layout--fixed-header">
      <header class="demo-header mdl-layout__header mdl-color--grey-100 mdl-color-text--grey-600">
        <div class="mdl-layout__header-row">
          <span class="mdl-layout-title">Appointments <?php
		 echo "for: <b>" . $tdate . "</b><br>";
		 ?></span>
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
        <form name = "date_select" method="GET" action="ScheduleAppointment.php">
         <div class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
		  Enter Date:
            <input class="mdl-textfield__input" type="date" id="date" name="date">        
        </div>
       
           <button type="submit" class="mdl-chip" name="search" id="search">
                <span class="mdl-chip__text">Submit</span>
              </button>
        
        
                  
		  
              <a href="NewAddAppointment.php"><button type="button" class="mdl-chip" name="Add" id="Add">
                <span class="mdl-chip__text">Add Appointment For New Patient</span></a>
              </button>
		  
              <a href="OldAddAppointment.php"><button type="button" class="mdl-chip" name="Add" id="Add">
                <span class="mdl-chip__text">Add Appointment For Existing Patient</span></a>
              </button>
          </form>
        <div>
          <?php
             
              $sql="SELECT * from appointment where Date = '$tdate'";
                $result = $conn->query($sql);
				//show patient remarks, referring doctor and phone no.
                if($result->num_rows>0)
				{
					$eight=array();
					$nine=array();
					$ten=array();
					$eleven=array();
					$twelve=array();
					$thirteen=array();
					$fourteen=array();
					$fifteen=array();
					$sixteen=array();
					$seventeen=array();
					$eighteen=array();
					$nineteen=array();
					$twenty=array();
					$twentyone=array();
					$twentytwo=array();
					while($row=$result->fetch_assoc())
					{
						$TTime = $row["Time"];
                            if (strtotime($TTime) >= strtotime('08:00') && strtotime($TTime) < strtotime('09:00'))
							{
								
								array_push($eight,$row);
							}
							if (strtotime($TTime) >= strtotime('09:00') && strtotime($TTime) < strtotime('10:00'))
							{
								
								array_push($nine,$row);
							}
							if (strtotime($TTime) >= strtotime('10:00') && strtotime($TTime) < strtotime('11:00'))
							{
								
								array_push($ten,$row);
							}
							if (strtotime($TTime) >= strtotime('11:00') && strtotime($TTime) < strtotime('12:00'))
							{
								
								array_push($eleven,$row);
							}
							if (strtotime($TTime) >= strtotime('12:00') && strtotime($TTime) < strtotime('13:00'))
							{
								
								array_push($twelve,$row);
							}
							if (strtotime($TTime) >= strtotime('13:00') && strtotime($TTime) < strtotime('14:00'))
							{
								
								array_push($thirteen,$row);
							}
							if (strtotime($TTime) >= strtotime('14:00') && strtotime($TTime) < strtotime('15:00'))
							{
								
								array_push($fourteen,$row);
							}
							if (strtotime($TTime) >= strtotime('15:00') && strtotime($TTime) < strtotime('16:00'))
							{
								
								array_push($fifteen,$row);
							}
							if (strtotime($TTime) >= strtotime('16:00') && strtotime($TTime) < strtotime('17:00'))
							{
								
								array_push($sixteen,$row);
							}
							if (strtotime($TTime) >= strtotime('17:00') && strtotime($TTime) < strtotime('18:00'))
							{
								
								array_push($seventeen,$row);
							}
							if (strtotime($TTime) >= strtotime('18:00') && strtotime($TTime) < strtotime('19:00'))
							{
								
								array_push($eighteen,$row);
							}
							if (strtotime($TTime) >= strtotime('19:00') && strtotime($TTime) < strtotime('20:00'))
							{
								
								array_push($nineteen,$row);
							}
							if (strtotime($TTime) >= strtotime('20:00') && strtotime($TTime) < strtotime('21:00'))
							{
								
								array_push($twenty,$row);
							}
							if (strtotime($TTime) >= strtotime('21:00') && strtotime($TTime) < strtotime('22:00'))
							{
								
								array_push($twentyone,$row);
							}
							if (strtotime($TTime) >= strtotime('22:00') && strtotime($TTime) < strtotime('23:00'))
							{
								
								array_push($twentytwo,$row);
							}
					}
					
				}
					$eightcount=count($eight);
					$ninecount=count($nine);
					$tencount=count($ten);
					$elevencount=count($eleven);
					$twelvecount=count($twelve);
					$thirteencount=count($thirteen);
					$fourteencount=count($fourteen);
					$fifteencount=count($fifteen);
					$sixteencount=count($sixteen);
					$seventeencount=count($seventeen);
					$eighteencount=count($eighteen);
					$nineteencount=count($nineteen);
					$twentycount=count($twenty);
					$twentyonecount=count($twentyone);
					$twentytwocount=count($twentytwo);
					$Max = max($eightcount,$ninecount,$tencount,$elevencount,$twelvecount,$thirteencount,$fourteencount,$fifteencount,$sixteencount,$seventeencount,$eighteencount,$nineteencount,$twentycount,$twentyonecount,$twentytwocount)

                ?>
			 </div> 
			 <form id="senddateexisting" method="get" action="OldAddAppointment.php"></form>
				<br><form name='ViewAppointments' method='_GET' action='ViewAppointment.php'><table class='mdl-data-table mdl-js-data-table'>
					<!--<tr>><td></td><td></td><td></td><td></td><td></td><td></td>
					<td></td><td></td><td></td><td></td><td></td><td></td><td></td>
					<td></td></tr>
                    <tr>--> <?php
                            echo('<tr>');
                            echo('<td>08:00AM-09:00AM<br> <a href="NewAddAppointment.php?newtime=08:00">New</a> <a href="OldAddAppointment.php?newtime=08:00">Existing</a></td>');
                            for($i=0;$i<count($eight);$i++) {


                                echo('<td> <a href="ViewAppointment.php?ViewAppt='.$eight[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$eight[$i]['Time'].'">' .$eight[$i]['PatientName'] . ' (' . $eight[$i]['Time'] . ')' . '</a></td>');
                            }
                    echo('<tr>');
                    echo('<td>09:00AM-10:00AM<br> <a href="NewAddAppointment.php?newtime=09:00">New</a> <a href="OldAddAppointment.php?newtime=09:00">Existing</a></td>');
                    for($i=0;$i<count($nine);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$nine[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$nine[$i]['Time'].'">' .$nine[$i]['PatientName']  . ' (' . $nine[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>10:00AM-11:00AM<br> <a href="NewAddAppointment.php?newtime=10:00">New</a> <a href="OldAddAppointment.php?newtime=10:00">Existing</a></td>');
                    for($i=0;$i<count($ten);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$ten[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$ten[$i]['Time'].'">' .$ten[$i]['PatientName']  . ' (' . $ten[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>11:00AM-12:00PM<br> <a href="NewAddAppointment.php?newtime=11:00">New</a> <a href="OldAddAppointment.php?newtime=11:00">Existing</a></td>');
                    for($i=0;$i<count($eleven);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$eleven[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$eleven[$i]['Time'].'">' .$eleven[$i]['PatientName'] . ' (' . $eleven[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>12:00PM-01:00PM<br> <a href="NewAddAppointment.php?newtime=12:00">New</a> <a href="OldAddAppointment.php?newtime=12:00">Existing</a></td>');
                    for($i=0;$i<count($twelve);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$twelve[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$twelve[$i]['Time'].'">' .$twelve[$i]['PatientName'] . ' (' . $twelve[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>01:00PM-02:00PM<br> <a href="NewAddAppointment.php?newtime=13:00">New</a> <a href="OldAddAppointment.php?newtime=13:00">Existing</a></td>');
                    for($i=0;$i<count($thirteen);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$thirteen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$thirteen[$i]['Time'].'">' .$thirteen[$i]['PatientName'] . ' (' . $thirteen[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>02:00PM-03:00PM<br> <a href="NewAddAppointment.php?newtime=14:00">New</a> <a href="OldAddAppointment.php?newtime=14:00">Existing</a></td>');
                    for($i=0;$i<count($fourteen);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$fourteen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$fourteen[$i]['Time'].'">' .$fourteen[$i]['PatientName'] . ' (' . $fourteen[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>03:00PM-04:00PM<br> <a href="NewAddAppointment.php?newtime=15:00">New</a> <a href="OldAddAppointment.php?newtime=15:00">Existing</a></td>');
                    for($i=0;$i<count($fifteen);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$fifteen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$fifteen[$i]['Time'].'">' .$fifteen[$i]['PatientName'] . ' (' . $fifteen[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>04:00PM-05:00PM<br> <a href="NewAddAppointment.php?newtime=16:00">New</a> <a href="OldAddAppointment.php?newtime=16:00">Existing</a></td>');
                    for($i=0;$i<count($sixteen);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$sixteen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$sixteen[$i]['Time'].'">' .$sixteen[$i]['PatientName'] . ' (' . $sixteen[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>05:00PM-06:00PM<br> <a href="NewAddAppointment.php?newtime=17:00">New</a> <a href="OldAddAppointment.php?newtime=17:00">Existing</a></td>');
                    for($i=0;$i<count($seventeen);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$seventeen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$seventeen[$i]['Time'].'">' .$seventeen[$i]['PatientName'] . ' (' . $seventeen[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>06:00PM-07:00PM<br> <a href="NewAddAppointment.php?newtime=18:00">New</a> <a href="OldAddAppointment.php?newtime=18:00">Existing</a></td>');
                    for($i=0;$i<count($eighteen);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$eighteen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$eighteen[$i]['Time'].'">' .$eighteen[$i]['PatientName'] . ' (' . $eighteen[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>07:00PM-08:00PM<br> <a href="NewAddAppointment.php?newtime=19:00">New</a> <a href="OldAddAppointment.php?newtime=19:00">Existing</a></td>');
                    for($i=0;$i<count($nineteen);$i++) {

                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$nineteen[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$nineteen[$i]['Time'].'">' .$nineteen[$i]['PatientName'] . ' (' . $nineteen[$i]['Time'] . ')' . '</a></td>');

                    }
                    echo('<tr>');
                    echo('<td>08:00PM-09:00PM<br> <a href="NewAddAppointment.php?newtime=20:00">New</a> <a href="OldAddAppointment.php?newtime=20:00">Existing</a></td>');
                    for($i=0;$i<count($twenty);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$twenty[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$twenty[$i]['Time'].'">' .$twenty[$i]['PatientName'] . ' (' . $twenty[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>09:00PM-10:00PM<br> <a href="NewAddAppointment.php?newtime=21:00">New</a> <a href="OldAddAppointment.php?newtime=21:00">Existing</a></td>');
                    for($i=0;$i<count($twentyone);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$twentyone[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$twentyone[$i]['Time'].'">' .$twentyone[$i]['PatientName'] . ' (' . $twentyone[$i]['Time'] . ')' . '</a></td>');
                    }
                    echo('<tr>');
                    echo('<td>10:00PM-11:00PM<br> <a href="NewAddAppointment.php?newtime=22:00">New</a> <a href="OldAddAppointment.php?newtime=22:00">Existing</a></td>');
                    for($i=0;$i<count($twentytwo);$i++) {


                        echo('<td> <a href="ViewAppointment.php?ViewAppt='.$twentytwo[$i]['AppointmentID'].'" data-toggle="tooltip" title="'.$twentytwo[$i]['Time'].'">' .$twentytwo[$i]['PatientName'] . ' (' . $twentytwo[$i]['Time'] . ')' . '</a></td>');
                    }
                        ?>

				</form></table>
			<div>
                <script>
                    $(document).ready(function(){
                        $('[data-toggle="tooltip"]').tooltip();
                    });
                </script>

            
        

        </div>
      </main>
    </div>
    <script src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  </body>
</html>
