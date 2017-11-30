#!/usr/bin/python

def count_onebits(x):
    num_bits = 0
    while x:
        if x & 1:
            num_bits += 1
        x = x >> 1
    return num_bits

if __name__ == "__main__":
	calculated = int(raw_input())
	print(count_onebits(x=calculated))
