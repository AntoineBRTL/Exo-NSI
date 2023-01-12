from Liste import Cellule

def listeTableau(list):
    # list to listeChainée

    cellule = None

    for i in range(len(list)):
        cellule = Cellule(list[-(i + 1)], cellule)

    return cellule

print(listeTableau([1, 5, 3, 6, 7]))