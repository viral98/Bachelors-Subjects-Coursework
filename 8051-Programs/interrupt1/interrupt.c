#include<reg51.h>
sbit p=P2^2;
sbit s=P2^1;
sbit l=P2^7;
unsigned char x=0;
void timer0() interrupt 1
{
	p=~p;
}

void timer1() interrupt 0
{
	unsigned int y;
	x++;
	P1=x;
	
	for(y=0;y<1000;y++);
}

void main()
{
	p=0;
	P1=0;
	TMOD=0x02;
	TH0=0xA4;
	IE=0x83;
	s=0;
	l=1;
	TR0=1;
	while(1)
	{
		if(s==1)
		{
			l=1;
		
		}
		else
		{
			l=0;
		}
			
	}
}
	