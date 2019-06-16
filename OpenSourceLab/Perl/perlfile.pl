#!/usr/bin/perl
$filename = 'myfile.txt';
open (fh , '<' , $filename)
	or die "Could not open file";
while ( $row = <fh>){
	chomp $row;
	print "$row\n";
}
seek fh,0,0;	
while (<fh>){
	print "$_";

}	
seek fh,0,0;
open(fh2,">mycopy.txt");
while (<fh>){
	print fh2 $_;
}
rename ("myfile.txt","file.txt");
close(fh);
close(fh2);
unlink ("myfile.txt");