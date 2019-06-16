#include<reg51.h>
void main()
{
	unsigned int i,j;
	
	while(1)
	{
		
		P0=~P0;
		P1=~P1;
		for(i=0;i<10;i++)
	  {
			for(j=0;j<1275;j++);
    }
	}
}