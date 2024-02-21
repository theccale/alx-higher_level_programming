#!/usr/bin/python3
"""function to print """

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(i - diff)), end='')


101-revove_char_at.py

#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
