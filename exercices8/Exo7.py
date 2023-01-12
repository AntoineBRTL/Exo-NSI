def deplace(a, b, c, k):
    if k == 1:
        print("deplace " + str(a) + " vers "  + str(b))
    else:
        deplace(a, c, b, k - 1)
        deplace(a, b, c, 1)
        deplace(c, b, b, k - 1)

def hanoi(n):
    if n <= 0:
        raise IndexError("n must be > 0")
    deplace(1, 3, 2, n)

hanoi(4)