#!/usr/bin/python3

def print_last_digit(number):
    if (number < 0):
        number = number * -1

    x = number % 10
    number = x
    print("{}".format(number), end='')

    return(number)
