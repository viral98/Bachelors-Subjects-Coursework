#include<time.h>
#include<stdio.h>
#include<time.h>
int before_optimize()
{
	int x=7;
	int y=14-x/2;
	float z=0;
	while(z<1000000){
		x=x+1;
		y=y+1;
		x=x+2;
		z=z+1;
	}
	x=7;
	y=14-x/2;
	return (y*(28/x+2));
}
int after_optimize()
{
	int y=14-7/2;
	float z=0;
	while(z<100000){
		z=z+1;
	}
	return (y*(28/7+2));
}
void main()
{
	int a,b;
	clock_t start, end;
	double secs=0;
	double cpu_time_used;
	start = clock();
	a=before_optimize () ;
	printf ("Result before optimization %d\n", a);
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("Time Taken Before Optimization Is : %f\n ",cpu_time_used);
	start = clock();
	b=after_optimize();
	printf ("Result after optimization %d\n",b);
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("Time Taken After Optimization Is : %f\n ",cpu_time_used);
}
/*DO NOT TAKE INPUT FROM THE USER IT DISTURBS THE TIMER--AQID KHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ gcc ConstantPropagation.c -o ./hello
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ ./hello
Result before optimization 66
Time Taken Before Optimization Is : 0.010299
 Result after optimization 66
Time Taken After Optimization Is : 0.000518
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ 
*/
