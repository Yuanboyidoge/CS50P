def main():
    get=input("Input:")
    print("Output:",end="")#end=""保证不换行
    shorten(get)

def shorten(word):
    res=[]
    for short in word:
        if short.lower() in ['a','e','i','o','u']:
            continue
        else:
            res.append(short)
    # 注意要有返回值哈
    # join拼接字符串
    return "".join(res)

if __name__ == "__main__":
    main()