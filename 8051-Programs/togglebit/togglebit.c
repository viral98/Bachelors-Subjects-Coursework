#include<reg51.h>

void msdelay(unsigned int);
	sbit mybit = P1^1;
void main()
{

	mybit=0;
	for(;;)
	{ 
		msdelay(10000);
		mybit=~mybit;
		msdelay(10000);
	}		
}

void msdelay(unsigned int itime)
{
	unsigned int i,j;
	for(i=0;i<itime;i++)
	{
		for(j=0;j<1275;j++);
	}	
}