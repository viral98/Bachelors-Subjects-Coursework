#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
void b_circle(int x,int y,int p)
{
	putpixel(x+320,240-y,1);
	putpixel(320-y,240-x,9);
	putpixel(-x+320,240-y,3);
	putpixel(x+320,240+y,7);
	putpixel(-x+320,240+y,13);
	putpixel(320-y,240+x,8);
	putpixel(320+y,240-x,5);
	putpixel(320+y,240+x,11);
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
		putpixel(x+320,240-y,1);
		putpixel(320-y,240-x,9);
		putpixel(-x+320,240-y,3);
		putpixel(x+320,240+y,7);
		putpixel(-x+320,240+y,13);
		putpixel(320-y,240+x,8);
		putpixel(320+y,240-x,5);
		putpixel(320+y,240+x,11);
	}
}
void main()
{
	int xinit,yinit;
	int p,x,y;
	int gm, gd = DETECT;
	float i,r,rr,xxinit,yyinit,rh;
	float xc,yc,rx,ry,s,h;
	initgraph(&gd,&gm,"");
	printf("Enter the radius of the circle: ");
	scanf("%f", &r);
	x=0;
	y=r;
	cleardevice();
	p = 3 - (2*r);  //Uses bresenham circle
	b_circle(x,y,p);
	line(320,240,320,200);
	line(320,240,350,240);
	xinit=0;
	yinit=40;
	rr=25;
	s=0;
	rh=20;
	h=0;
	for(i=0;i<80;i++)
	{
		cleardevice();
		outtextxy(320,200,"12");
		outtextxy(360,240,"3");
		outtextxy(320,280,"6");
		outtextxy(280,240,"9");
		p=3-(2 * r);
		b_circle(x,y,p);
		//xxinit=xinit;
		//yyinit=yinit;
		s=s+0.10472;
		xinit=rr*cos(s)+rr*sin(s);//Where rr=25
		yinit=-rr*sin(s)+rr*cos(s);
		line(320,240,320+xinit,240-yinit);
		h=h+0.00174;
		xxinit=rh*cos(h)+rh*sin(h);//Where rh = 20
		yyinit=-rh*sin(h)+rh*cos(h);
		line(320,240,320+xxinit,240-yyinit);
		delay(500);
	}
	getch();
	closegraph();
}

