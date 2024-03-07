import sys
# 获取list长度
def getlen(my_list):
    total=len(my_list)
    for line in my_list:
        # 判断是不是注释或者空行
        if line.strip().startswith("#") or line.lstrip()=="":
            total-=1
    return total

inputlist=[]
try:
    if len(sys.argv)>2:
        raise ValueError
    elif len(sys.argv)==1:
        raise TypeError
    elif sys.argv[1].endswith(".py") ==0:
        raise NameError
    with open(sys.argv[1]) as file:
        for line in file:
            inputlist.append(line.rstrip())
        print(getlen(inputlist))
except ValueError:
    sys.exit("Too many command-line arguments")
except TypeError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
except NameError:
    sys.exit("Not a Python file")

