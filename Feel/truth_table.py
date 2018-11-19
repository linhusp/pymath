import itertools

def implies(a, b):
    if a:
        return b
    return True

x = 1
y = 2
v = 3

print(implies(x >= 0 and y >= 0, v * y >= 0))

def or_table(a, b):
    for i in range(4):
        if a:
            print("%s, %s" %(a, b))
        else:
            print("%s, True" %a)

or_table(False, True)

n = 3
table = list(itertools.product([False, True], repeat=n))

for i in table:
    print(i)
