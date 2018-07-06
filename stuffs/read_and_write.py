#Reading and writing to file
#By: Bridget Weston

#set-up / inactive
def fib(numTerms):
	a=0; b=1;
	print(a);
	print(b);
	for i in range(0, numTerms):
		nextTerm = a + b;
		print(nextTerm);
		a = b;
		b = nextTerm;#prints each term of fibonacci sequence in given range

#run:
file = open("file.txt","w+"); #creates new file named "file.txt" in common dir

i=0;

while i < 10:
	toAdd = i*2;
	file.write(i*2);
	file.close;
	i = i + 1;