#!/usr/bin/python3
def uppercase(str): 
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i))
        print("{}".format(i), end="")
    print("")