#!/usr/bin/python

def power(base,exponent):
	result, power = 1, exponent
	while power:
		if power & 1:
			result = result * base
		base, power = ( base * base ), power >> 1
	return "{0:b}".format(result)

if __name__ == "__main__":
	x = int(raw_input(),2)
	y = int(raw_input(),2)
	print(power(base = x, exponent = y))
