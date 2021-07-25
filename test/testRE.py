#-*- coding = utf-8 -*-
#@Time : 2021/5/4 16:34
#@Author : 李家旺
#@File : testRE.py
#@Software : IntelliJ IDEA

#正则表达式
import re

#创建模式对象
pat = re.compile("AA") # AA是正则表达式
m = pat.search("CAABAAA") # 这的字符串是被校验的内容  只匹配第一个
print(m)

n = re.search("asd", "fdasd") # 1：规则 2：被校验对象
print(n)

print(re.findall("a", "ASDFDFadfsa")) # 前面是规则，后面是被校验对象

print(re.findall("[A-Z]", "ASDSDjhsjdaSJDHIS"))

print(re.findall("[A-Z]+", "ASDSDjhsjdaSJDHIS"))

print(re.sub("a", "A", "abcdcasd")) # 找到a用A替换在三个字符串查找

#建议在正则表达式中，被比较的字符串前面加上r, 防止转义字符
a = r"\sdfsdf-\'"
print(a)