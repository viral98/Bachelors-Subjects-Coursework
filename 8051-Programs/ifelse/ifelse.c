#include<reg51.h>

sbit mybit=P1^5;

void main()
{
	mybit=1;
	while(1)
	{
		if(mybit==1)
			P0=0x55;
		else
			P0=0xAA;
	}
}