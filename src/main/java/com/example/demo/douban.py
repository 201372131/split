#-*- coding = utf-8 -*-
#@Time : 2021/5/4 1:00
#@Author : 李家旺
#@File : douban.py
#@Software : IntelliJ IDEA

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # #1, 爬取网页
    datalist = getData(baseurl)
    # #3,保存数据
    savepath = ".\\豆瓣电影Top250.xls"
    # saveData(savepath)
    #askURL("https://movie.douban.com/top250")

findLink = re.compile(r'<a href="(.*？)">')   #创建正则表达式对象，表示规则

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        html = askURL(url) #保存获取到的网页源码
        # 2，逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_="item"):  #查找符合要求的字符串
            data = [] #保存一部电影所有信息
            item = str(item)
            print(item)
            link = re.findall(findLink, item)   #RE库通过正则表达式查找指定的字符串
            print(link)

    return datalist


#得到指定的一个URL的网页内容
def askURL(url):
    #模仿浏览器
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    request = urllib.request.Request(url, headers=head);
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e :
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

        print("出现异常了")
    return html




def saveData(savepath):
    #3,保存数据
    print("save")

if __name__ == "__main__":
    #调用函数
    main()


