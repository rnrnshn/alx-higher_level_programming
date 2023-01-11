#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number_of_args = len(sys.argv)
    if number_of_args < 2:
        print("{} arguments.".format(number_of_args - 1))
    elif number_of_args == 2:
        print("{} argument:".format(number_of_args - 1))
        print("{}: {}".format(number_of_args - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(number_of_args - 1))
        for i in range(1, number_of_args):
            print("{}: {}".format(i,sys.argv[i]))
