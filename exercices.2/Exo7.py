def tranche(t, i, j):
    k = min([i], [j])

    tab = []
    for n in range(abs(j - i)):
        tab.append(t[k + n])
    
    return tab

def concatenation(t1, t2):
    tab = []

    for el in t1:
        tab.append(el)

    for el in t2:
        tab.append(el)

    return tab