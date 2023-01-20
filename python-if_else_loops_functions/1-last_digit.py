#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
# keep sign, unless it's 0 (so, -123 -> -3, -120 -> 0
# and 123 -> 3)

print(f"Last digit of {number} is {last_digit} and is", end=" ")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
# yes, we want to print "Last digit of 0 is 0 and is 0"
