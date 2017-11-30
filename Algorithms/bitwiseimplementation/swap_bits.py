#!/usr/bin/python

def swap_bits(x,i,j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1<<i) | (1<<j)
        x = x ^ bit_mask
    return x
if __name__ == "__main__":
	calculated = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
	print(swap_bits(x=calculated,i=a,j=b))
