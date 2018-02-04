#!/usr/local/bin/python2.7
# -*- coding=utf-8 -*-
from simhash import Repeat
from cmsmodel import Cmsmod
from bankmodel import Bankmod
import pymysql
import time,re
nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print('nowtime:',nowtime) 
#print('nowtime:',time.time())
def create_hash():
    REX = re.compile(u'[\u4e00-\u9fa5]+')
    newids = Bankmod.getnewid()
    if newids!='':
       newid = str(newids[0][0]) 
    else:
        newid = ''
    results = Cmsmod.getcontent('50',newid)
    if len(results) < 1:
        print "message not found"
        exit()
    sqlone = '(`simhash`, `ContId`, `Title`, `Url`, `CatId`, `CreatedTime`) values' 
    flag = ''   
    for res in results:
        simhash = Repeat.simhash(res[0])
        if simhash==[]:
            continue
        flag = '1'
        sqlone += '("'+simhash+'","'+str(res[1])+'","'+pymysql.escape_string(str(res[2]))+'","'+str(res[3])+'","'+str(res[4])+'","'+str(res[5])+'"),'
    sqlone = sqlone.strip(',');
    if flag=='1':
        print Bankmod.insertcontent(sqlone,'article_hashcontent')
    #print('endtime:',time.time())
    print('endtime:',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
if __name__ == '__main__':
    create_hash() 
