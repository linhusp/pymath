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

len_ = 3
for i in range(0, len_):
    print(' '*(len_ - i - 1) + '*'*(i + 1) + '*'*i)
