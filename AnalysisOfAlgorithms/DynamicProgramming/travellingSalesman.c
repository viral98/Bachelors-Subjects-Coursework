#include<stdio.h>

int distanceBetween[10][10],visited[10],n,cost=0;

void get(){
	int i,j;
	printf("Enter No. of Cities: ");
	scanf("%d",&n);
	printf("\nEnter Cost Matrix\n");
	for(i=0;i < n;i++){
		printf("\nEnter Elements of Row # : %d\n",i+1);
		for( j=0;j < n;j++)
			scanf("%d",&distanceBetween[i][j]);
			visited[i]=0;
	}
	printf("\n\nThe cost list is:\n\n");
	for( i=0;i < n;i++){
		printf("\n\n");
		for(j=0;j < n;j++)
			printf("\t%d",distanceBetween[i][j]);
	}
}

void mincost(int city){
	int i,newCity;
	visited[city]=1;
	printf("%d -->",city+1);
	newCity=least(city);
	if(newCity==999){ //This is the terminating condition of the algorithm
	/*Newcity = 999 when all other cities were visitied and no new values could be assigned to
	the newCity variable in least() function. Hence it returned the default 999*/
		newCity=0;
		printf("%d",newCity+1);
		cost+=distanceBetween[city][newCity];
		return;
	}
	mincost(newCity);
}

int least(int currentCity){
	int i,newCity=999;
	int min=999,kmin;
	for(i=0;i < n;i++){
		if((distanceBetween[currentCity][i]!=0)&&(visited[i]==0))
			if(distanceBetween[currentCity][i] < min){
				min=distanceBetween[i][0]+distanceBetween[currentCity][i];
				kmin=distanceBetween[currentCity][i];
				newCity=i;
			}
	}
	if(min!=999)
		cost+=kmin;
	return newCity;
}

void put(){
	printf("\n\nMinimum cost:");
	printf("%d\n",cost);
}

void main(){
	get();
	printf("\n\nThe Path is:\n\n");
	mincost(0);
	put();
}
