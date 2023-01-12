import xml.dom.minidom as dom

def stat_xml(d:dom.Node):

    t = (int(d.nodeType == dom.Node.ELEMENT_NODE), len(d.attributes), int(d.nodeType == dom.Node.TEXT_NODE))  

    for i in range(len(d.childNodes)):
        t2 = stat_xml(d.childNodes[i])
        t[0] += t2[0]
        t[1] += t2[1]
        t[2] += t2[2]

    return t

