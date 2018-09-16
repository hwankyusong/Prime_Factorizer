#returns prime factorization in list form
#fixed emptying list issue

from math import *

L=[]

def prime(n):
	if len(L) != 0:
		del L[:]
		return helper(n)
	return helper(n)


def helper(n):
	for i in range(2,round(sqrt(n))+1):
		if n % i == 0:
			L.append(i)
			return helper(n/i)
	L.append(n)
	return L
	