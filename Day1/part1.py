import math


def calculate_fuel(mass):
    fuel = int(mass) / 3
    fuel = math.floor(fuel)
    fuel -= 2
    return fuel


total = 0
with open("input.txt") as fp:
    for line in fp:
        total += calculate_fuel(line)
print(total)


