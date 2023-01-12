def applique(function, list):
    res = []
    for i in range(len(list)):
        res.append(function(list[i]))
    return res

def applique2(function, list):
    return [function(list[i]) for i in range(len(list))]