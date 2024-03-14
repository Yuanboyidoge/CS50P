from datetime import date
import inflect
import sys

p=inflect.engine()


def main():
    print(p.number_to_words(getdate(input("Date of Birth:")),andword="").capitalize(),"minutes")

def getdate(s):
    try:
        # 转化为规范格式
        birth=date.fromisoformat(s)
        # date.today（）获得今天日期，记住最后返回分钟
        return (date.today()-birth).days*24*60
    except ValueError:
        # 为了退出无异常，选择try&except
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()