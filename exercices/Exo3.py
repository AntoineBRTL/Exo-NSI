def serie(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    if n >= 2:
        return 3 * serie(n - 1, a, b) + 2 * serie(n - 2, a, b) + 5