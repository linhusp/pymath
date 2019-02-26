import math

def prob(people):
    base = 2
    chance = 364 / 365
    while base < people:
        chance *= (365 - base) / 365
        base += 1
        print(1 - chance)
    return 1 - chance


print("chance = %s" % prob(85))
print(1 - math.factorial(85) / math.factorial(365))
print(1 - math.factorial(85) / (pow(365, 85)))
print(1 - pow(35, 84) / (math.factorial(85) * math.factorial(84)))
print(1 - math.factorial(365) / (math.factorial(280) * pow(365, 85)))
