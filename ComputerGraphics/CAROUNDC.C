#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#include<dos.h>
void b_circle(float xS, float yS, int r){
	float p,x=0,y=r;
	putpixel((int)x+xS,(int)yS+y,1);
	putpixel((int)xS+x,(int)yS-y,9);
	putpixel((int)-x+xS,(int)yS+y,3);
	putpixel((int)-x+xS,(int)yS-y,7);
	putpixel((int)y+xS,(int)yS+x,13);
	putpixel((int)xS+y,(int)yS-x,8);
	putpixel((int)xS-y,(int)yS+x,5);
	putpixel((int)xS-y,(int)yS-x,11);
	p = 3 - 2*r;
	while(x<=y)
	{
		if(p<=0)
		{
			x=x+1;
			y=y;
			p=p+(4*x)+2;
		}
		else
		{
			x=x+1;
			y=y-1;
			p=p+(4*x)-(4*y)+2;
		}
		putpixel((int)x+xS,(int)yS+y,1);
		putpixel((int)xS+x,(int)yS-y,9);
		putpixel((int)-x+xS,(int)yS+y,3);
		putpixel((int)-x+xS,(int)yS-y,7);
		putpixel((int)y+xS,(int)yS+x,13);
		putpixel((int)xS+y,(int)yS-x,8);
		putpixel((int)xS-y,(int)yS+x,5);
		putpixel((int)xS-y,(int)yS-x,11);
	}
}
void main()
{       int i,gd=DETECT,gm,angle;
	float theta;
	initgraph(&gd,&gm," ");


	angle=0;

	for(angle=0;angle<=360;angle++)
	{       b_circle(320,240,100);
		theta=angle*((3.14)/180);
		b_circle(320+100*cos(theta),240+100*sin(theta),20);
//	       #	floodfill(320+100*cos(theta),240+50*sin(theta),BLUE);
		delay(40);
		cleardevice();
	}
	getch();
	closegraph();

}