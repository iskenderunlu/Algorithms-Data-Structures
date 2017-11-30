#!/usr/bin/python

def multiplication(x,y):
	result = 0
	while y:
		if y & 1:
			result = result + x
			x = x << 1
		else:
			x = x << 1
		y = y >> 1
	return "{0:b}".format(result)

if __name__ == "__main__":
	a = int(raw_input(),2)
	b = int(raw_input(),2)
	print(multiplication(x = a, y = b))
