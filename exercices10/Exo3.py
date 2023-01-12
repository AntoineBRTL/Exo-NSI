def applique(function, list):
    return [function(list[i]) for i in range(len(list))]

majuscule = lambda lst : applique(lambda x : x.upper(), lst)

a = majuscule(["test"])
print(a)