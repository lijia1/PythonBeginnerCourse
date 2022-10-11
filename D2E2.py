"""
This program prints the following pattern (a pyramid)

0001000
0011100
0111110
1111111

"""
import sys

k = 0
for y in range(1, 5): # y is the rowß
    for x in range(1,8): # x is the column
        if (x >= 4-k) and (x < 5+k):
            sys.stdout.write("1")
        else:
            sys.stdout.write("0")
    print() # print the new line
    k = k + 1
