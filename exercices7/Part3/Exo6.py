def generateDoc(n):

    doc = "<a>"

    for i in range(n):
        doc += "<b>" + i + "</b>"

    doc += "</a>"

    f = open("docn.xml")
    f.write(doc)
    f.close()