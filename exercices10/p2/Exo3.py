def calcule(f, a, x):
    r = f(x[0])
    for i in range(1, len(x)):
        r = a(r, f(x[i]))
    return r

a = calcule(lambda x: x, lambda x, y: str(x) + ", " + str(y), [1, 2, 3, 4])
print(a)

