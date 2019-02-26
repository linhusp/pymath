import time


#1
def list_primes(n):
    """return a list of prime numbers less than n"""
    check = []
    valid = []

    for i in range(n + 1):
        check.append(True)

    for i in range(2, n + 1):
        if check[i] == True:
            j = i + i

            while j <= n:
                if j % i == 0:
                    check[j] = False
                j += i

    for i in range(2, n + 1):
        if check[i] == True:
            valid.append(i)

    return valid

print(list_primes(1000))


#2
def factorize(n):
    """return a dict of prime factorization of n"""
    d = {}
    ls = list_primes(n - 1)

    for i in ls:
        count = 0
        
        while n % i == 0:
            n = n / i
            count += 1

        if count != 0:
            d[i] = count

    return d

print(factorize(243))


#3
def gcd(a, b):
    """return greatest common divisor of a and b"""
    a = abs(a)
    b = abs(b)
    q = 0

    while b != 0:
        q = a % b
        a = b
        b = q

    return a

print(gcd(2, 100))
