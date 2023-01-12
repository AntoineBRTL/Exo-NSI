def nbChiffre(x):
    if x <= 9:
        return 1
    return 1 + nbChiffre(x / 10)