#-*- coding = utf-8 -*-
#@Time : 2021/5/3 23:33
#@Author : 李家旺
#@File : demo6.py
#@Software : IntelliJ IDEA

#文件操作

'''
f = open("test.txt", "w") # 打开文件，没有就新建（w)
f.write("hello word i am here") #将字符串写入文件中

f.close() # 关闭文件

f = open("test.txt","r")
content = f.read(5)
print(content)
print(f.read(5))
f.close()


f = open("test.txt", "r")
content = f.readlines() # 读取全部文件为列表

#print(content)
i = 1
for temp in content:
    print("%d:%s"%(i,temp))
    i +=1
f.close()


f = open("test.txt", "r")
content = f.readline()
print(content)
content = f.readline()

print(content)
f.close()
'''

import os
os.rename("test.txt", "test1.txt")