# def main():
#     time=input("What time is it? ")
#     z=convert(time)
#     if 7<=z<=8:
#         print("breakfast time")
#     elif 12<=z<=13:
#         print("lunch time")
#     elif 18<=z<=19:
#         print("dinner time")
#     else :
#         return 0


# def convert(tim):
#     x=int(tim.split(':')[0])
#     y=int(tim.split(':')[1])
#     t=x+round(y/60,2)
#     return t
    

# if __name__ == "__main__":
#     main()

# 进阶版
def main():
    z=convert(input("What time is it? ").strip().lower())
    if 7<=z<=8:
        print("breakfast time")
    elif 12<=z<=13:
        print("lunch time")
    elif 18<=z<=19:
        print("dinner time")
    else :
        return 0


def convert(tim):
    x=int(tim.split(':')[0])
    y=int(tim.split(':')[1])
    t=x+round(y/60,2)
    return t


if __name__ == "__main__":
    main()