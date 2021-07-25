#-*- coding = utf-8 -*-
#@Time : 2021/5/2 23:09
#@Author : 李家旺
#@File : demo4.py
#@Software : IntelliJ IDEA

# for循环例子

'''
for i in  range(5):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -101, -30):
    print(i)


name = "chengdu"
for x in name:
    #print(x)
    print(x, end="\t")

a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i,a[i])


# while
i = 0
while i < 5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i += 1

# 1=100求和
i = 0
j = 0

while i <= 100:
    j = j + i
    i += 1
print(j)

count = 0
while count<5:
    print(count,"小于5")
    count +=1
else:
    print(count,"大于或等于5")


i = 0
while i<10:
    i = i+1
    print("-"*30)
    if i == 5:
        break
    print(i)

i = 0
while i<10:
    i = i+1
    print("-"*30)
    if i == 5:
        continue
    print(i)

# 九九乘法表

a = 1
while a < 10:
    for i in range(1, a+1, 1):
        print(a,"*",i, end=" ")
        i =i+1
    print()
    a =a+1


#字符串
word = '字符串'
word2 = "双引号"
word3 = """
        段落和换行
        换行
"""
print(word)
print(word2)
print(word3)

myStr = "I'm a student"
print(myStr)


str = "chengdu"
print(str)
print(str[0:6])
print(str[0])
print(str[0:6:2])

str = "chengdu"
print(str[5:]) # 显示5个之后的字符
print(str[:5]) # 显示前面5个字符

print(str + ", 你好")
print(str * 3)
print("hello\nchengdu") #换行
print(r"hello\nchengdu") # 换行失效


# 列表
#nameList = [] #定义列表
name = ["小李", "小王", "小丽"]
print(name[0])
print(name[1])
print(name[2])

name2 = [1, "str"]
print(name2[0])
print(name2[1])
print(type(name2[0]))
print(type(name2[1]))

for n in name2:
    print(n)

print(len(name2)) #列表长度

length = len(name2)
i = 0
while i < length:
    print(name2[i])
    i += 1


#增加
nameList = ["小李", "小王", "小丽"]

print("-----增加前 名单列表的数据-----")
for name in nameList:
    print(name)

nametemp = input("请输入添加的名字")
nameList.append(nametemp) # 末尾增加元素
print("-----增加后 名单列表的数据-----")
for name in nameList:
    print(name)

#增加
a = [1,2,3]
b = [3,4]
a.append(b) # 将列表当成一个元素增加到列表中
print(a)

a.extend(b) # 将b列表中的元素追加到列表中
print(a)

a = [0,1,2,]
a.insert(1,3) # 1：下标 3：元素
print(a)


# 删
movie = ["加勒比海盗", "骇客帝国", "第一滴血", "速度与激情", "第一滴血"]
print("-----增加前 电影列表的数据-----")
for name in movie:
    print(name)

#del movie[2] # 指定位置删除
#movie.pop() # 弹出末尾一个元素
movie.remove("第一滴血") # 直接删除指定的元素 如果有重复数据删除第一个元素

print("-----增加后 电影列表的数据-----")
for name in movie:
    print(name)

# 改
nameList = ["小李", "小王", "小丽"]

print("-----增加前 名单列表的数据-----")
for name in nameList:
    print(name)
nameList[1] = "小红" #修改指定下标的元素

print("-----增加后 名单列表的数据-----")
for name in nameList:
    print(name)


#查 [in    not in]
nameList = ["小李", "小王", "小丽"]

findName = input("输入要查询的学生")
if findName in nameList:
    print("找到了")
else:
    print("没找到")


list = ["a", "b", "c", "a", "b"]
list.index("a", 1, 4) # 下标1-4有没有a出现 返回找到元素的下标
print(list.index("a", 1, 4))

#print(list.index("a", 1, 3)) # 范围区间左闭右开，找不到报错

print(list.count("a")) #统计元素出现的次数


#排序和反转
a = [1,4,2,3]
print(a)
a.reverse() # 将列表所有元素反转
print(a)

a.sort() #升序
print(a)

a.sort(reverse=True) #降序
print(a)


#嵌套
#schoolNames = [[], [], []] #有三个元素的空列表，每个元素都是一个空列表
schoolNames = [["北京大学", "清华大学"], ["南开大学", "天津师范", "山东大学"], ["山东大学", "青岛大学", "中国海洋"]]
print(schoolNames[0][0])


import random
offices = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

print(offices)

i = 1
for office in offices:
    print("办公室%d的人数为： %d"%(i,len(office)))
    i +=1
    for name in office:
        print("%s"%name, end="\t")
    print("\n")
    print("-"*20)


#作业
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499],["Coffee", 31],["Book", 60], ["Nike", 699]]
i = 0
for product in products:
    length = len(product)
    print(i ,end=" ")
    for p in range(0, length):
        print(product[p], end=" ")
    i +=1
    print()

q = ["q"]
buyCar = []
while True:
    want = input("想要哪个商品？")
    print(want)
    if q in want: # 判断
        print("购物车的商品", buyCar)
        print("退出")
        break
    else:
        buy = products[want]
        buyCar.append(buy)
        print("选择的商品", buyCar)
'''

#元组
'''
tup1 = () # 创建空的元组
tup2 = (50) # 不是元组 是个整形
tup3 = (50,)
tup4 = (50,60,70)

print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))


tup1 = ("abc", "def", 2000, 2020,333,444,555,666) #元素可以是不同类型
print(tup1[0])
print(tup1[-1]) # 去最后一个元素
print(tup1[1:5]) # 左闭右开


# 增
tup1 = (12,34,56)
#tup1[0] = 100 # 不允许修改
tup2 = ("abc","xyz")
tup = tup1 + tup2 # 连接
print(tup)

#删
del tup1   #删除了整个元组tup1, 而不是里面的值
print(tup1)


# 字段

info = {"name":"吴彦祖", "age":18} # 字典定义

print(info["name"]) #访问
print(info["age"])  #key不存在会报错

print(info.get("gender")) #key不存在返回None

print(info.get("gender", "m")) # 如果没找到返回默认值
print(info.get("age", 22))
'''

info = {"id":1, "name":"吴彦祖", "age":18} # 字典定义
#增
#newID = input("请输入id")
#info["id"] = newID
#print(info)

#删
# print("删除前:%s"%info["name"])
# #del info["name"] # 删除键值对
# print("删除后:%s"%info["name"])
#
# del info # 删除变量
# print(info)

# print("清空前:%s"%info)
# info.clear()
# print("清空后:%s"%info)

#修改
print("修改前:%s"%info)
info["age"] = 20
print(info)


#查
print(info.keys()) # 得到所有键
print(info.values()) # 得到所有的值

print(info.items()) # 得到所有的键值对


#遍历所有的键
for key in info.keys():
    print(key)

#遍历所有的值
for value in info.values():
    print(value)

#遍历所有的键值对
for key, value in info.items():
    print("key=%s, value%s"%(key,value))


#使用枚举函数同时拿到列表的下标和元素
list  = ["a", "b","c","d"]
print(enumerate(list))
for i,x in enumerate(list):
    print(i+1,x) # 打印下标和值



