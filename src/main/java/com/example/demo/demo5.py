#-*- coding = utf-8 -*-
#@Time : 2021/5/3 20:48
#@Author : 李家旺
#@File : demo5.py
#@Software : IntelliJ IDEA

# 函数
'''
def printinfo():
    print("----------")
    print("       人生苦短， 我用python    ")
    print("---------")

#函数的调用
printinfo()


#带参数函数
def add2Num(a, b):
    c = a + b
    print(c)

add2Num(11,22)


#带返回值函数
def add2Num(a, b):
    return a + b

result = add2Num(11,22)
print(result)


#返回多个值的函数

def divid(a, b):
    shang = a//b
    yushu = a%b
    return shang, yushu  # 多个返回值用逗号分开

sh,yu = divid(5,2)
print("商： %d, 余数：%d"%(sh,yu))
'''

def printLine():
    print("-------------")
printLine()

def line(a):
    print("-"*a)
line(8)

def add3Num(a,b,c):
    print(a+b+c)
    return a+b+c
count = add3Num(1,2,3)
print(count)

def avg(a,b,c):
    # total = add3Num(a,b,c)
    # aa = total/3.0
    # return aa

 avg(4,5,6)
