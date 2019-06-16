#include<stdio.h>
#include<stdlib.h>
#include <unistd.h>
void main(){
	int i,packets[10],content=0,newcontent,time,clk,bcktsize,output_rate;  

	for(i=0;i<5;i++){
		packets[i]=rand()%10;
		if(packets[i]==0) --i;
	}

	printf("\n Enter output rate of the bucket: \n");
	scanf("%d",&output_rate);

	printf("\n Enter Bucketsize\n");
	scanf("%d",&bcktsize);

	for(i=0;i<5;i++){
		
	   printf("Incoming Size is %d\n",packets[i]);
	   currentSpaceInBucket = bcktsize - content;
	   if(packets[i]<=currentSpaceInBucket){
               content+=packets[i];
               printf("Buffer size is %d out of %d\n",content,bcktsize);

	   }
       else{
              printf("Packet loss : %d\n",packets[i]-currentSpaceInBucket);
              content=bcktsize;
              printf("Buffer size is %d out of %d\n",content,bcktsize);
        }
           
      if(content>output_rate){
             content-=output_rate;
       }
	   else{
             content=0;
       }

       printf("After transmission : ");
       printf("Buffer size is %d out of %d\n",content,bcktsize);
       printf("\n");
	   time=rand()%10;
	   printf("\n Next packet will come at %d\n",time);
	   for(clk=0;clk<time;++clk){
		printf("%d\n",(time-clk));
	    sleep(1);
       }


	}	
}