import inflect

names=[]
# 注意inflect的用法，这里应该是p
p=inflect.engine()

while True:
    try:
        # append函数在list最后增加新元素
        names.append(input("Name:"))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        #EOF是退出循环不是继续循环
        break