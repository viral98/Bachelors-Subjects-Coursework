#include<reg51.h>

void main()
{
	unsigned char z;
	while(1)
	{
	z=P1;
	z=z&0x03;
	switch(z)
	{
		case(0):
		{
			P0='0';
			break;
		}
		case(1):
		{
			P0='1';
			break;
		}
		case(2):
		{
			P0='2';
			break;
		}
		case(3):
		{
			P0='3';
			break;
		}
		
	}
	}
}