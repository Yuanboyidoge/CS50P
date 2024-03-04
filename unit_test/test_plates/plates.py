def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and 2<=len(s)<=6:
        for ch in s[2:]:
            #排除不是字母或者数字的
            if ch.isalpha()==False and ch.isdigit()==False:
                return False
        for ch in s[2:]:
            #字母的ok
            if ch.isdigit():
                if ch=="0":
                    return False
                else:
                    #循环到第一位数字，无论怎样，都return，不再继续遍历ch
                    first_number_position=s.index(ch)
                    #s[i:j]切片
                    for i in s[first_number_position:]:
                        if i.isalpha():
                            return False
                    return True
        #全是字母的情况
        else:
            return True
    #排除前两位不是字母的和长度不对的
    else:
        return False

if __name__ == "__main__":
    main()