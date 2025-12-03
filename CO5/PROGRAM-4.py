import csv
with open('student.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("Place")
    print("----")
    for i in data:
        print(i['Place'])
        
