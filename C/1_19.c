
/*
Kernighan & Ritchie Programming in C;
Exercise # 1-19
(Reverse the input string)
*/

#include <stdio.h>

#define MAXLINE 1000


int line(char line[], int maxline);
void reverse(char s[]);

int main(int argc, char const *argv[])
{

	char s[MAXLINE];

	while (line(s, MAXLINE) > 0) {

		reverse(s);
		printf("%s", s);
	}

}


int line(char s[], int maxlen) {
  char c;
  int i;
  for (i = 0; (c = getchar()) != EOF; i++) {
    s[i] = c;
    if (c == '\n') {
      s[i] = c;
      ++i;
    }
  }
  s[i] = '\0';
  return i;
}

void reverse(char s[]) {
	int i, j;
	char temp;

	i = 0;
	while (s[i] != '\0')
		++i;
	
	--i;
	if(s[i] == '\n')
		--i;
	j=0;
	while(j < i) {
		temp = s[j];
		s[j] = s[i];
		s[i] = temp;
		--i;
		++j;
	}

}


