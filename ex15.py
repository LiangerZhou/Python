#-*- coding:utf-8 -*-
from sys import argv

script, filename = argv
#打开文件，把文件传给变量
txt = open(filename)

print "Here's your file %s:" % filename
print txt.readlines();#打印文件变量接收到的文件内容
txt.close()
#print "Type the filename again:"
#file_again = raw_input("> ")#输入文件名

#txt_again = open(file_again)

#print txt_again.read()