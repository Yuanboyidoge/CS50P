import os.path
import sys
from PIL import Image,ImageOps

images = []
try:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    for im in sys.argv[1:]: 
        if im.endswith(".jpg") ==0 and im.endswith(".png") ==0 and im.endswith(".jpeg") ==0:
            sys.exit("Invalid input")
    # 判断后缀名是否一样
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")
    shirt=Image.open("shirt.png")

    im= Image.open(sys.argv[1]) 
    # 将before.jpg缩减成shirt的大小
    im = ImageOps.fit(im, shirt.size)
    # 把shirt粘贴在before.jpg上，im.paste(shirt, mask=shirt)？神奇的用法，可以去掉shirt以外的东西
    im.paste(shirt, shirt)
    im.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File does not exist")
