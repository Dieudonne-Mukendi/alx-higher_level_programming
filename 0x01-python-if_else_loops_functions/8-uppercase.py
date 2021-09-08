#!/usr/bin/python3
def uppercase(string):
    '''
    prints a string in uppercase followed by a new line.
    '''
    for c in string:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
