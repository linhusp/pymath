a = [1, 2, 3, 4, 5, 1, 16, 6, 5]

def get_max2(a):
    max1 = -10e5
    max2 = -10e5

    for n in a:
        max2 = max(max2, min(max1, n))
        max1 = max(max1, n)

    return max2

print(get_max2(a))
