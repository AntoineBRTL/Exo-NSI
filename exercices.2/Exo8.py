def cree():
    return []

def cle(d, k):
    for el in d:
        if k == el[0]:
            return True
    return False

def lit(d, k):
    for el in d:
        if k == el[0]:
            return el[1]
    return None

def ecrit(d, k, v):
    for i in range(len(d)):
        if(d[i][0] == k):
            d[i] = (k, v)
            return
    d.append((k, v))

dic = cree()
ecrit(dic, "test", "aa")
print(lit(dic, "test"))