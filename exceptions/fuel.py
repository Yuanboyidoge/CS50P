# implement a program that prompts the user for a fraction, formatted as X/Y, 
# wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
# instead prompt the user again. (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def getxy():
    while True:
        try:
            x,y=input("Fraction: ").split("/")
            x=int(x)
            y=int(y)
            if y==0:
                # 将被除数为0的异常主动触发
                raise ValueError
            # 只有正常的数才能返回
            if 0<= x/y <=1:
                return(x/y)
        except ValueError:
            pass


def main():
    res=round(getxy()*100)
    if res<=1:
        print("E")
    elif res>=99:
        print("F")
    else:
        print(f"{res:}%")

main()