#include <stdio.h>
#include <time.h>
void before_movement(int b,int c)
{
    int i,a,z;
    printf("\nBefore Code movement Optimization\n");
    clock_t start, end;
    double cpu_time_used;
    start = clock();
    i = 0;
    while(i<10)
    {
		a = b*c;
		z = a*2;
		i++;
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	printf("Result: %d",z);
    printf("\nTime taken = %f",cpu_time_used);
}
void after_movement(int b,int c)
{
    int temp,i,z;
    printf("\nAfter code movement optimization\n");
    clock_t start, end;
    double cpu_time_used;
    start = clock();
    temp = b*c;
    while(i<10)
    {
		z = temp * 2;
		i++;
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Result: %d",z);
    printf("\nTime taken = %f\n",cpu_time_used);
}
void main()
{
    int b=123,c=456;
    before_movement(b,c);
    after_movement(b,c);
}

/*
DO NOT TAKE INPUT FROM THE USER THE TIMER GETS DISTURBED----AQID KHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ gcc CodeMovement.c -o ./hello
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ ./hello
Before Code movement Optimization
Result: 112176
Time taken = 0.000003
After code movement optimization
Result: 112176
Time taken = 0.000001
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ 
*/
