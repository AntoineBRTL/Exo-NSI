def C(n, p):
    if p > n:
        return 0
    if p == 0 or n == p:
        return 1
    return C(n - 1, p - 1) + C(n - 1, p)

def TriangleDePascal(nmax):
    for x in range(nmax):
        for y in range(nmax):
            print(C(x, y), end="")
        print("\n", end="")