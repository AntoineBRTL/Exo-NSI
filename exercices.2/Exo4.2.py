def cree():
    return [0] * 6

def contient(s, x):
    iEntier = x // 64
    bit = x % 64
    return (s[iEntier] & (1 << bit) != 0)

def ajoute(s, x):
    iEntier = x // 64
    bit = x % 64
    s[iEntier] = s[iEntier] | (1 << bit)

def enumere(s):
    tab = []

    for entier in s:
        for bit in range(64):
            if entier & (1 << bit) != 0:
                tab.append(entier * 64 + bit)

    return tab

def contientDoublon(t):
    s = [0] * 6
    for x in t:
        if s[x // 64] & (1 << (x % 64)) != 0:
            return True
        s[x // 64] = s[x // 64] | (1 << (x % 64))
    return False

def uninon(t1, t2):
    tab = []

    for n in range(6):
        tab.append(t1[n] | t2[n])

    return tab
    return [t1[i] | t2[i] for i in range(6)]

def intersection(t1, t2):
    tab = []

    for n in range(6):
        tab.append(t1[n] & t2[n])

    return tab
    return [t1[i] & t2[i] for i in range(6)]
