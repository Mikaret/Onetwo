#include <stdio.h>

#define MAX 1000

int binsearch(int x, int v[], int n);

int main(int argc, char const *argv[])
{

	int k;
	int ar[MAX];

	for (int i = 0; i < MAX; i++)	{
		ar[i] = i;
	}

	k = binsearch(333, ar, MAX);

	printf("%d\n", k);
	
	return 0;
	
}

int binsearch(int x, int v[], int n) {

	int low, high, mid;

	low = 0;

	high = n - 1;

	while (low <= high) {

		mid = (low + high) / 2;
		if (x < v[mid]) 
			high = mid - 1;
		else if (x > v[mid])
			low = mid + 1;
		else
			return mid;

	}

	return -1;
	
}