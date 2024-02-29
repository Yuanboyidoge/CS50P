print("Amount Due: 50")
remain=50
while True:
    get=int(input("Insert Coin: "))
    if get==25 or get==10 or get==5:
        remain=remain-get
        if remain>0:
            print("Amount Due:",remain)
        elif remain<0:
            print("Change Owed:",-remain)
            break
    else:
        print("Amount Due:",remain)
    if remain==0:
        print("Change Owed:",remain)
        break
