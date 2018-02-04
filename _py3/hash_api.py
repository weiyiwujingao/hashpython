#!/usr/local/bin/python2.7
# -*- coding=utf-8 -*-
from simhash import Repeat
from cmsmodel import Cmsmod
import pymysql
import sys,pickle,json
id = sys.argv[1]
if(id==''):
    exit('参数错误')
content = Cmsmod.getcontentbyid(id)
if content[0][0] == '':
    exit('内容为空')
simhash = Repeat.simhash(content[0][0])
print simhash




