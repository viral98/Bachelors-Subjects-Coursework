BEGIN{
 tcp = 0;
 cbr = 0;
 ack = 0;
}
{
 if ($5 == "tcp")
 tcp++;
 if ($5 == "cbr")
 cbr++;
 if ($5 == "ack")
 ack++;
}
END{
 printf("TCP pkts = %d ",tcp);
 printf("\n");
 printf("CBR pkts = %d ",cbr);
 printf("\n");
 printf("ACK pkts = %d ",ack);
 }
