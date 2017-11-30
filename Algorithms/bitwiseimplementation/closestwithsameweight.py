#!/usr/bin/python

def closestwithsameweight(x,l):
	for i in range(l):
		if (x >> i) & 1 != (x >> (i+1)) & 1:
			x = x ^ ((1 << i ) | (1 << (i+1)))
			return "{0:b}".format(x)

if __name__ == "__main__":
	inputstringform = raw_input()
	calculated = int(inputstringform,2)
	length = len(list(inputstringform))
	print(closestwithsameweight(x = calculated, l = length))
