#-*- coding = utf-8 -*-
#@Time : 2021/5/4 15:36
#@Author : 李家旺
#@File : testBs4.py
#@Software : IntelliJ IDEA

from bs4 import BeautifulSoup
#BeautifulSoup4将复杂HTML文档转换成一个复杂的属性结构
#每个节点都是python对象，所有对象可以归纳为四种
# Tag
# NavigableString
# BeautifulSoup
# Comment

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.head)

#Tag  标签和内容，拿到第一个标签
#print(type(bs.head))

# NavigableString 标签里的内容
#print(type(bs.title.string))

# 属性
#print(bs.a.attrs)

# BeautifulSoup 整个文档
# print(type(bs))
# print(bs)
# print(bs.name)


# print(bs.a.string)

#文档遍历
#print(bs.head.contents)

#1.文档搜索
#t_list = bs.find_all("a")  #查找所有a标签  (字符串方式过滤）
#print(t_list)

#2.正则表达式搜索 使用search()
import re
list = bs.find_all(re.compile("a"))
print(list)

#方法搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# list = bs.find_all(name_is_exists)
# print(list)
# for item in list:
#     print(item)


# 参数搜索
# list = bs.find_all(id = "head")
# for item in list:
#      print(item)

# test 搜索
# list = bs.find_all(text=["hao123","地图","贴吧"])
# for item in list:
#       print(item)

# 正则表达式
# list = bs.find_all(text=re.compile("\d"))
# for item in list:
#        print(item)

# list = bs.find_all("a", limit=3)
# print(list)

# css选择器
'''
print(bs.select('title'))  # 标签查找
print(bs.select(".mnav")) #.表示类名
print(bs.select("#u1")) # id查找
print(bs.select("a[class='bri']")) #属性查找
print(bs.select("head > title")) # 层级查找
print(bs.select(".mnav ~ .bri"))
'''
