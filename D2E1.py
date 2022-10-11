"""
 This program prints the following pattern

|
||
|||
||||
|||||

"""

import sys

for y in range(1,6):
    for x in range(1, y+1):
        sys.stdout.write("|")
    print() # prints the new-line
