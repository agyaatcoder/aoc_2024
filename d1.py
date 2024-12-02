#https://adventofcode.com/2024/day/1/input

import os
from utils import fetch_input

session_cookie = os.getenv("SESSION_COOKIE")

year = 2024
day  = 1
puzzle_input = fetch_input(year, day, session_cookie)

# Parse the input
list1 = []
list2 = []

# Split the input into lines
lines = puzzle_input.strip().split("\n")

# Split each line into two numbers and add to the respective lists
for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

result = sum([abs(list1[i]-list2[i]) for i in range(len(list1))])
print(f"{result=}")