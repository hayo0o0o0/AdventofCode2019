import math


def calculate_fuel(mass):
    fuel = int(mass) / 3
    fuel = math.floor(fuel)
    fuel -= 2

    if fuel < 0:
        return 0
    return fuel + calculate_fuel(fuel)


total = 0
with open("input.txt") as fp:
    for line in fp:
        total += calculate_fuel(line)
print(total)
