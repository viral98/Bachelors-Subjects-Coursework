#include<reg51.h>
sbit s=P0^0;

void main()
{
	unsigned char x,i,j,k;
	x=0x01;
	P2=0x00;
	while(1)
	{
		while(s==1)
		{
			P2=x;
			x=x<<1;
			for(i=0;i<255;i++)
			{
				for(j=0;j<255;j++)
				{
					for(k=0;k<255;k++);
				}
			}
			if(P2>0x80)
			{
				P2=01;
			}
		}	
	}
}