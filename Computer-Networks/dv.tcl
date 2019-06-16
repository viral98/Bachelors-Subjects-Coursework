set ns [new Simulator]

$ns color 0 Blue
$ns color 1 Red

set tr [open out.tr w]
puts $tr "Event Time from to pktype size flags SID:PORT DID:PORT ACKNO"
$ns trace-all $tr

set namtr [open out.nam w]
$ns namtrace-all $namtr

proc finish {} {
  global ns nf tr
  $ns flush-trace
  #close $nf
  close $tr
  exec nam out.nam &
  exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$ns rtproto DV

$ns duplex-link $n0 $n1 10Mb 5ms DropTail
$ns duplex-link $n0 $n2 10Mb 5ms DropTail
$ns duplex-link $n0 $n3 10Mb 5ms DropTail

$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n0 $n2 orient left-up
$ns duplex-link-op $n0 $n3 orient left-down

set udp0 [new Agent/UDP]
$ns attach-agent $n3 $udp0

set null0 [new Agent/Null]
$ns attach-agent $n1 $null0

set udp1 [new Agent/UDP]
$ns attach-agent $n2 $udp1

set null1 [new Agent/UDP]
$ns attach-agent $n3 $null1

$ns connect $udp0 $null0
$ns connect $udp1 $null1

$udp0 set fid_ 0
$udp1 set fid_ 1

set cbr0 [new Application/Traffic/CBR]
set cbr1 [new Application/Traffic/CBR]

$cbr0 attach-agent $udp0
$cbr1 attach-agent $udp1

$ns at 1.0 "$cbr0 start"
$ns at 1.5 "$cbr1 start"

$ns at 4.5 "$cbr0 stop"
$ns at 5.0 "$cbr1 stop"

$ns at 5.1 "finish"

$ns run
