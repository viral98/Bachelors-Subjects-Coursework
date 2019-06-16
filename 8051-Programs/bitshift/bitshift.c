#include<reg51.h>

void msdelay(unsigned int);

void main()
{
	unsigned char z;
	z=01;
	while(1)
	{
	P1=z;
	z=z<<1;
	msdelay(10000);
	}
}

void msdelay(unsigned int itime)
{
	int i,j;
	for(i=0;i<itime;i++)
	{
		for(j=0;j<1275;j++);
	}
}