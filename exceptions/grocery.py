
# 申明一个dic
item={}
while True:
    # 这个dic的键是items_name,值是count
    try:
        # 这样结合后面的就将用户输入放入了dic中
        item_name=input().upper()
    except EOFError:
        print()
        break
    if item_name in item:
        item[item_name] += 1
    else:
        item[item_name]=1

# 对字典排序，sorted(item.items())返回键值对
for item_name,count in sorted(item.items()):
    print(f"{count} {item_name}")