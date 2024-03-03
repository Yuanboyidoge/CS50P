import json
import requests
import sys

while 1:
    try:
        num=float(sys.argv[1])
        if len(sys.argv)!=2:
            raise requests.RequestException
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Missing command-line argument ")

    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json?limit=1")
    o=response.json()
    # 嵌套字典取值
    # 注意，根据url取["bpi"]["USD"]["rate_float"]得到的是数字，["bpi"]["USD"]["rate"]得到的是字符串
    rate=o["bpi"]["USD"]["rate_float"]
    print(f"${rate*num:,.4f}")
    # 记得break，不然将一直循环获取rate，打印结果
    break
