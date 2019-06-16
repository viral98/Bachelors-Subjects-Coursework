%hash = ('Umair',100,'Varun',200,'Bhavuk',300);
print "Key Value Pair os hash is\n";

foreach $x (keys(%hash)){
	print"$x:$hash{$x} "
}
print "\n";


@keys = keys%hash;
$size=@keys;
print $size;
print "\n";
print @keys;


print"\nDeleitng Bhavuk\n";
delete $hash{'Bhavuk'};
foreach $x (keys(%hash)){
	print"$x:$hash{$x} "
}
print "\n";



print"\nAdding Sidd\n";
$hash{'Sidd'} = 900;
foreach $x (keys(%hash)){
	print"$x:$hash{$x} "
}
print "\n";