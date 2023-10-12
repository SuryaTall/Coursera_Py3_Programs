#Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(x):
    return x

#Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(x):
    return x + 2

#Write a function called change that takes any string,
#  adds “Nice to meet you!” to the end of the argument given, and returns that new string.

def change(x):
    return x + "Nice to meet you!"

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(x):
    y = 0
    for i in x:
        y += i
    return y

#Write a function, length, that takes in a list as the input.
#  If the length of the list is greater than or equal to 5, return “Longer than 5”.
#  If the length is less than 5, return “Less than 5”.

def length(x):
    y = 0
    for i in x:
        y += 1
        i += 0
    if y >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

#You will need to write two functions for this problem. 
# The first function, divide that takes in any number and returns that same number divided by 2. 
# The second function called sum should take any number, divide it by 2, and add 6.
#  It should return this new number. You should call the divide function within the sum function.
#  Do not worry about decimals.

def divide(x):
    return x/2
def sum_(x):
    return (x/2) + 6

