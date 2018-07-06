#Python learning/test program

def fib(numTerms):
	a=0; b=1;
	print(a);
	print(b);
	for i in range(0, numTerms):
		nextNum = a + b;
		print(nextNum);
		a = b;
		b = nextNum;


#everything run at execution:
fib(15);