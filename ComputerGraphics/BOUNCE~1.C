#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <dos.h>

int main() {
 int gd = DETECT, gm;
 int i, x, y, flag=0;
 initgraph(&gd, &gm, "C:\\TC\\BGI");

 /* get mid positions in x and y-axis */
 x = 320/2;
 y = 30;


 while (!kbhit()) {
  if(y >= 240-30 || y <= 30)
     flag = !flag;
     /* draws the gray board */
     setcolor(RED);
     setfillstyle(SOLID_FILL, RED);
     circle(x, y, 30);
     floodfill(x, y, RED);

 /* delay for 50 milli seconds */
 delay(20);

 /* clears screen */
 cleardevice();
 if(flag){
     y = y + 1;
     x = x + 2;
 } else {
     y = y - 5;
     x = x -2;
 }
}

    getch();
    closegraph();
    return 0;

}