set ns [new Simulator]
set tr [open wireoutex2.tr w]
puts $tr "Event Time From To PktType Size Flags SId:Port DId:port SeqNo AckNo"
$ns trace-all $tr
set nt [open wireoutex2.nam w]
$ns namtrace-all $nt
#Create Nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
#Create Links b/w Nodes
$ns duplex-link $n0 $n1 10mb 5ms DropTail
$ns duplex-link $n0 $n2 10mb 5ms DropTail
$ns duplex-link $n1 $n3 10mb 5ms DropTail
$ns duplex-link $n2 $n3 10mb 5ms DropTail
$ns duplex-link $n3 $n4 10mb 5ms DropTail
$ns duplex-link $n3 $n5 10mb 5ms DropTail
$ns duplex-link $n4 $n6 10mb 5ms DropTail
$ns duplex-link $n5 $n6 10mb 5ms DropTail
#Placements of the Nodes
$ns duplex-link-op $n0 $n1 orient right-up
$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n3 orient right-down
$ns duplex-link-op $n2 $n3 orient right-up
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n5 orient right-down
$ns duplex-link-op $n4 $n6 orient right-down
$ns duplex-link-op $n5 $n6 orient right-up
#To Create Data Traffic
# ------------------- UDP ----------------
#Transport Layer Variables
set udp0 [new Agent/UDP]
set null0 [new Agent/Null]
$ns attach-agent $n0 $udp0
$ns attach-agent $n6 $null0
$ns connect $udp0 $null0
#Application Layer Variables
set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0
$ns at 2.0 "$cbr0 start"
$ns at 10.0 "$cbr0 stop"
$udp0 set fid_ 1
$ns color 1 blue
#------------------- TCP ----------------
set tcp0 [new Agent/TCP]
set sink0 [new Agent/TCPSink]
$ns attach-agent $n2 $tcp0
$ns attach-agent $n4 $sink0
$ns connect $tcp0 $sink0
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ns at 3.0 "$ftp0 start"
$ns at 9.0 "$ftp0 stop"
$tcp0 set fid_ 3
$ns color 3 red
$ns run
