#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void floodfill1(int x,int y,int oldcolor,int fcolor) {
	int p;
	p=getpixel(x,y);
	if(p==oldcolor) {
		putpixel(x,y,fcolor);
		floodfill1(x+1,y,oldcolor,fcolor);
		floodfill1(x-1,y,oldcolor,fcolor);
		floodfill1(x,y+1,oldcolor,fcolor);
		floodfill1(x,y-1,oldcolor,fcolor);

	}
}
void main() {
	int i,j,x=100,y=10,old,newc;
	int gd=DETECT,gm;
	initgraph(&gd,&gm,"");
	//To draw all the lines
	for(i=0;i<9;i++){
			line(x,10,x,90);
			line(100,y,180,y);
			x+=10;
			y+=10;
	}

	x=105;
	y=15;
	//To fill the white parts in between
	for(i=0;i<8;i++){
		if(i%2==0){
			x=105;
		}
		else{
			x=115;
		}
		for(j=0;j<8;j++){
			if(j%2==0){
				floodfill1(x,y,0,15);
			}
			x+=10;
		}//End of for with variable j
		y+=10;
	}
	getch();

}
