#include<stdio.h>

int max(int a, int b) { return (a > b)? a : b; }

int knapSack(int knapsackSize, int weight[], int val[], int noOfItems)
{
   int i, w;
   int K[noOfItems+1][knapsackSize+1];

   for (i = 0; i <= noOfItems; i++)
   {
       for (w = 0; w <= knapsackSize; w++)
       {
           if (i==0 || w==0)
               K[i][w] = 0;
           else if (weight[i-1] <= w)
                 K[i][w] = max(val[i-1] + K[i-1][w-weight[i-1]],  K[i-1][w]);//Mug up 
           else
                 K[i][w] = K[i-1][w];
       }
   }

   return K[noOfItems][knapsackSize];//Return the maximum possible value
}

int main()
{
    int i, noOfItems, val[20], weight[20], knapsackSize;

    printf("Enter number of items:");
    scanf("%d", &noOfItems);

    printf("Enter value and weight of items:\n");
    for(i = 0;i < noOfItems; ++i){
        scanf("%d%d", &val[i], &weight[i]);
    }

    printf("Enter size of knapsack:");
    scanf("%d", &knapsackSize);

    printf("%d", knapSack(knapsackSize, weight, val, noOfItems));
    return 0;
}
