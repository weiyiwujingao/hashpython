#!/usr/local/python2.7/bin/python2.7
# -*- coding=utf-8 -*-
from simhash import Repeat
xxx = '说知乎上有个提问，知乎，小时候缺爱的女孩子，长大后该怎么办 是的小明'
yyy ='小米？'
#ccc = zzz * 10
a = Repeat.simhash(xxx)
b = Repeat.simhash(yyy)
#c = Repeat.simhash(zzz)
print(a)
print(b)
print 'dd'
print(Repeat._hamming(a,b))
#print(Repeat._hamming(a,c))
