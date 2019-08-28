dict = {"Ant-Man":"Marvel","Batman":"DC"}
print(dict)
print(dict.values())
print(dict.keys())
print(dict.items())

person ={"John":[30,"Gamer"] ,"Man":[30,"Programmer"],"Zin":[30,"AIS"]}
print(person)
print(person["John"])
print(person["Zin"])
print(person["Zin"][0])

for item in person:
    print("Name :{}  Work :{}".format(person[item][0],person[item][1]))

nnn = list(person.keys())
nnn.sort(reverse=True)
print(nnn)