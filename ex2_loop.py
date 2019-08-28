#รับข้อมูลตัวเลขหลายๆตัวจากผู้ใ้ จนกว่าจะใส่ -1 ใส่ List
nums = int(input("Add Val to List >>"))
stop = 0
list =[]
list.append(nums)
while stop != 1:
    if nums == "-1" :
        stop = 1
    else :
        nums = input("Add Val to List >>")
        list.append(nums)
        print(list)
        stop = 0

max = 0
for ii in range(len(list)):
    if int(list[ii]) > max:
        max = int(list[ii])

print(max)
