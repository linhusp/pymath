import time


#1
def sum_to(n=10):
    """return sum from 1 to n | n >= 1\n"""
    if n <= 1:
        return 1
    return n + sum_to(n - 1)

print(sum_to())


#2
def fibo(n):
    """
    return the nTH fibonacci number\n
    fibo(20)
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(20))


#3
def digits(n):
    """
    return the number of digits a positive integer n has\n
    digits(199)
    """
    if n < 10:
        return 1
    return 1 + digits(n / 10)

print(digits(199))


#4
def max_list(ls):
    """
    return the maximum in list ls\n
    ls = [9, 2, 15, 3]
    """
    if len(ls) == 1:
        return ls[0]
    return max(ls[0], max_list(ls[1:]))

ls = [9, 2, 15, 3]
print(max_list(ls))


#5
def min_arr(arr, size):
    """
    return the minimum element in an array, array and size are given as parameters\n
    arr = [9, 2, 15, 3]
    """
    if size == 1:
        return arr[0]
    return min(arr[size - 1], min_arr(arr, size - 1))

print(min_arr(ls, len(ls)))


#6
def P(n, r):
    """
    return n(n-1)(n-2)...(n-r+1) if n >= r > 0 otherwise return 1\n
    P(8, 2)
    """
    if n < r or r < 0:
        return 0
    if r == 0:
        return 1
    return n * P(n - 1, r - 1)

print(P(8, 2))


#7
def move_disk(disk, start, end):
    print("move disk %s from %s to %s" % (disk, start, end))
    return 1

def move_tower(disk, start, end, temp):
    """
    return the number of moves to move the tower with n disks from start column to end (goal) column\n
    move tower(4, "A", "B", "C")
    """
    if disk == 1:
        return move_disk(disk, start, end)
    return move_tower(disk - 1, start, temp, end) + move_disk(disk, start, end) + move_tower(disk - 1, temp, end, start)
    
print("moves = %s" % move_tower(4, "A", "B", "C"))


#8
def gcd(a, b):
    """
    return greatest common divisor recursively\n
    gcd(18, 96)
    """
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(18, 96))
