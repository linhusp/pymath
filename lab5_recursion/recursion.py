import time


def sum_to(n):
    if n <= 1:
        return 1
    return n + sum_to(n - 1)


# print(sum_to(10))


def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# print(fibo(5))


def digits(n):
    if n < 10:
        return 1
    return 1 + digits(n / 10)


# print(digits(199))


def max_list(ls):
    if len(ls) == 1:
        return ls[0]
    return max(ls[0], max_list(ls[1:]))


ls = [9, 2, 15, 3]
# print(max_list(ls))


def min_arr(arr, size):
    if size == 1:
        return arr[0]
    return min(arr[size - 1], min_arr(arr, size - 1))


# print(min_arr(ls, len(ls)))


def permutation(n, r):
    if n < r or r < 0:
        return 0
    if r == 0:
        return 1
    return n * permutation(n - 1, r - 1)


print("%s" % permutation(69, 2))

# for i in range(4):
#     print("%s " % permutation(5, i), end="")

# print()


def perm(n, r):
    if n < r or r < 0:
        return 0
    if r == 0:
        return 1
    temp = perm(n - 1, r - 1)
    print("level temp: %s, n: %s, r: %s" % (temp, n, r))
    return n * temp

# print(perm(4, -2))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# start_time = time.time()
print(gcd(18, 96))
# print(time.time() - start_time)


def move_disk(disk, start_col, end_col, times):
    print("move disk %s from %s to %s" % (disk, start_col, end_col))
    return 1

def move_tower(disk, start_col, end_col, temp_col):
    times = 1
    if disk >= 1:  
        times = move_tower(disk - 1, start_col, temp_col, end_col)
        move_disk(disk, start_col, end_col, times)
        times += move_tower(disk - 1, temp_col, end_col, start_col) 
    return times
    
print(move_tower(3, "A", "C", "B"))
