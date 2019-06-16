#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#define MAX 10
#define M 4
#define P 3
#define Q 3
float rotation[P][Q], translation[P][Q], scaling[P][Q], inputMatrix[M][P],temp[M][P];
void init(float matrix[M][Q]){
	int i,j;
	for(i=0;i<M;i++){
		for(j=0;j<Q;j++){
			matrix[i][j] = 0;
		}
	}
}
void printMatrix(float matrix[3][3]){
	int i, j;



}
void print(float matrix[M][P]){
	line(320+matrix[0][0],240-matrix[0][1],320+matrix[1][0],240-matrix[1][1]);
	line(320+matrix[1][0],240-matrix[1][1],320+matrix[2][0],240-matrix[2][1]);
	line(320+matrix[2][0],240-matrix[2][1],320+matrix[3][0],240-matrix[3][1]);
	line(320+matrix[3][0],240-matrix[3][1],320+matrix[0][0],240-matrix[0][1]);
}
void matrixMultiply(float matrix1[3][3], float matrix2[3][3]){
	int i,j,k;
	float matrix[M][P],sum=0;
       //	init(matrix);
	for(i=0;i<M;i++){
		for(j=0;j<Q;j++){
			sum=0;
			for(k=0;k<P;k++){
				sum = sum + matrix1[i][k] * matrix2[k][j];
			}
			matrix[i][j] =sum;
			temp[i][j] =sum;
		}

	}
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			inputMatrix[i][j]=temp[i][j];
		}
	}
	print(matrix);
}
void main(){
	int i,j;//Counter variables
	int check;
	float theta,Sx,Sy,Tx,Ty;
	int gd=DETECT,gm;
	initgraph(&gd,&gm,"");

	init(rotation);
	init(translation);
	init(scaling);
	init(temp);
	line(0,240,640,240);//X axis
	line(320,0,320,480);//Y axis
	printf("Enter the point to rotate about\n");
	scanf("%f",&Tx);
	scanf("%f",&Ty);
	printf("Enter the input matrix\n");
	for(i=0;i<M;i++){
		for(j=0;j<P;j++){
			scanf("%f",&inputMatrix[i][j]);
		}
	}
	printf("Enter the value of theta\n");
	scanf("%f",&theta);
	//Translate
	translation[2][0] = -Tx;
	translation[2][1] = -Ty;
	translation[2][2] = 1;
	translation[1][1] = 1;
	translation[0][0] = 1;
	matrixMultiply(inputMatrix,translation);
	//Rotation
	theta = (theta / 180)*3.14;
	rotation[0][0] = cos(theta);
	rotation[0][1] = sin(theta);
	rotation[1][0] = -sin(theta);
	rotation[1][1] = cos(theta);
	rotation[2][2] = 1;
	matrixMultiply(inputMatrix,rotation);
	 init(translation);
	//Translate
	translation[2][0] = Tx;
	translation[2][1] = Ty;
	translation[2][2] = 1;
	translation[1][1] = 1;
	translation[0][0] = 1;
	matrixMultiply(inputMatrix,translation);
	getch();
	closegraph();
}

