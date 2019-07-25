#include <stdio.h>

/*
Kernighan & Ritchie Programming in C;
Exercise # 1-9
*/

int main(int argc, char const *argv[])
{
	int c, d, cnt;

	d = 0;

	while((c = getchar()) != EOF) {

		if (c != ' ') putchar(c);

		if(c == ' ')
			if (d != ' ')
				putchar(c);
		
		d = c;
	}
}