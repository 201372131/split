#-*- coding = utf-8 -*-
#@Time : 2021/5/3 23:52
#@Author : 李家旺
#@File : demo3.py
#@Software : IntelliJ IDEA

try:
    print("-------test-----1")
    f = open("123.txt","r")
    print("-------test-----2")
except IOError:
    print("报错了")
    pass