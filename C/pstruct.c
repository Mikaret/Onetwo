#include <stdio.h>

int main(int argc, char const *argv[])
{
	struct point
	{
		int x;
		int y;
	};

	struct point *pp;
	struct point origin;

	pp = &origin;

	printf("origin is (%d, %d)\n", (*pp).x, (*pp).y);


	// second more useful/common pointer to struct notation:


	printf("origin is (%d, %d)\n", pp->x, pp->y);

	return 0;
}