import sys
import os
print('hello, world!')
# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):
    full_path = name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)   #msg也就是下面的Hello world!
    # file.close()
os.chdir(sys.path[0]) 
text_create('mytxtfile', 'Hello world!')
# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!