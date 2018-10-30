import time

def list_primes(n):
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


start_time = time.time()
print(list_primes(1000000))
print("%s" % (time.time() - start_time))

def factorize(n):
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

start_time = time.time()
print(factorize(1000000))
print("%s" % (time.time() - start_time))

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    q = 0

    while b != 0:
        q = a % b
        a = b
        b = q

    return a

start_time = time.time()
print(gcd(-1, -5))
print("%s" % (time.time() - start_time))

def new_gcd(a, b):
    a = abs(a)
    b = abs(b)

    if a == 0 or b == 0:
        return a + b
    
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a

# start_time = time.time()
# print(new_gcd(1000000, 0))
# print("%s" % (time.time() - start_time))
