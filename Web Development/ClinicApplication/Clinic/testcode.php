
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
$result = $conn->query("SELECT PatientID,PatientName FROM appointment");
$header = $conn->query("SELECT UCASE(`COLUMN_NAME`) 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='clinic' 
AND `TABLE_NAME`='appointment'
and `COLUMN_NAME` in ('name','author')");
require('../Clinic/fpdf.php');

$pdf = new FPDF();
$pdf->AddPage();
$pdf->SetFont('Arial','B',16);
foreach($header as $heading) {
	foreach($heading as $column_heading)
		$pdf->Cell(95,12,$column_heading,1);
}
foreach($result as $row) {
	$pdf->Ln();
	foreach($row as $column)
		$pdf->Cell(95,12,$column,1);
}
$pdf->Output();
?>
