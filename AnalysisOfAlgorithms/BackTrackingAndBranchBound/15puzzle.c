#include<stdio.h>
int m=0,n=4;

int cal(int temp[10][10],int t[10][10])
{
	int i,j,m=0;
	for(i=0;i < n;i++)
		for(j=0;j < n;j++){
			/*Check the number of differences between the
			current temp matrix and the target matrix*/
			if(temp[i][j]!=t[i][j])
				m++; //m represents the number of differences
		}
	return m;
}

int check(int a[10][10],int t[10][10])
{
	int i,j,f=1;
	/*Flag initialized to true indicating no differences between
	temporary and target matrices*/
	for(i=0;i < n;i++)
		for(j=0;j < n;j++)
			if(a[i][j]!=t[i][j])
				f=0;
				/*Flag turns false if there is any difference between
				the temp matrix provided and the target*/
	return f;
}


void main()
{
	int p,i,j,n=4,a[10][10],t[10][10],temp[10][10],r[10][10];
	int m=0,x=0,y=0,d=1000,dmin=0,l=0;
	printf("\nEnter the 4x4 matrix to be solved,space with zero :\n");
	for(i=0;i < n;i++)
		for(j=0;j < n;j++)
			scanf("%d",&a[i][j]);

	printf("\nEnter the target 4x4 matrix,space with zero :\n");
	for(i=0;i < n;i++)
		for(j=0;j < n;j++)
			scanf("%d",&t[i][j]);
//Redundant Printing
	printf("\nEntered Matrix is :\n");
	for(i=0;i < n;i++)
	{
		for(j=0;j < n;j++)
			printf("%d\t",a[i][j]);
		printf("\n");
	}

	printf("\nTarget Matrix is :\n");
	for(i=0;i < n;i++)
	{
		for(j=0;j < n;j++)
			printf("%d\t",t[i][j]);
		printf("\n");
	}

	while(!(check(a,t)))//a is original matrix and t is target matrix
	{
		l++;
		d=1000;//Initial assignment of ridiciously high value, gets replaced in the first iteration
		for(i=0;i < n;i++)
			for(j=0;j < n;j++)
			{
				if(a[i][j]==0)
				{
					x=i;
					y=j;
				}
			}//End of both for loops

		//To move upwards
		for(i=0;i < n;i++)
			for(j=0;j < n;j++)
				temp[i][j]=a[i][j];
		//Check if x is in the top most row, if so, we cannot move it further upwards
		if(x!=0)
		{
			//Exchange the value above the hole and the hole
			p=temp[x][y];
			temp[x][y]=temp[x-1][y];
			temp[x-1][y]=p;
		}
		m=cal(temp,t);//t is target matrix
		dmin=l+m;//Here, l is the counter variable for current iteration
		if(dmin < d)
		{
			d=dmin;//d represents the overall minimum value
			for(i=0;i < n;i++)
				for(j=0;j < n;j++)
					r[i][j]=temp[i][j];
		}

		//To move downwards
		for(i=0;i < n;i++)
			for(j=0;j < n;j++)
				temp[i][j]=a[i][j];
		if(x!=n-1)//Check if the hole is in the last row
		{
			//If not, exchange the value below it
			p=temp[x][y];
			temp[x][y]=temp[x+1][y];
			temp[x+1][y]=p;
		}
		m=cal(temp,t);
		dmin=l+m;
		if(dmin < d)
		{
			d=dmin;
			for(i=0;i < n;i++)
				for(j=0;j < n;j++)
					r[i][j]=temp[i][j];
		}

		//To move right side
		for(i=0;i < n;i++)
			for(j=0;j < n;j++)
				temp[i][j]=a[i][j];
		if(y!=n-1)//Check if the hole is in the rightmost column
		{
			p=temp[x][y];
			temp[x][y]=temp[x][y+1];
			temp[x][y+1]=p;
		}
		m=cal(temp,t);
		dmin=l+m;
		if(dmin < d)
		{
			d=dmin;
			for(i=0;i < n;i++)
				for(j=0;j < n;j++)
					r[i][j]=temp[i][j];//r represents the final matrix
		}

		//To move left
		for(i=0;i < n;i++)
			for(j=0;j < n;j++)
				temp[i][j]=a[i][j];
		if(y!=0)
		{
			p=temp[x][y];
			temp[x][y]=temp[x][y-1];
			temp[x][y-1]=p;
		}
		m=cal(temp,t);
		dmin=l+m;
		if(dmin < d)
		{
			d=dmin;
			for(i=0;i < n;i++)
				for(j=0;j < n;j++)
					r[i][j]=temp[i][j];
		}

		printf("\nCalculated Intermediate Matrix Value :\n");
		for(i=0;i < n;i++){
			for(j=0;j < n;j++)
			  printf("%d\t",r[i][j]);
			printf("\n");
		}
		//Make the original matrix a equal to the Intermediate matrix r and reset temp
		for(i=0;i < n;i++)
			for(j=0;j < n;j++){
			  a[i][j]=r[i][j];
			  temp[i][j]=0;
			}
		printf("Minimum cost : %d\n",d);
	}
}
