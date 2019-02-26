def fibo(n):
    return _fibo(n)[0]

def _fibo(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fibo(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        return (d, c + d)  

s = 0
for i in range(2, 100):
    s += fibo(i) / (fibo(i - 1) * fibo(i + 1))
    print(s)
