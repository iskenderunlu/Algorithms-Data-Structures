#!/usr/bin/python

def reverse_bits(x):
	reverse = 0
	while x:
		reverse = (reverse << 1) + (x & 1)
		x = x >> 1
	return "{0:b}".format(reverse)

if __name__ == "__main__":
	calculated = int(raw_input(),2)
	print(reverse_bits(x = calculated))
