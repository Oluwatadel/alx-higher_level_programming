#!/usr/bin/python3
import random
ld = ("Last digit of ")
number = random.randint(-10000, 10000)
if number > 0:
    remainder = number % 10
else:
    remainder = number % -10
if remainder > 5:
    print("{}{} is {} and is greater than 5".format(ld, number, remainder))
elif remainder == 0:
    print("{}{} is {} and is 0".format(ld, number, remainder))
else:
    print(f'{ld}{number} is {remainder} and is less than 6 and not 0')
