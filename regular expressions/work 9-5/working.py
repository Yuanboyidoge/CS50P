import re
import sys


def main():
    # print(convert("9 AM to 5 PM"))
    print(convert(input("Hours: ")))


def convert(s):
    if matches:=re.search(r"(\d|1[0-2]):?([0-5]\d)? (AM|PM) to (\d|1[0-2]):?([0-5]\d)? (AM|PM)",s):
        # print(matches.groups())
        # 注意arr[]从arr[0]开始,而group()从group(1)开始
        arr=[]
        for i in matches.groups():
            arr.append(i)
        if arr[1]==None:
            arr[1]=0
        if arr[4]==None:
            arr[4]=0
        # print(arr)
        # 注意map时，不用matches.group()是因为其中可能有None，会导致不能强转int类型
        arr[0],arr[1],arr[3],arr[4]=map(int,[arr[0],arr[1],arr[3],arr[4]])
         
        if arr[2]=="PM":
            arr[0]+=12
        if arr[5]=="PM":
            arr[3]+=12

        return f"{arr[0]:02}:{arr[1]:02} to {arr[3]:02}:{arr[4]:02}"

    else:
        raise ValueError


...


if __name__ == "__main__":
    main()