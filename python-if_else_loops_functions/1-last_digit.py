#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = str(number)[-1]
print(f"Last digit of {number} is {last_digit} and is", end=" ")

last_digit = int(last_digit)
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")

