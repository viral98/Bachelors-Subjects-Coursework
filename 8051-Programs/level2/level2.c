#include<reg51.h>
sbit btn=P1^1;
void main()
{
	unsigned char count,count2;
	count2=0;
	P3=0;
	while(1)
	{
		P2=0;
		count=0;
		count2=0;
		P3=0;
	while(count2<=9)
	{
	count=0;
	P2=0;
	P2=count;
	while(count<=9)
	{
		if(btn==0)
		{
			while(btn==0);
			count++;
			P2=count;
		}
	}
	count2++;
	P3=count2;
}
}
}