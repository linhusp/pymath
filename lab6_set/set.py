def intersection(set1, set2):
    temp = []
    for i in set1:
        if i in set2:
            temp.append(i)
    return temp


def difference(set1, set2):
    temp = []
    for i in set1:
        if i not in set2:
            temp.append(i)
    return temp


def is_subset(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True


def size(set1):
    count = 0
    for i in range(len(set1)):
        if set1[i] not in set1[i+1:]:
            count += 1
    return count


ls = [1, 2, 3, 4, 5, 6, 5, 1]
ls2 = [1, 2, 3, 4, 5, 6, 5, 1]

# print(size(ls))


def equal_sets(set1, set2):
    return is_subset(set1, set2) and is_subset(set2, set1)

# print(equal_sets(ls, ls2))

# 1


def rm_duplicates(ls):
    temp = []
    for i in range(len(ls)):
        if ls[i] not in ls[i+1:]:
            temp.append(ls[i])
    return temp


dup_ls = [1, 4, 5, 3, 6, 7, 5, 3, 1, 9, 3, 3, 4, 2]
print(rm_duplicates(dup_ls))


def rm_bad_users(users, bad_users):
    return difference(users, bad_users)


users = set(['tom', 'pam', 'sasha', 'jj', 'que', 'jeff'])
bad = set(['jeff', 'sasha'])

# print(rm_bad_users(users, bad))


def map_days(day, days):
    days = {
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6,
        "sun": 7
    }
    for i in days:
        if day == i:
            return days[i]


# print(map_days("sun", days))


def reverse_map_days(num, days):
    for i in days:
        if map_days(i, days) == num:
            return i

# print(reverse_map_days(7, days))


various_ls = ['dog', 'pencil', 'fence', 'dog', 'apple',
              'dog', 'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']


def time_occurs(ls):
    d = {}

    for i in rm_duplicates(ls):
        d[i] = 0

    for i in ls:
        d[i] += 1

    return d


print(time_occurs(various_ls))


def freequently_items(my_dict):
    return sorted(time_occurs(my_dict), reverse=True)[:2]


print(freequently_items(various_ls))
