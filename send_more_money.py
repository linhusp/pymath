import time
from itertools import permutations

N_OUTPUT = 8
MIN_RANGE = 10**(N_OUTPUT - 1) - 1
MAX_RANGE = 10**N_OUTPUT - 1


def main():
    outputs = solve()
    print(outputs)


def solve():
    for digits_tuple in permutations(range(10), N_OUTPUT):
        if is_valid(digits_tuple):
            peek(digits_tuple)
            return digits_tuple
    return None


def is_valid(digits_tuple):
    if is_1st_digit_zero(digits_tuple):
        return False
    return has_valid_condition(digits_tuple)


def peek(digits):
    print('%s + %s = %s' %
          (digits2number(SEND(digits)),
           digits2number(MORE(digits)),
           digits2number(MONEY(digits))))


def digits2number(digits):
    len_digits = len(digits)
    return sum(digits[i] * 10**(len_digits-i-1) for i in range(len_digits))


def is_1st_digit_zero(digits):
    return digits[0] == 0


def has_valid_condition(digits):
    send = SEND(digits)
    more = MORE(digits)
    money = MONEY(digits)

    if is_1st_digit_zero(send) \
            or is_1st_digit_zero(more) \
            or is_1st_digit_zero(money):
        return False

    return digits2number(send) + digits2number(more) == digits2number(money)


def SEND(digits):
    return (digits[0], digits[1], digits[2], digits[3])


def MORE(digits):
    return (digits[4], digits[5], digits[6], digits[1])


def MONEY(digits):
    return (digits[4], digits[5], digits[2], digits[1], digits[7])


def test():
    # arr = [i for i in range(10000000, 100000000) if len(set(list(str(i)))) >= 3]
    # arr = [
    #     a*10000000 + b*1000000 + c*100000 + d*10000 + e*1000 + f*100 + g*10 + h
    #     for a, b, c, d, e, f, g, h in permutations(range(10), 8)
    #     if a != 0
    # ]
    arr = [
        # sum(e * 10**(8-i-1) for i, e in enumerate(a))
        # sum([a[i] * 10**(8-i-1) for i in range(N_OUTPUT)])
        a
        for a in permutations(range(10), 8)
        # if a[0] != 0
        if a[0] != 0 and \
            sum([a[i] * 10**(8-i-1) for i in range(N_OUTPUT)]) == 95671082
    ]
    # print(arr[-1])
    print(arr)


if __name__ == "__main__":
    t = time.time()
    main()
    # test()
    print('finished in', end=' ')
    print(time.time() - t, end=' ')
    print('secs')
