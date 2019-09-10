import math


def main():
    limit = 100
    s1 = sum(i for i in range(1, limit + 1))
    print(s1)

    s2 = sum(i for i in range(2, limit + 1, 2))
    print(s2)

    odd_ls = [i for i in range(1, 999, 2)
              if i // 100 % 2 != 0
              and i % 100 // 10 % 2 != 0
              and i % 10 % 2 != 0]
    print(odd_ls)

    star(4)

    str_ = 'toi di choi'
    print(reverse_str(str_))

    print(count_vowels(str_))

    print(count_digits(69))


def star(len_):
    for i in range(0, len_):
        print(' '*(len_ - i - 1) + '*'*(i + 1) + '*'*i)


def reverse_str(str_):
    return ' '.join(str_.split(' ')[::-1])


def count_vowels(str_):
    return sum(1 for c in str_.lower() if c in 'aeiou')


def count_digits(num):
    return math.log(num) + 1


if __name__ == '__main__':
    main()
