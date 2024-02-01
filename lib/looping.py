#!/usr/bin/env python3

def happy_new_year():
    # using a loop countdown from 10
    # when loop gets to 0 stop countdown
    # when countdown stop print('happy new year')
        i = 10
        while i >= 0:
            print("Happy New Year!") if i < 1 else print(i)
            i -= 1
    

def square_integers(int_list):
    # code goes here!
    # takes a list of intergers and returns a list of squared elements

    # Standar ForLoop
    # ints_squared = list()
    # for ints in int_list:
    #     int_squared = ints * ints
    #     ints_squared.append(int_squared)
    
    # List Comprehension
    ints_squared = [ints * ints for ints in int_list]
    
    return ints_squared

def fizzbuzz():
    # code goes here!
    for i in range (1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 5 == 0):
            print("Buzz")
        elif (i % 3 == 0):
            print("Fizz")
        else:
            print(i)

        
