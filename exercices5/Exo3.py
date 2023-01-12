from Exo2 import Pile
import operator

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul }

def calculatricePolonaise(string):
    pile = Pile()

    array = string.split(" ")

    for e in array:
        # on regarde si c'est un nb entier
        if e.isdigit():
            pile.empiler(int(e))
        #sinon c'est un operateur
        else:
            if(len(pile) == 0):
                raise Exception("Operateur avant 1er entier")
            
            x = pile.depiler()
            y = pile.depiler()

            pile.empiler(ops[e](x, y))

    if len(pile) > 1:
        return None

    return pile.depiler()

#print(calculatricePolonaise("1 2 3 * + 4 *"))