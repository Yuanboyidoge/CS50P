import sys
import csv

hp=[]
try:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith(".csv") ==0 or sys.argv[2].endswith(".csv") ==0:
        sys.exit("Not a csv file")
    # 读文件，将文件放入hp字典中
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last,first=row["name"].strip("").split(", ")
            hp.append({"first": first, "last":last,"house": row["house"]})
    # 写文件，把hp文件写入另一csv
    with open(sys.argv[2],"w",newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writeheader()
        for row in hp:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
        
except FileNotFoundError:
    sys.exit("File does not exist")

    
