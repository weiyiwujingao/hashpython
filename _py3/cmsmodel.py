#!/usr/local/bin/python2.7
# -*- coding=utf-8 -*-
import pymysql
import time

class Cmsmod:
    @classmethod
    def getcontent(cls, limit=10, newid=''):
        sixmonth = str(time.time()-3600*24*30*6)
        sixmonth = '1483200000'
        if newid =='':
            sql = 'SELECT art.Content,art.ContId,cont.Title,cont.Url,cont.CatId,cont.CreatedTime FROM cnfol_article as art inner join cnfol_content as cont on art.ContId = cont.ContId  and cont.CreatedTime>"'+sixmonth+'"  ORDER BY art.ContId ASC LIMIT '+limit
        else:
            sql = 'SELECT art.Content,art.ContId,cont.Title,cont.Url,cont.CatId,cont.CreatedTime FROM cnfol_article as art inner join cnfol_content as cont on art.ContId = cont.ContId and cont.ContId >"'+newid+'" and cont.CreatedTime>"'+sixmonth+'" and art.ContId!="0" ORDER BY art.ContId ASC LIMIT '+limit 

        csdb_connection = pymysql.connect(host='10.1.4.211', user='cnfolCMS', db='cnfolCMS',password='Op6d5zfc13&h',init_command='SET NAMES UTF8')
        cs_cursor = csdb_connection.cursor()
        cs_cursor.execute(sql)
        key_results = cs_cursor.fetchall()
        if len(key_results) < 1:
            return ''
        return key_results
    @classmethod
    def getcontentbyid(cls, id=''):
        sql = 'SELECT Content FROM cnfol_article WHERE ContId="'+id+'" LIMIT 1;'
        csdb_connection = pymysql.connect(host='10.1.4.211', user='cnfolCMS', db='cnfolCMS',password='Op6d5zfc13&h',init_command='SET NAMES UTF8')
        cs_cursor = csdb_connection.cursor()
        cs_cursor.execute(sql)
        key_results = cs_cursor.fetchall()
        if len(key_results) < 1:
            return ''
        return key_results
    @staticmethod
    def _update(s1, s2):
        d = '1'
        return d
    