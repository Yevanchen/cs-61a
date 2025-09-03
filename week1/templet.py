def sum_naturals(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k**3, k + 1
    return total


def sum_pi(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 1/k, k + 1
    return total

def identity(k):
    return k

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

test = sum_naturals(10)
print(test)

test = sum_cubes(10)
print(test)

test = identity(10)
print(test)


