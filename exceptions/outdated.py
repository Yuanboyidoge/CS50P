month={
    "January":"1",
    "February":"2",
    "March":"3",
    "April":"4",
    "May":"5",
    "June":"6",
    "July":"7",
    "August":"8",
    "September":"9",
    "October":"10",
    "November":"11",
    "December":"12"
}

# try & exception 可以比较方便排除指定成功格式外的全部格式
while True:
    try:
        gets=input("Date: ")
        if "/" in gets:
            m,d,y=gets.split("/")
            m=int(m)
            y=int(y)
            d=int(d)
            if 0<m<=12 and 0<d<=31:
                print(f"{y}-{m}-{d}")
                break
            else:
                raise ValueError
        elif "," in gets:
            m1,d0,y1=gets.split(" ")
            if m1 in month:
                m1=int(month[m1])
            else:
                raise ValueError
            y1=int(y1)
            d1=int(d0.split(",")[0])
            if 0<d1<=31:
                print(f"{y1}-{m1}-{d1}")
                break
            else:
                raise ValueError
            
    except ValueError:
        pass
