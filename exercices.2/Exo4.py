def creer():
    return []

def contient(t, x):
    return x in t

def ajoute(t, x):
    t.append(x)

def uninon(t1, t2):
    tab = list(t1)

    for x in t2:
        if x not in tab:
            tab.append(x)
        
    return tab

def intersection(t1, t2):
    tab = []

    for x in t2:
        if x in t1:
            if x not in tab:
                tab.append(x)
    
    return tab
    return [x for x in s1 if x in s2]