#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = repr(number)
last_digitstr = last_num[-1]
last_digit = int(last_digitstr)
if last_digit > 5:
	print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6:
	print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
	print(f"Last digit of {number} is {last_digit} and is 0")
