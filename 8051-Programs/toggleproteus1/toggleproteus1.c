#include<reg51.h>
sbit p2pin1 = P2^1;
sbit p1pin1  = P1^1;

void main()
{
	unsigned char i;
	p1pin1=0;
	p2pin1=1;
	while(1)
	{
	 while(p2pin1==0)
	 {
		p1pin1=~p1pin1; 
		for(i=0;i<255;i++);
	 }	
	}
}