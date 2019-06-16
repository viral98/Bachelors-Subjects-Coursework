#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#include<dos.h>
void plot(int x, int y){
	putpixel(320+x,240+y,YELLOW);
	putpixel(320+x,240-y,YELLOW);
	putpixel(320-x,240+y,YELLOW);
	putpixel(320-x,240-y,YELLOW);
}
void midpoint(int a, int b){
	long int p1,p2,x,y,b2,a2;
	line(0,240,640,240);//X axis
	line(320,0,320,480);//Y axis
	p1 = (b*b) - (a*a)*b + (a*a)/4;
	x = 0;
	y = b;
	b2=b*b ;
	a2=a*a;
	while((2*(b2)*x) < (2*(a2)*y)){
		if(p1<0){
			x++;
			p1 = p1 + 2*(b2)*x + (b2);
		}
		else{
			p1 = p1 + 2*(b2)*x - 2*(a2)*y + (b2);
			x++;
			y--;
		}
		plot(x,y);

	}
	p2 = b2*(x+0.5)*(x+0.5) + a2*(y-1)*(y-1) - a2*b2;
	while(y>0){
		if(p2>0){
		   y--;
		   p2 = p2 - 2*a2*y + a2;
		}
		else{
			x++;
			y--;
			p2 = p2 + 2*b2*x - 2*a2*y + a2;
		}
		plot(x,y);
	}
}
void main(){
	int j,k,num,x,y;

	int gd=DETECT,gm;
	initgraph(&gd,&gm,"");
	printf("Enter the two radii\n");
	scanf("%d%d",&x,&y);
	midpoint(x,y);
	getch();
	closegraph();
}
