#!/usr/bin/python

def count_bits(x):
    num_bits = 0
    while x:
        x = x >> 1
        num_bits += 1
    return num_bits

if __name__ == "__main__":
	calculated = int(raw_input())
	print(count_bits(x=calculated))
