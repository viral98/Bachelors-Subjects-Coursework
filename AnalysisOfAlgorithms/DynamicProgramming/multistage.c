#include <stdio.h>
#define MAX 10

void forward_mstage(int adj[MAX][MAX], int n, int k);

int main() {
	int n, k, adj[MAX][MAX];
	int i, j;
	clrscr();
	printf("Enter the number of stages in the graph: ");
	scanf("%d", &k);
	printf("Enter the number of vertices in the graph: ");
	scanf("%d", &n);
	printf("Enter the adjacency matrix of the multi-stage graph\n");
	for (i=0; i<n; i++) {
	printf("Input For i - %d\n",i);
		for (j=0; j<n; j++) {
			printf("Input For ( %d, %d)\n",i,j);
			scanf("%d", &adj[i][j]);
		}
	}
	forward_mstage(adj, n, k);
	getch();
	return 0;
}

void forward_mstage(int adj[MAX][MAX], int n, int k) {
	int successor[MAX], path[MAX], fcost[MAX];
	int i, j;
	int min;
	for (i=0; i<n; i++) {
		fcost[i] = 0;
		successor[i] = -1;
	}
	for (i=n-2; i>=0; i--) {
		min = 9999;
		for (j=0; j<n; j++) {
			if (adj[i][j] > 0 && adj[i][j] + fcost[j] < min) {
				min = adj[i][j] + fcost[j];
				successor[i] = j;
			}
		}
	}
	path[0] = 0;
	path[k-1] = n-1;
	for (i=1; i<k-1; i++)
		path[i] = successor[path[i-1]];
	printf("Shortest Distance Path\n");
	for (i=0; i<k; i++)
		printf("%d ", path[i]);
	printf("\n");
}
