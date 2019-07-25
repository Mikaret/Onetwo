#include <stdio.h>

#define IN 1
#define	OUT 2

/*
Kernighan & Ritchie Programming in C;
Exercise # 1-12
*/

int main(int argc, char const *argv[])
{
	int c, nl, nw, nc, state;

	state = OUT;
	while ((c=getchar()) != EOF) {

		if (c == ' ' || c == '\n' || c == '\t') {
			state = OUT;
			printf("\n");
		}
		else if (state == OUT) {
			state = IN;
			putchar(c);
		}

		else if (state == IN) {
			putchar(c);
		}
	
	
	}
	
}