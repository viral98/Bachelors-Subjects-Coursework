#!/usr/bin/perl

use DBI;
use strict;

my $driver = "SQLite";
my $database =  "test.db";
my $dsn = "DBI:$driver:database=$database";
my $dbh = DBI->connect($dsn,'','');
my $sth = $dbh->prepare("CREATE TABLE IF NOT EXISTS student (id integer, name text, address text)");
$sth->execute();

my $sth2 = $dbh->prepare("INSERT INTO student VALUES(1,'Viral','Mumbai')");;
$sth2->execute();
my $sth2 = $dbh->prepare("INSERT INTO student VALUES(1,'Maithili','Mumbai')");;
$sth2->execute();
my $sth2 = $dbh->prepare("INSERT INTO student VALUES(1,'Milind','Parle')");;
$sth2->execute();
my $sth2 = $dbh->prepare("INSERT INTO student VALUES(1,'PratikT','Kalyan')");;
$sth2->execute();

my $sth3 = $dbh->prepare("SELECT * FROM student");
$sth3->execute();

while(my @row = $sth3->fetchrow_array()){
  my($id,$name,$address) = @row;
  print"ID = $id NAME = $name ADDRESS = $address \n"
}

$sth3->finish();
