from xml.dom import minidom

with open("files/data.xml", "r", encoding="utf-8") as file:
    #   doc = minidom.parse(file)
    doc = minidom.parseString(file.read())
    root = doc.documentElement

    print(root.nodeName, "- id:", root.attributes["id"].nodeValue)

    for child in root.childNodes:
        if child.nodeType == minidom.Node.ELEMENT_NODE:
            for gchild in child.childNodes:
                if gchild.nodeType == minidom.Node.ELEMENT_NODE:
                    print(gchild.nodeName, ":", gchild.firstChild.nodeValue)
