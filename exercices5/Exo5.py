from Exo4 import Pile

def chaineBienParenthesee(string):
    pile = Pile()

    for element in string:
        if(element == "("):
            pile.empiler("(")

        if(element == ")"):
            if(pile.depiler() != "("):
                return False

        if(element == "["):
            pile.empiler("[")

        if(element == "]"):
            if(pile.depiler() != "["):
                return False

    return len(pile) == 0

#print(chaineBienParenthesee("()[]"))