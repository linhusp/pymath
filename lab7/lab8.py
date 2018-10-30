import random
import itertools


# Ex5
def ways(n):
    """
    n - int, the number of boxes
    function returns the number of ways (int) by which 
    at least one box contains a white ball and 
    boxes containing white balls are consecutively numbered
    """
    if n == 1:
        return 1
    return n + ways(n - 1)

print(ways(1))


def integers(n):
    """
    n - int, n >= 3
    function returns an int - how many integers are there with 1, 2, or 3 in the correct position
    """
    perms = itertools.permutations(range(1, n + 1), n)
    count = 0
    for perm in list(perms):
        if perm[0] == 1 and perm[1] == 2 and perm[2] == 3:
            count += 1

    return count


print(integers(5))

# Ex7
def smallest(p):
    """
    p - float, probability of two or more persons having the same birthday 
    function returns an int - the smallest number of people
    """
    pass

# print(smallest(0.5))

# Ex8
def smallest_number(s):
    """
    s - int, sum (example = 15)
    function returns an int - the smallest number of integers 
    you must choose from S such that two of them sum to s,
    where S = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    """

    nums = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    def exist(a_set, value):
        subsets = list(itertools.combinations(a_set, 2))
        for subset in subsets:
            if subset[0] + subset[1] == value:
                return True
        return False

    def all_subsets(a_set, n, value):
        subsets = list(itertools.combinations(a_set, n))
        
        for subset in subsets:
            if not exist(subset, value):
                return False
        return True
    
    n = 2
    while not all_subsets(nums, n, s):
        n += 1

    return n

print(smallest_number(15))
