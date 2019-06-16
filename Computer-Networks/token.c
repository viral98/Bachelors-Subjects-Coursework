#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void main(){

    int i, packets[10],bcktsize,time,clk;
    int tokens=0;

    printf("\n Enter Bucketsize\n");
    scanf("%d",&bcktsize);

    for(i=0;i<5;i++){
      packets[i]=rand()%10;
      if(packets[i]==0) --i;
   }

   tokens=rand()%10;
   sleep(1);
   for(i=0;i<5;i++){
       
       if(tokens<bcktsize){
         tokens++;
         printf("Tokens before transmission:%d\n",tokens);
       }
       else{ 
         printf("Tokens overflow:: ");
         printf("Tokens before transmission:%d\n",tokens);
       }
       

       

       if(packets[i]<=tokens){
        printf("Packet %d of size %d transmitted\n",i,packets[i]);
        tokens-=packets[i];
        printf("Remaining Tokens: %d\n",tokens);
        time=rand()%10;
        printf("\n Next packet will come at %d\n",time);
          for(clk=0;clk<time;++clk){
            printf("%d\n",(time-clk));
            sleep(1);
          }


        }
        else{
          printf("Enough tokens not available, Packet has to wait\n");
          --i;
          sleep(1);
        }
   }//End of FOR
}//End of Main