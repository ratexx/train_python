import json

products = [
    {'name': 'หมู', 'price': 120},
    {'name': 'ไก่', 'price': 150}
]

with open("files/data2.json", "w") as file:
    string = json.dumps(products, indent=4, ensure_ascii=False)

    file.write(string)
