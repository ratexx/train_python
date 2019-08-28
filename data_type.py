name = ["Jim","JO","J"]
print(name[0])
print("J" in name)
name = ["Ant","Cat","Doggggg","Man","Bat"]
print(len(name))
print(name[-1])
for n in name:
        print(n)

for i in range(0,len(name)):
    print(i,name[i])

friend = "Man"
print("Cat in the list {}".format(friend in name) )


for n in name:
    if n == friend:
        isFound= True



for i in range(0,len(name)):
    if name[i] == friend:
        pos = i

print("pos val > {}".format(pos))
print(isFound)



#sort normal case
name.sort()
print(name)

#sort reverse case
name.sort(reverse=True)
print(name)


#sort KEy case
def my_sort(e):
    return len(e)


name.sort(reverse=True, key=my_sort)
print(name)