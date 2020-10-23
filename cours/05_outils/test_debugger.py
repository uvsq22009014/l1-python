def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(fact(9))
print(fact(10))
