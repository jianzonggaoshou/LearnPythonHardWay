# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

# 命令行传入参数，脚本名，源文件， 目标文件
script, from_file, to_file = argv

# 打印 从源文件复制到目标文件
print "Copying from %s to %s" % (from_file, to_file)

# 我能在一行中做这两行吗？
# we could do these two on one line too, how?
# 打开源文件并赋值给in_file
in_file = open(from_file)
# 将in_file读取并赋值给Indata
indata = in_file.read()

# 打印 输入文件的长度是XX字节
print "The input file is %d bytes long" % len(indata)

# 打印 输出文件存在吗？
print "Does the output file exist? %r" % exists(to_file)
# 打印 准备好了吗？点击RETURN来继续，C+C来离开
print "Ready, hit RETURN to contitue, CTRL-C to abort."
# 用户输入
raw_input()

# 以写入方式打开目标文件，并赋值给out_file
out_file = open(to_file, 'w')
# 将源文件写入目标文件
out_file.write(indata)

# 打印， 好，完成
print "Alright, all done."

# 目标文件关闭
out_file.close()
# 源文件关闭
in_file.close()
