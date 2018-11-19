def f(a, b, c):
    """return the truth value of a <=> b and not c"""
    return a is b and not c

print(f(True, False, True))
