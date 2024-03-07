import sys
import csv
from tabulate import tabulate

menu=[]
try:
    if len(sys.argv)>2:
        raise ValueError
    elif len(sys.argv)==1:
        raise TypeError
    elif sys.argv[1].endswith(".csv") ==0:
        raise NameError
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file,fieldnames=["pizza1","Small","Large"])
        for row in reader:
            menu.append({"pizza": row["pizza1"], "Small": row["Small"],"Large":row["Large"]})
    print(tabulate(menu,headers="firstrow",tablefmt="grid"))
    # 注意区别：headers="firstrow"，那么表头就是csv里的第一行
    # headers="keys"，表头是键名（"pizza","small","large"）
except ValueError:
    sys.exit("Too many command-line arguments")
except TypeError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
except NameError:
    sys.exit("Not a csv file")
