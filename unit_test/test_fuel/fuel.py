def main():
    print(gauge(convert(input("Input:"))))

def convert(fraction):
    while True:
        try:
            x,y=fraction.split("/")
            x=int(x)
            y=int(y)
            if y==0:
                # 将被除数为0的异常主动触发
                raise ValueError
            # 只有正常的数才能返回
            if 0<= x/y <=1:
                res=round(100*x/y)
                return res
        except ValueError:
            pass

def gauge(res):
    if res<=1:
        return "E"
    elif res>=99:
        return "F"
    else:
        return f"{res:}%"


if __name__ == "__main__":
    main()