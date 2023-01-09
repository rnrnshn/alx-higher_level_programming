#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit = abs(((number * -1) % 10) * -1)
    else:
        last_digit = number % 10
    print("{}".format(last_digit), end='')
    return last_digit
