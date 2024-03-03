# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
import sys
import random
from pyfiglet import Figlet

font_list=Figlet().getFonts()
try:
    if len(sys.argv)==3 :
        # 字体需要在字体表中，sys.argv[1]也应该是'-f'或'--font'
        if sys.argv[2] in font_list and sys.argv[1] in ['-f','--font']:
            getin=input("Input: ")
            print("Output:")
            f=Figlet(font=sys.argv[2])
            print(f.renderText(getin))
        else:
            raise ValueError
    elif len(sys.argv)==1:
        getin=input("Input: ")
        print("Output:")
        # 随机字体
        f=Figlet(font=random.choice(font_list))
        print(f.renderText(getin))
    else:
        raise ValueError
except ValueError:
    # 退出并提示'Invalid usage'
    sys.exit('Invalid usage')