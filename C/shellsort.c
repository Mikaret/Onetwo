#include <stdio.h>

#define MAX 100

void shellsort(int v[], int n){
	int gap, i, j, temp;

	for (gap = n/2; gap > 0; gap /=2)
		for (i = gap; i < n; i++)
			for (j=i-gap; j >= 0 && v[j] > v[j+gap]; j-=gap) {
				temp = v[j];
				v[j] = v[j+gap];
				v[j+gap] = temp;
			}
}

int main(int argc, char const *argv[])
{
	int ar[MAX];

	for(int i = 0; i < MAX; i++) {
		if (i%2==0) ar[i] = MAX - i;
		else ar[i] = i;
	}

	printf("Before:\n");

	for(int i = 0; i < MAX; i++) {
		printf("%d\t", ar[i]);
	}
	printf("\n\n");

	shellsort(ar, MAX);

printf("After:\n");
	for(int i = 0; i < MAX; i++) {
		printf("%d\t", ar[i]);
	}
	printf("\n");


	return 0;
}

