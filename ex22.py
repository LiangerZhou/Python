# 前21章总结

# print 打印
# "" 字符串符号
# '' 字符/短的字符串
# ^ 用来指示出错的位置
# SyntaxError 语法错误
# -*- coding:utf-8 -*- 解决关于ASCII编码错误问题
#（octothorpe） 单行注释
# + 加号
# - 减号
# / 除号
# * 乘号
# % 取余
# < 小于号
# > 大于号
# <= 小于等于
# >= 大于等于
# () 括号
# 运算优先级：PEMDAS --> 括号（Parentheses）、指数（Exponents）、乘（Multiplication）、除（Division）、加（Addition）、减（Subtraction）
# =(单等号)作用是将右边的值赋值给左边的变量名
# ==(双等号)作用是检查左右两边是否相等
# %s 就是str 只打印要输出的内容 用于显示
# %r 就是repr 打印所用东西包括符号 用于调试
# round()函数 将浮点数四舍五入
# TypeError:'str' Object is not callable 漏写字符串和变量之间的%号
# TypeError：not all arguments converted during string formatting 字符串里的%格式化字符数量比后面的给的变量多
# ()可以用来放多个变量，之间以逗号分隔
# raw_input() 接收用户输入  input()函数只接收合法的python表达式
# print 中逗号作用是取消换行，加空格，（print默认后面加的是换行）
# \n 换行
# """多行字符串，之间无空格
# \\ 反斜杠
# \' 单引号
# \" 双引号
# \a ASCII响铃符（BEL）
# \b ASCII退格符（BS）
# \f ASCII进纸符（FF）
# \n ASCII换行符（LF）
# \N{name} Unicode数据库中的字符名，其中name是它的名字，仅适用Unicode
# \r ASCII回车符（CR）
# \t ASCII水平制表符（TAB）
# \uxxxx 值为16位十六进制值xxxx的字符（仅适用Unicode）
# \Uxxxxxxxx 值为32位十六进制值xxxxxxxx的字符（仅适用Unicode）
# \v ASCII垂直制表符（VT）
# \ooo 值为八进制值ooo的字符
# \xhh 值为十六进制数hh的字符
# python -m pydoc 用于查看某个模块（比如file）文档
# from sys import argv 引入argv模块 
# int()会把括号里的内容转换成数字
# ValueError:need more than 1 value to unpack 提供参数少了
# . 用来调用函数
# txt = open(filename) 返回文件的对象
# close() 关闭文件
# read() 读取文件内容
# readline() 读取文本文件中的一行
# truncate() 清空文件
# write(stuff) 将stuff写入文件
# seek(0)指定位置，0代表文件开始第一位，其处理对象是字节而非行，seek(0)转到文件的 0 byte（即第一个字节）位置
# 'w'表示写入模式，'r'表示读取模式，'a'表示追加模式
# 'w+'、'r+'、'a+' 可以把文件用同时读写的方法打开
# open()函数默认模式是'r'
# linux cat命令用于显示文件内容，对应的windows powershell里的命令 type
# len()以数的形式返回你传递的字符串长度
# read()一旦运行，文件就会被Python关掉
# exists(filename)判断文件是否存在 返回True or False
# def 函数名（参数）:     函数定义，内容要缩进
# 函数命名 只要以字母、数字以及下划线组成，且不是数字开头
# *args的*的功能：告诉Python把函数的所有参数都接收进来
# x += y 等同于x = x + y
# return 函数返回内容
# float(raw_input)将输入转成浮点型
# int(raw_input)将输入转成整型