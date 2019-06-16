#include <stdio.h>
#include <time.h>
void before_optimise()
{
    clock_t start,end;
    double cpuTimeUsed;
    int result, i;
    start = clock();
    for( i=1; i<10; i++){
        result = i*7;
    }
    printf("Result before optimization: %d",result);
    end = clock();
    cpuTimeUsed = ((double)(end-start))/CLOCKS_PER_SEC;
    printf("\nTime taken = %f\n",cpuTimeUsed);
}
void after_optimise()
{
    clock_t start,end;
    double cpuTimeUsed;
    int result, i, temp;
    start = clock();
    temp = 0;
    for( i=1; i<10; i++){
        temp += 7;
    }
    result = temp;
    printf("Result after optimization: %d",result);
    end = clock();
    cpuTimeUsed = ((double)(end-start))/CLOCKS_PER_SEC;
    printf("\nTime taken = %f\n",cpuTimeUsed);
}
void main()
{
    before_optimise();
    after_optimise();
}
/*
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ gcc StrengthReduction.c -o ./hello
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ ./hello
Result before optimization: 63
Time taken = 0.000150
Result after optimization: 63
Time taken = 0.000003
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_9$ 
*/
