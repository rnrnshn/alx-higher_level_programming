#!/usr/bin/python3
def uppercase(str):
    char = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            char += chr(ord(str[i]) - 32)
        else:
            char += str[i]

    print("{}".format(char))
