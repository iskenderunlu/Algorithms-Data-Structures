#!/usr/bin/python

def parity(x):
    parity = 0
    while x:
        parity = parity ^ (x & 1)
        x = x >> 1
    return parity

if __name__ == "__main__":
	calculated = int(raw_input())
	print(parity(x=calculated))
