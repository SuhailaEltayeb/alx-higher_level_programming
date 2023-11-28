#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
if number < 0:
    ldigit = -(ldigit)
string = "Last digit of {} is {}".format(number, ldigit)
if ldigit > 5:
    print(f"{string} and is greater than 5")
elif ldigit == 0:
    print(f"{string} and is 0")
elif ldigit < 6:
    print(f"{string} and is less than 6 and not 0")
