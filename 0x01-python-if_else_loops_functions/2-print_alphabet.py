#!/usr/bin/python3
"""function to print alphabeths"""

for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')
