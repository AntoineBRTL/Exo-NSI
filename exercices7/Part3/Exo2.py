from Arboresence import Node
import os

def repertoires(s:str):
    r = s.split("/")
    name = r[len(r) - 1]
    n = Node(name, [])

    if os.path.isdir(s):
        childDir = os.listdir(s)
        for cd in childDir:
            cn = repertoires(os.path.join(s, cd))
            n.appendChild(cn)
    return n

n = repertoires("/home/tnsi-eleve1/Documents/Terminal/ExercicesTerminale-main/")
n.display()