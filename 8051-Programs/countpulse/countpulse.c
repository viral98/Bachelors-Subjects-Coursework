#include<reg51.h>

void main()
{
	P2=0;
	P1=0;
	TMOD=0x05;
	TR0=1;
	while(1)
	{
		P1=TL0;
		P2=TH0;
		if(TF0==1)
		{
			TF0=0;
		}
	}
}