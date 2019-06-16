#include<stdio.h>
#include<math.h>
#include<conio.h>
#include<graphics.h>
void bez();
float fact(int);
void main()
{

  int gd =DETECT,gm;
  initgraph(&gd,&gm,"");

  line(300,200,300,250);
  line(300,200,350,225);
  line(300,250,350,225);
  bez();

  getch();
  closegraph();
}
void bez()
{
 int  n=4,r;
 float u,c ,x[5],y[5],xn,yn;

 x[0]=350;y[0]=225;
 x[1]=400;y[1]=125;
 x[2]=475;y[2]=225;
 x[3]=400;y[3]=325;
 x[4]=350;y[4]=225;

 for(u=0;u<1;u=u+0.001)
 {
  xn=0;
  yn=0;
  for(r=0;r<=n;r++)
  {
   c=fact(n)/(fact(n-r)*fact(r));
   xn=xn + c*pow(1-u,n-r)*pow(u,r)*x[r];
   yn=yn + c*pow(1-u,n-r)*pow(u,r)*y[r];
  }
  putpixel(xn,yn,WHITE);
 }

}


float fact(int n)
{
 int i,f=1;
 for(i=1;i<=n;i++)
 {
   f=f*i;
 }
 return f;
}

