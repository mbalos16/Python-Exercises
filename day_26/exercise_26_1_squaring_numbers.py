# Exercise 26.1. Squaring numbers 

# Instructions: 
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

# e.g. 4 * 4 = 16
# 4 squared equals 16.

# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

import pandas as pd

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number*number for number in numbers]

#Write your code 👆 above:

print(squared_numbers)
