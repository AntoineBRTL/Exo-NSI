def applique(function, list):
    return [function(list[i]) for i in range(len(list))]

def mystere(lst):
    return applique(lambda x : x**2, lst)

a = mystere([1, 2, 3, 4, 5])
print(a)