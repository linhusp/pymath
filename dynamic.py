def main():
    # print(fib(10))
    limit = 500
    print(', '.join(str(fib(i)) for i in range(limit + 1)))
    # print(', '.join(str(fib_re(i)) for i in range(limit + 1)))

    # print(lis([5, 8, 3, 7, 2, 4, 6, 9]))


def fib(n):
    fibs = [0, 1]
    for i in range(n):
        fibs[(i - 1) % 2] += fibs[i % 2]
    return fibs[n % 2]


def lis(l):
    is_ = [0 for _ in l]
    is_[-1] = 1
    for i in range(len(l) - 2, -1, -1):
        max_ = 0
        for j in range(i + 1, len(l)):
            if l[j] > l[i] and is_[j] > max_:
                max_ = is_[j]
                is_[i] = max_ + 1

    r = []
    for i in range(len(l)):
        if is_[i] == max(is_):
            t = is_[i]
            r1 = []
            for j in range(i, len(l)):
                if is_[j] == t:
                    r1.append(l[j])
                    t -= 1
            r.append(r1)

    return r


if __name__ == '__main__':
    main()
