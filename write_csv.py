import csv

data = [[1,"man",22],[2,"bear",33],[3,"shell",44]]

with open("files/mydata.csv","w",newline="")as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)