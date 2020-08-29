vnds = sorted([i * 10**j for j in [3, 4, 5]
               for i in [1, 2, 5]], reverse=True)


def main():
    test = 10241000
    print(divide(test))


def divide(money):
    d = {}
    for vnd in vnds:
        if money >= vnd:
            d[vnd] = money // vnd
            money %= vnd
    return d


if __name__ == "__main__":
    main()
