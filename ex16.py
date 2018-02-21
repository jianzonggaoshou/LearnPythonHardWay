# -*- coding: utf-8 -*-
# 从sys模块导入argv函数
from sys import argv

# 将argv参数赋值script, filename常量
script, filename = argv

# 我们将会清空xx文件
print "We're going to erase %r." % filename
# 如果不愿意点击c+c
print "If you don't want that, hit CTRL-C (^C)."
# 如果愿意点击回车
print "If you do want that, hit RETURN."
#
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
