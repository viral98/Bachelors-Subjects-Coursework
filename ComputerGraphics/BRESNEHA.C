#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>

void bres(int x1, int y1, int x2, int y2){
	int step, dx,dy,i,p,xk,yk,pk,v1=10,v2=3;
	float x,y,xincr,yincr;
	line(0,240,640,240);//X axis
	line(320,0,320,480);//Y axis
	dx=(x2-x1);
	dy=(y2-y1);
	if(abs(dx)>abs(dy)){
		step=abs(dx);
	}
	else{
		step=abs(dy);
	}
	pk = 2*abs(dy)-abs(dx);
	xk=x1;
	yk=y1;
	putpixel(320+xk,240-yk,15);
	i=1;
	if(abs(dx)>abs(dy)){
		while(i<=step){
			    if(pk<0){
				xk = xk + (dx/abs(dx));
				yk = yk;
				pk = pk + 2*abs(dy);
			    }
			    else{
				xk = xk + (dx/abs(dx));
				yk = yk + (dy/abs(dy));
				pk = pk + 2*abs(dy) - 2*abs(dx);
			    }
			    i++;
			    if(v1>5){
				 putpixel(320+xk,240-yk,15);
			    }
			    else{
				if(v1<4&&v1>2&&v2>0)
				  putpixel(320+xk,240-yk,YELLOW);
				v2--;
			    }
			    v1--;
			    if(v1==0){
				v1=10;
				v2=3;
			    }


		}
	}
	else{
		pk=2*abs(dx)-abs(dy);
		while(i<=step){
			    if(pk<0){
				xk = xk;
				yk = yk+ (dy/abs(dy));
				pk = pk + 2*abs(dx);
			    }
			    else{
				xk = xk + (dx/abs(dx));
				yk = yk + (dy/abs(dy));
				pk = pk + 2*abs(dx) - 2*abs(dy);
			    }
			    i++;
			    if(v1>5){
				 putpixel(320+xk,240-yk,15);
			    }
			    else{
				if(v1<4&&v1>2&&v2>0)
				  putpixel(320+xk,240-yk,YELLOW);
				v2--;
			    }
			    v1--;
			    if(v1==0){
				v1=10;
				v2=3;
			    }
		}
	}
}
void main(){
	int j,k,num,x1,y1,x2,y2,y3,y4,x3,x4;
	int gd=DETECT,gm;
	initgraph(&gd,&gm,"");
	printf("Enter co-ordinates\n");
	scanf("%d%d%d%d",&x1,&y1,&x4,&y4);
	bres(x1,y1,x4,y4);
	getch();
	closegraph();
}



