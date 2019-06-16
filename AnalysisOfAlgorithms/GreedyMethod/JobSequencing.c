#include <stdio.h>

#define MAX 100

typedef struct Job {
	char id[5];
	int deadline;
	int profit;
} Job;

void jobSequencingWithDeadline(Job jobs[], int n);

int minValue(int x, int y) {
	if(x < y) return x;
	return y;
}

int main(void) {
	//variables
	int i, j;

	//jobs with deadline and profit
	Job jobs[5] = {
		{"j1", 2,  60},
		{"j2", 1, 100},
		{"j3", 3,  20},
		{"j4", 2,  40},
		{"j5", 1,  20},
	};

	//temp
	Job temp;

	//number of jobs
	int n = 5;

	//sort the jobs profit wise in descending order
	for(i = 1; i < n; i++) {
		for(j = 0; j < n - i; j++) {
			if(jobs[j+1].profit > jobs[j].profit) {
				temp = jobs[j+1];
				jobs[j+1] = jobs[j];
				jobs[j] = temp;
			}
		}
	}

	printf("%10s %10s %10s\n", "Job", "Deadline", "Profit");
	for(i = 0; i < n; i++) {
		printf("%10s %10i %10i\n", jobs[i].id, jobs[i].deadline, jobs[i].profit);
	}

	jobSequencingWithDeadline(jobs, n);

	return 0;
}

void jobSequencingWithDeadline(Job jobs[], int n) {
	//variables
	int i, j, k, maxprofit;

	//free time slots
	int timeSlot[MAX];

	//filled time slots
	int filledTimeSlot = 0;

	//find max deadline value
	int maximumDeadline = 0;
	for(i = 0; i < n; i++) {
		if(jobs[i].deadline > maximumDeadline) {
			maximumDeadline = jobs[i].deadline;
		}
	}

	//free time slots initially set to -1 [-1 denotes EMPTY]
	for(i = 1; i <= maximumDeadline; i++) {
		timeSlot[i] = -1;
	}

	printf("maximumDeadline: %d\n", maximumDeadline);

	for(i = 1; i <= n; i++) {
		k = minValue(maximumDeadline, jobs[i - 1].deadline);
		while(k >= 1) {
			if(timeSlot[k] == -1) {
				timeSlot[k] = i-1;
				filledTimeSlot++;
				break;
			}
			k--;
		}

		//if all time slots are filled then stop
		if(filledTimeSlot == maximumDeadline) {
			break;
		}
	}

	//required jobs
	printf("\nRequired Jobs: ");
	for(i = 1; i <= maximumDeadline; i++) {
		printf("%s", jobs[timeSlot[i]].id);

		if(i < maximumDeadline) {
			printf(" --> ");
		}
	}

	//required profit
	maxprofit = 0;
	for(i = 1; i <= maximumDeadline; i++) {
		maxprofit += jobs[timeSlot[i]].profit;
	}
	printf("\nMax Profit: %d\n", maxprofit);
}
