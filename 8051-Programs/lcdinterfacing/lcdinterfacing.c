#include<reg51.h>
#define LCD P2
sbit rs = P1^0;
sbit rw = P1^1;
sbit e = P1^2;
unsigned char value;
unsigned char *display;

void msdelay(unsigned int time)
{
	unsigned int i,j;
	for(i=0;i<time;i++)
	{
		for(j=0;j<1275;j++);
	}
}
void lcdcmd(unsigned char value)
{
		LCD = value;
		rs = 0;
		rw = 0;
		e = 1;
		msdelay(1);
		e=0;
}

void lcddata(unsigned char value)
{
		LCD = value;
		rs = 1;
		rw = 0;
		e = 1;
		msdelay(10);
		e=0;
}

void lcddataa(unsigned char *display)
{
	unsigned int x;
	for(x=0;display[x]!=0;x++)
	{
		lcddata(display[x]);
		msdelay(10);
	}
	
}


void main()
{
	
	lcdcmd(0x38);
	msdelay(10);
	lcdcmd(0x0F);
	msdelay(10);	
	lcdcmd(0x80);
	msdelay(10);	
	/*lcddata('M');
	msdelay(10);
	lcddata('I');
	msdelay(10);
	lcddata('L');
	msdelay(10);
	lcddata('I');
	msdelay(10);
	lcddata('N');
	msdelay(10);
	lcddata('D');
	msdelay(10);
	
	lcddata('S');
	msdelay(10);
	lcddata('H');
	msdelay(10);
	lcddata('A');
	msdelay(10);
	lcddata('H');
	msdelay(10);
	*/
	lcddataa("MILIND");
	msdelay(10);
	lcdcmd(0xC0);
	msdelay(10);
	lcddataa("SHAH");
	msdelay(10);
	lcdcmd(0x06);
	msdelay(10);
	lcdcmd(0x0C);
	msdelay(10);

	
}