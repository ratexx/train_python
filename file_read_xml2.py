from xml.dom import minidom

with open("files/data.xml", "r", encoding="utf-8") as file:
    #   doc = minidom.parse(file)
    doc = minidom.parseString(file.read())
    root = doc.getElementsByTagName("receipt")[0]

    print(root.nodeName, "- id:", root.attributes["id"].nodeValue)

    for item in root.getElementsByTagName("item"):
        print(
            item.getElementsByTagName("name")[0].firstChild.nodeValue,
            ":",
            item.getElementsByTagName("price")[0].firstChild.nodeValue)
