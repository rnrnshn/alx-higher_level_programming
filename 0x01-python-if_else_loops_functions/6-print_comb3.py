#!/usr/bin/python3
for i in range(1, 90):
   if i < int("{0:02d}".format(i)[::-1]):
        if i < 89:
            print("{0:02d}, ".format(i), end='')
        else:
            print("{}".format(i))
