def recSyracuse(Un):
    if Un % 2 == 0:
        return Un / 2
    return 3 * Un + 1

def syracuseNonRecursive(Un):
    tab = []
    while Un > 1:
        Un = recSyracuse(Un)
        tab.append(Un)
    return tab

def syracuse(Un):
    print(Un)

    if(Un <= 1):
        return 0

    if Un % 2 == 0:
        return syracuse(Un/2)
    return 3 * syracuse(3 * Un + 1)
    