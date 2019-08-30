import json

with open("files/data.json", "r", encoding="utf-8") as file:
    #   obj = json.load(file)
    obj = json.loads(file.read())

    for font in obj["font"]:
        print(font["color"], font["lang"])
