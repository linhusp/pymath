import sys
print('\n'.join([' ' * (int(sys.argv[1]) - i - 1) + '*' *
                 2 * i + '*' for i in range(int(sys.argv[1]))]))
