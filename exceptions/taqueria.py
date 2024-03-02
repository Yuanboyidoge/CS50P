# enables a user to place an order,prompting them for items, one per line, 
# until the user inputs control-d (which is a common way of ending one’s input to a program). 
# After each inputted item, display the total cost of all items inputted thus far, 
# prefixed with a dollar sign ($) and formatted to two decimal places.
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.

menu={ 
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price=0
while True:
    # item=input不能放在try外，否则找不到EOF
    try:
        # 首字母大写
        item=input("Item: ").title()
        # 判断item是否在menu中，不在则pass
        if item in menu:
            price=price+menu[item]
            print(f"Total: ${price:.2f}")
    except EOFError:
        print()
        #EOF是退出循环不是继续循环
        break