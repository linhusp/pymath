import math
import time


def main():
    t = time.time()
    # print(len(eratosthenes(10000000)))
    n = 1000000
    # l = n * (10 + int(str(n)[0])) + max(0, 10**(len(str(n)) - 1))
    # print(len(eratosthenes(l)))
    # print(eratosthenes(l)[n - 1])
    print(eratosthenes(n))
    # print(list_prime(n))
    print(time.time() - t)


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def list_prime(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


def eratosthenes(n):
    n += 1
    mask = [True for i in range(n)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if mask[i]:
            for j in range(i * i, n, i):
                mask[j] = False

    return [i for i in range(2, n) if mask[i]]


if __name__ == "__main__":
    main()
