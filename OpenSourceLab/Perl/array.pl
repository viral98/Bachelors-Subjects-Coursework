@array = (10,20,30);
print "@array";
print "Enter value to push: ";
$val = <STDIN>;	
push(@array, $val);
print "@array";
print "\n";
print "Poping\n";  
pop(@array);
print "@array";
print "\n";
print "Shifting\n";
shift(@array);
print "@array";		   
print "\n";
print "Enter value to unshift: ";
$val = <STDIN>;	
unshift(@array, $val);
print "@array";
print "\n";