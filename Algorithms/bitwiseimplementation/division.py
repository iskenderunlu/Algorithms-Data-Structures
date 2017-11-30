#!/usr/bin/python

def division(x,y):
	result, power = 0, 32
	y_power = y << power
	while x >= y:
		while y_power > x:
			y_power = y_power >> 1
			power = power - 1

		result = result + 1 << power
		x = x - y_power
	return "{0:b}".format(result)

if __name__ == "__main__":
	dividend = int(raw_input(),2)
	divider = int(raw_input(),2)
	print(division(x = dividend, y = divider))
