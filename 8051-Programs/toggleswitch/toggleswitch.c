#include<reg51.h>

void msdelay(unsigned int);
sbit p1pin1=P1^1;
sbit p2pin7=P2^7;
void main()
{
	unsigned int i,j;
 while(1)
 {
	  while(1)
		{
		if(p1pin1==0)
		{
			for(j=0;j<1000;j++);
			 if(p1pin1==0)
			 {
				//		p1pin1=1;
				break;
			 }
		}
		}
		 while(1)
		 {
			p2pin7 =~p2pin7;
			for(i=0;i<10000;i++);
			if(p1pin1==0)
			{
				for(j=0;j<1000;j++);
			 if(p1pin1==0)
			 {
				//		p1pin1=1;
				goto delay;
			 }
			}
		 }
		 delay:
		 for(j=0;j<8000;j++);
	}
}
