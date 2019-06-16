#include<time.h>
#include<stdio.h>
#include<time.h>
void before_optimize()
{
	float r=10.0,pi=3.14,t;
	printf ("The Circumference of circle is : %f\n", (2.0*pi*r));
	printf("The Area of circle is: %f\n", (pi*r*r));
}
void after_optimize()
{
	float r=10.0,pi=3.14,t;
	t=pi*r;//Common subexpression
	printf("The Circumference of circle is: %f\n", (2.0*3.14*r));
	printf("The Area of circle is: %f\n", (3.14*r*r));
}
void main()
{
	clock_t start, end,start1,end1;
	double cpu_time_used;
	start = clock();
	before_optimize();
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("Time Taken Before Optimization Is : %f\n ",cpu_time_used);
	start=clock();
	after_optimize();
	end=clock();
	cpu_time_used = ((double) (end-start)) / CLOCKS_PER_SEC;
	printf("Time Taken After Optimization Is : %f\n ",cpu_time_used);
}
/*DO NOT TAKE INPUT FROM THE USER IT DISTURBS THE TIMER--AQID KHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ gcc CommonSubExpression.c -o ./hello
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ ./hello
The Circumference of circle is : 62.800002
The Area of circle is: 314.000000
Time Taken Before Optimization Is : 0.000194
 The Circumference of circle is: 62.800000
The Area of circle is: 314.000000
Time Taken After Optimization Is : 0.000014
 aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ 
*/
