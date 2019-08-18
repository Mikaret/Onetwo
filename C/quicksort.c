#include <stdio.h>

#define MAX 100

void swap(int v[], int i, int j) {
	int temp;

	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
}

void qsort(int v[], int left, int right) {

	int i, last;

	if (left >= right)
		return;
	swap(v, left, (left+right)/2);
		last = left;
		for(i = left+1; i <= right; i++)
			if (v[i] < v[left])
				swap(v, ++last, i);
			swap(v,left,last);
			qsort(v,left,last-1);
			qsort(v,last+1,right);
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

	qsort(ar, 0, MAX-1);

printf("After:\n");
	for(int i = 0; i < MAX; i++) {
		printf("%d\t", ar[i]);
	}
	printf("\n");


	return 0;
}