import random
# 这层循环用来输入正确的level
while 1:
    try:
        level=int(input("Level:"))
        if level<1:
            raise ValueError 
        break
    except ValueError:
        pass
ans=random.randint(1,level)
# 这层循环用来猜数字，也应该是正确的数字
while 1:
    try:
        guess=int(input("Guess:"))
        if guess<ans:
            print("Too small!")
        elif guess>ans:
            print("Too large!")
        elif guess==ans:
            print("Just right!")
            # 退出全部循环
            break
    except ValueError:
        pass


