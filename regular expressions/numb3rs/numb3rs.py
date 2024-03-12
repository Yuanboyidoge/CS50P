import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # https://blog.csdn.net/shanf7921/article/details/108456279 (0-255匹配)
    if matches:=re.match(r'(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])',ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()