#!/usr/bin/python

def add(x, y):
    carry, partialSum = 1, 1
    while carry:
        partialSum = x ^ y
        carry = (x & y) << 1
        x = partialSum
        y = carry
    return "{0:b}".format(partialSum)

if __name__ == "__main__":
	a = int(raw_input(),2)
	b = int(raw_input(),2)
	print(add(x = a, y = b))
