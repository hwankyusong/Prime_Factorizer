from math import *

def prime(n):
	for i in range(2,round(sqrt(n))+1):
		if n % i == 0:
			print (i)
			return prime(n/i)
		i = i + 1
	print(n)