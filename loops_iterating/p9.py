# Problem 9

def fac(n):
    fact = 1
    n_range = range(1, n + 1)
    for i in n_range:
        fact *= i

    return fact

f = fac(5)
print(f)
