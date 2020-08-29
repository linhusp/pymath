test1 = '[what the fuck{lol fuck (ak()kk)}]'
test2 = '[what the fuck lol fuck ( {akkk)}]'
test3 = '[what the fuck (){a}'


def main():
    test(test1, check(test1))
    test(test2, check(test2))
    test(test3, check(test3))


def check(s):
    stack = []
    parentheses = {'(': ')', '[': ']', '{': '}'}
    open_p = '[{('
    close_p = ']})'
    for char in s:
        if char in open_p:
            stack.append(parentheses[char])
        elif char in close_p and stack.pop() != char:
            return False
    return not stack


def test(s, result):
    print('{} -> {}'.format(s, result))


if __name__ == "__main__":
    main()
