# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', 
        	'123niHAO', 'testdb')
        self.cursor = self.conn.cursor()
        self.conn.set_character_set('utf8')
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def process_item(self, item, spider):
        print "insert into tables...*******************************************\n\n"
        try:
            self.cursor.execute("""INSERT INTO works  
                            VALUES (%s, %s, %s, %s, %s, 
                            %s, %s, %s, %s, %s, %s, %s)""", 
                           (item['name'], 
                            item['category'],
                            item['owner'],
                            item['nation'],
                            item['province'],
                            item['city'],
                            item['author'],
                            item['finish_date'],
                            item['publish_date'],
                            item['register_id'],
                            item['register_date'],
                            item['post_date']))
            print "insert into tables...***************************"
            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])


        return item