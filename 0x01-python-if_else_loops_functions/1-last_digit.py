#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
    num = num % 10
    num *= -1
else:
    lastdigit = number % 10
if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {lastdigit}", end=' ')
    print("and is less than 6 and not 0")
