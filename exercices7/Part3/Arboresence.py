class Node:
    def __init__(self, v, f):
        self.value = v
        self.childs = f

    def appendChild(self, c):
        self.childs.append(c)

    def display(self):
        display(self)

class Arborecence:
    def __init__(self):
        self.racine = Node()

    def display(self):
        display(self.racine)

def display(n:Node, s = ""):
    print(s + n.value)

    for i in range(len(n.childs)):
        display(n.childs[i], s + "  ")