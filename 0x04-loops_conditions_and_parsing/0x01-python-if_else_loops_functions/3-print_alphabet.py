!/usr/bin/python3
"""function to print some alphabeth"""

for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
