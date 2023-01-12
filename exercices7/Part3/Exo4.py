import xml.dom.minidom as dom

def compte_balise(node:dom.Node, name):

    n = 0

    if node.nodeName == name:
        n += 1

    for i in range(len(node.childNodes)):
        n += compte_balise(node.childNodes[i], name)

    return n