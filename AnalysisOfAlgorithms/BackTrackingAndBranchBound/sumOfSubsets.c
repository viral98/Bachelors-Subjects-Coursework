#include<stdio.h>

#define TRUE 1
#define FALSE 0
int inc[50],numberSet[50],sum,n;
int promising(int i,int wt,int total) {
	return(((wt+total)>=sum)&&((wt==sum)||(wt+numberSet[i+1]<=sum)));
}

void main() {
	int i,j,n,temp,total=0;

	printf("\n Enter how many numbers:\n");
	scanf("%d",&n);
	printf("\n Enter %d numbers to the set:\n",n);
	for (i=0;i<n;i++) {
		scanf("%d",&numberSet[i]);
		total+=numberSet[i];
	}
	printf("\n Input the sum value to create sub set:\n");
	scanf("%d",&sum);

  //Sort the given table in ascending order
	for (i=0;i<=n;i++)
	  for (j=0;j<n-1;j++)
	   if(numberSet[j]>numberSet[j+1]) {
		temp=numberSet[j];
		numberSet[j]=numberSet[j+1];
		numberSet[j+1]=temp;
	}
	printf("\n The given %d numbers in ascending order:\n",n);
	for (i=0;i<n;i++)
	  printf("%d \t",numberSet[i]);

  //If the total of all the weights is less than sum, then the sol is infeasible
	if((total<sum))
	  printf("\n Subset construction is not possible");
  else {
    //Initialize an 'include' set
		for (i=0;i<n;i++)
		   inc[i]=0;
		printf("\n The solution using backtracking is:\n");
		sumset(-1,0,total);
	}

}
void sumset(int i,int wt,int total) {
	int j;
	if(promising(i,wt,total)) {
		if(wt==sum) {
			printf("\n{\t");
			for (j=0;j<=i;j++)
			    if(inc[j])
			     printf("%d\t",numberSet[j]);
			printf("}\n");
		}
    else {
			inc[i+1]=TRUE;
			sumset(i+1,wt+numberSet[i+1],total-numberSet[i+1]);
			inc[i+1]=FALSE;
			sumset(i+1,wt,total-numberSet[i+1]);
		}
	}
}
