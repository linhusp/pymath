#1
def binary(n):
    """convert n to base 2"""
    b2 = ""

    if n == 0:
        return "0"
    
    while n != 0:
        b2 = str(n % 2) + b2
        n = int(n / 2)

    return int(b2)

print(binary(169))


#2
def gcd(a, b):
    """return greatest common divisor of a and b"""
    a = abs(a)
    b = abs(b)
    q = 0

    while b != 0:
        q = a % b
        a = b
        b = q

    return a

def lcm(a, b):
    """return least common mutiplier of a and b"""
    return int((a * b) / gcd(a, b))

print(lcm(12, 18))
