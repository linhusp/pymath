import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def box(trials):
    b = [1, 2, 3, 4, 5]
    count = 0
    for i in range(trials):
        b1 = random.choice(b)
        b2 = random.choice(b)

        if is_prime(b1 + b2) and b1 + b2 != 2:
            count += 1

    return count / trials

print(box(100000))
