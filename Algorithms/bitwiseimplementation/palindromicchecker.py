#!/usr/bin/python

def palindromechecker(decimal_integer):
	list_decimal_integer = list(decimal_integer)
	length = len(list_decimal_integer)
	for i in range(length // 2):
		if list_decimal_integer[i] != list_decimal_integer[length-1-i]:
			return False
	return True


if __name__ == "__main__":
	integer = raw_input()
	if palindromechecker(decimal_integer = integer):
		print("Your string is palindromic")
	else:
		print("Your string is not palindromic")
