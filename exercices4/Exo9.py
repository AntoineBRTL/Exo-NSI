from Liste import Cellule
from Exo8 import triParInsertion

def listeN(n):
    # renvoie la liste des N premiers entier.
    if(n == 0):
        return None

    return triParInsertion(Cellule(n, listeN(n-1)))

print(listeN(8))