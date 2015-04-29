# coding=gbk
import codecs
f=codecs.open('hello.txt','r','utf-8')
for line in f:
    print line
f.close()

