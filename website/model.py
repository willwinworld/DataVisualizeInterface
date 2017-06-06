#! /usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from datetime import datetime

db = SqliteDatabase('crime.sqlite')
# mysql_db = MySQLDatabase('sdpc',
#                          user='cosearch',
#                          password='123456',
#                          host='192.168.1.190',
#                          autocommit=True)
# mysql_db.connect()


class BaseModel(Model):
    class Meta:
        # database = mysql_db
        database = db


class Crime(BaseModel):
    url = CharField(null=False, primary_key=True, verbose_name='URL')
    module = CharField(max_length=1000, null=True, verbose_name='所属模块')
    content = TextField(null=True, verbose_name='Content')

    created_time = DateTimeField(default=datetime.now, verbose_name='创建时间')


if __name__ == '__main__':
    Crime.create_table()