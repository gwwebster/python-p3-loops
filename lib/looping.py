#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # square_list = list()
    # for int in int_list:
    #     square_int = int * int
    #     square_list.append(square_int)
    square_list = [int * int for int in int_list]
    return square_list

def fizzbuzz():
    num = 1
    while num < 101:
        if num%15 == 0:
            print("FizzBuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num%3 == 0:
            print("Fizz")
        else:
            print(num)
        num += 1
