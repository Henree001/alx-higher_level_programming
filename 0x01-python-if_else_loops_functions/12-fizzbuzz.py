#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
	    if i % 3 == 0 and i % 5 == 0:
		    i = "FizzBuzz"
	    if i == 3:
		    i = "Fizz"
	    if i == 5:
		    i = "Buzz"
	    if i == 100:
		    print(f"{i}")
	    else:
		    print(f"{i}", end=" ")
