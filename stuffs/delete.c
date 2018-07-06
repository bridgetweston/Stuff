#include <stdio.h>

int main() {
	char star = '*';
	int numStars = 1, h = 15, w, i, j, k;
	w = 2*h - 1;
	int numSpaces;

	for (i=0; i<h; i++) {
		numSpaces = (w-numStars)/2;
		for (k=0; k<numSpaces; k++) {printf(" ");}
		for (j=0; j<numStars; j++) {printf("%c", star);}
		printf("\n");
		numStars+=2;
	}

	return 0;
}