getin=input("Input:")
print("Output:",end="")#end=""保证不换行
for short in getin:
    if short.lower()=="a" or short.lower()=="e" or short.lower()=="i" or short.lower()=="u" or short.lower()=="o":
        print("",end="")
    else:
        print(short,end="")