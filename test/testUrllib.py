#-*- coding = utf-8 -*-
#@Time : 2021/5/4 12:14
#@Author : 李家旺
#@File : testUrllib.py
#@Software : IntelliJ IDEA

import urllib.request


#get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

#post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode("utf-8"))


#超时了
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("超时了")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server"))
# print(response.status)


#伪装浏览器
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))