get_name=input("camelCase: ").strip()
print("snake_case:",end="")
for a in get_name:
    if a.islower():
        print(a,end="")#保证输出不换行
    if a.isupper():
        print("_"+a.lower(),end="")#用“+”而不是“，”，因为避免空格

