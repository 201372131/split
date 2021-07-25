#-*- coding = utf-8 -*-
#@Time : 2021/5/2 21:25
#@Author : 李家旺
#@File : demo1.py
#@Software : IntelliJ IDEA

# 第一行代码
#print("hello, world")
'''
多行注释


a = 10
print(a)
print("这是变量：",a)

print("------------------------")
age = 18
print("我的年龄是：%d"%age)
print("我的名字是: %s, 我的国籍是: %s"%("小张","中国"))

print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
print("hello ", end="")
print("world ", end="")
print("python ", end="\t")#换行

password = input("请输入密码")
print("您刚刚输入的密码是：",password)

a = "10"
print(type(a))

a = input("输入：")
print(type(a))


a = int("123")
print(type(a))
b = a + 199
print(b)


if False:
    print("True")
else:
    print("False")
print("aaa")

score = 87

if score >=90 and score <=100:
    print("考试成绩A")
else:
    if score >= 80 and score <90:
        print("成绩为B")
    print("考试成绩E")

xingBie = 1
danshen = 1
if xingBie == 1:
    print("男生")
    if danshen == 1:
        print("单身")
    else:
        print("不是单身")
else:
    print("女生")


import random #引入随机数库

a = random.randint(0,2) # 随机生成 0，1，2三个数字
print(a)
'''
a = input("请输入")
if a == 0:
    print("你输入的是剪刀")
elif a == 1:
    print("你输入的是石头")

print("你输入的是布")

import random
b = random.randint(0,2)
print("随机生成数字为",b)

if a == 0 :
    if b == 0:
        print("平手")
    if b == 1:
        print("你输了")
    if b == 2:
        print("你赢了")
elif a == 1:
    if b == 0:
        print("你赢了")
    if b == 1:
        print("平手")
    if b == 2:
        print("你输了")
else :
    if b == 0:
        print("你输了")
    if b == 1:
        print("你赢了")
    if b == 2:
        print("平手")





















