from Exo3 import Pile

def parentheseCorrespondante(string, index):
    pile = Pile()

    for i in range(len(string)):
        element = string[i]

        if(i == index):
            return pile.depiler()

        if(element == "("):
            pile.empiler(i)

        if(element == ")"):
            pile.depiler()

#print(parentheseCorrespondante("(4 * 2 (3 + 18))", 15))
