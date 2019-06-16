#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#include<dos.h>

void main()
{       int i,gd=DETECT,gm,angle;
	float theta;
	initgraph(&gd,&gm," ");


	angle=0;

	for(angle=0;angle<=360;angle++)
	{       ellipse(320,240,0,360,100,50);
		theta=angle*((3.14)/180);
		circle(320+100*cos(theta),240+50*sin(theta),20);
	       //	floodfill(320+100*cos(theta),240+50*sin(theta),BLUE);
		delay(40);
		cleardevice();
	}
	getch();
	closegraph();

}