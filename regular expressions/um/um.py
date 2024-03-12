import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    i=0
    if matches:=re.findall(r"\b(um)\b",s,re.IGNORECASE):
        i=len(matches)
        return i
    else:
        return 0


if __name__ == "__main__":
    main()