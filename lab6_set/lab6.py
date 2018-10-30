import random

# Ex1


def sym_dif(A, B):
    """
    sym_dif([1,2,3],[3,4])
    returns a list
    """
    return set(A).symmetric_difference(B)


a = [1, 2, 3]
b = [3, 4]
print(sym_dif(a, b))

# Ex2


def remove_dup(A):
    """
    remove_dup([1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2])
    returns a set
    """
    temp = []
    for i in range(len(A)):
        if A[i] not in A[i+1:]:
            temp.append(A[i])
    return set(temp)


print(remove_dup([1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2]))

# Ex3


def allowed(users, bad):
    """
    users = ['tom', 'pam', 'sasha', 'jj', 'que', 'jeff']
    bad = set(['jeff', 'sasha'])
    allowed(users,bad)
    return a set
    """
    return set(sym_dif(users, bad))


users = ['tom', 'pam', 'sasha', 'jj', 'que', 'jeff']
bad = set(['jeff', 'sasha'])
print(allowed(users, bad))

# Ex4


def prob(first, second, trials):
    """
    first = 2
    second = 5
    trials = 100000
    prob(first, second, trials)
    return a float - probability
    """
    a = 0
    b = 0
    count = 0
    temp = [first, second]
    for i in range(trials):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        if a in temp and b in temp:
            count += 1
    return float(count) / trials


print(prob(2, 5, 10000))

# Ex5


def translate(week_day):
    """
    week_day - day of week, e.g. Monday, Tuesday
    return a int, e.g. 2, 3
    in function you have to use a data structure type - dictionary
    """
    days = {
        "Mon": 1,
        "Tue": 2,
        "Wed": 3,
        "Thu": 4,
        "Fri": 5,
        "Sat": 6,
        "Sun": 7,
    }
    for i in days:
        if week_day == i:
            return days[i]


print(translate("Mon"))

# Ex6


def times(A):
    """
    A - a list, e.g. ['dog', 'pencil', 'fence', 'dog', 'apple', 'dog', 'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']
    returns a dictionary showing the numbers of times each word occurs, e.g.
    {'dog': 5, 'pencil':2, 'fence': 1}
    """
    d = {}
    rm_dup = remove_dup(A)
    for i in rm_dup:
        d[i] = 0

    for i in A:
        d[i] += 1
    return d


t = ['dog', 'pencil', 'fence', 'dog', 'apple', 'dog',
     'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']
print(times(t))

# Ex7


def most_frequent(M):
    temp1 = []
    temp2 = []

    for i in M:
        temp1.append(M[i])

    for i in sorted(temp1, reverse=True)[:2]:
        for j in M:
            if i == M[j]:
                temp2.append(j)
    return temp2


ocurrs = {'dog': 5, 'pencil': 2, 'fence': 1}
print(most_frequent(ocurrs))
