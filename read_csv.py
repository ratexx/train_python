import csv
file = open("files/data.csv","r",encoding="tis620")
reader = csv.reader(file,delimiter=",")

for row in reader:
    for col in row:
        print(col)
    print(row)
file.close()
print(reader)