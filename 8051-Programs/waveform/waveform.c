#include<reg51.h>
sbit pin=P1^0;
void main()
{
	pin=0;
	TMOD=0x01;
	
	while(1)
	{
		TH0=0xFC;
		TL0=0x67;
		TR0=1;
		while(TF0==0);
		pin=~pin;
		TR0=0;
		TF0=0;
	}
}