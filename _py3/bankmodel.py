#!/usr/local/bin/python2.7
# -*- coding=utf-8 -*-
import pymysql
import time

class Bankmod:
    @classmethod
    def getnewid(cls): 
        sql = 'SELECT ContId FROM article_hashcontent ORDER BY ContId DESC LIMIT 1;'
        csdb_connection = pymysql.connect(host='172.30.2.199', user='app_databank', db='databank',password='Op6d5zfc13&h',init_command='SET NAMES UTF8')
        cs_cursor = csdb_connection.cursor()
        cs_cursor.execute(sql)
        id_result = cs_cursor.fetchall()
        if len(id_result) < 1:
            return ''
        return id_result
    @classmethod
    def insertcontent(cls,value='',table=''):
        if value=='' or table=='':
            return ''
        sql = 'INSERT INTO '+table+' '+value+';'
        #print sql
        csdb_connection = pymysql.connect(host='172.30.2.199', user='app_databank', db='databank',password='Op6d5zfc13&h',init_command='SET NAMES UTF8')
        cs_cursor = csdb_connection.cursor()
        a = cs_cursor.execute(sql)
        csdb_connection.commit()
        return a
    @staticmethod
    def _update(s1, s2):
        d = '1'
        return d
    