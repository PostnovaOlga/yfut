def incorrect():
	print("Incorrect_data")
def klass(n):
	i = 10
	if n > 0:
		 k=n
	else:
		k=-n
	while not ((k%i)==k):
	    i = i*10
	i = i/10
	first = k//i
	last = k%10
	if ((first % 2)==0)|((last % 2)==0):
		exit()
		incorrect()
	else:
		r = (k-i*first+i*last-last+first)
		if n > 0:
			n=r
		else:
			n=-r
	return int(n) 
try:
	n = input("Integer, the first and the last digits are odd: ")
	n = int(n)
	print("N = ", n)
	print("Result", klass(n))
except:
	 incorrect()