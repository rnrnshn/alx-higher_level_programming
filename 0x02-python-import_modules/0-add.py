#!/usr/bin/python3
if __import__("__main__").__spec__ is None:
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
