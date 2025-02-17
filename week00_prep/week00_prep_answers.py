# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:29:19 2025

@author: alexr
"""

import numpy as np
# import matplotlib as plt


" EXERCISE 1 "
" Define a function called greet that takes a name as a string, then prints Hello, <name>! to the screen. "

def greet():
    name = input("Enter your word: ")
    
    return name

var = greet()


print("\nEXERCISE 1")
print("Hello, " + var + "!")

#%%

"EXERCISE 2"
"""Goldilocks is 135 cm tall, and she is very picky about the size of her bed. If the bed is shorter than
 140 cm, or larger than 150 cm, then she is unhappy. Write a function called goldilocks that takes the 
 length of a bed in cm and prints whether goldilocks is happy with it. Be sure to distinguish whether
 the bed is too small or too large!"""

def goldilocks(bedlength):
    
    if bedlength < 140:
        print("Bed is too short, Goldilocks is unhappy")
    elif bedlength > 150:
        print("Bed is too long, Goldilocks is unhappy")
    else:
        print("Bed is okay, Goldilocks is happy")
        
    return bedlength

#length = input("Enter the bed length in cm: ")
length = 143

print("\nEXERCISE 2")

var = goldilocks(length)

"EXERCISE 3"
""" Write a function called square_list that takes a list of numbers and returns a list where 
each element has been squared. """

def square_list(numbers):
    
    squared = np.square(numbers)
    
    return squared

num = [1, 2, 3]
sqr = square_list(num)

print("\nEXERCISE 3")
print("Input: ", num, "Squared: ", sqr)

"EXERCISE 4"
""" Write a function called fibonacci_stop that returns a list of the Fibonacci numbers up to a 
specified maximum value. Recall that the Fibonacci sequence is a sequence in which the next number 
is the sum of the previous two numbers: 1, 1, 2, 3, 5, etc. """

def fibonacci_stop(maxvalue):
    fibo = []
    i = 2
    fibo.append(1)
    fibo.append(1)
    while fibo[i-1] < maxvalue:
        fibo.append(fibo[i-1] + fibo[i-2])
        
        i = i + 1
        
    return fibo

fibomax = 30
var = fibonacci_stop(fibomax)
var = var[0:-1]

print("\nEXERCISE 4")
print(var)

"EXERCISE 5"
""" Define a function called clean_pitch that takes two lists, one representing measurements 
from the pitch instrument at certain points in time and the other representing the corresponding 
status signal. The function should return a cleaned list of the pitch angle, where “good” values 
are untouched and “bad” values are set to -999. """

def clean_pitch(measurements,status):
    for i in range(len(measurements)):
        if measurements[i] < 0 or measurements[i] > 90:
            if status[i] > 0:
                measurements[i] = -999
        
        
    return measurements, status

measurements = [-1, 2, 6, 95]
status = [1, 0, 0, 0]

var = clean_pitch(measurements,status)
print("\nEXERCISE 5")
print(var)


