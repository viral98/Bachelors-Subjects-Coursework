#include<stdio.h>
int cost[8][8],dist[8][8],n;
void main()
{
	int i,j,k,m,u,INF=100;
	printf("\nEnter the no. of vertices: ");
	scanf("%d",&n);
	printf("\nEnter the adjacency matrix(Enter 100 if there is no edge present)\n");
	for(i=1;i <= n;i++)
		for(j=1;j <= n;j++)
		{
			scanf("%d",&cost[i][j]);
		}
	for(i=1;i <= n;i++)
		dist[i][1]=0;
	printf("\nDistance Matrix:\n");
	for(i=2;i <= n;i++)
	{
		dist[1][i]=cost[1][i];
		printf("%d    ",dist[1][i]);
	}
	printf("\n");
	printf("\n");
	for(k=2;k < n;k++)
	{
		for(u=2;u <= n;u++)
		{
			m=min(k,u);
			if(dist[k-1][u] > m)
				dist[k][u]=m;
			else
				dist[k][u]=dist[k-1][u];
			printf("%d    ",dist[k][u]);
		}
		printf("\n");
		printf("\n");
	}
	for(i=1;i <= n;i++)
	{
		printf("\nDistance of 1 to %d is ",i);
		printf("%d    ",dist[n-1][i]);
	}
}

int min(int k,int u)
{
	int min1,i;
	min1=dist[k-1][1]+cost[1][u];
	for(i=2;i <= n;i++)
		if(min1 > (dist[k-1][i]+cost[i][u]))
			min1=dist[k-1][i]+cost[i][u];
	return min1;
}
