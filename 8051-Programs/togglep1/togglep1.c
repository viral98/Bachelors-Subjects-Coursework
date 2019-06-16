#include<reg51.h>

void msdelay(unsigned int);

void main()
{
	while(1)
	{
		P1=0x55;
		msdelay(250);
		P1=0xAA;
		msdelay(250);
	}	
}

void msdelay(unsigned int itime)
{
	unsigned int i,j;
	for(i=0;i<=itime;i++)
	{
		for(j=0;j<1275;j++);
	}		
}