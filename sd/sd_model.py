#! /usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
from datetime import datetime


mysql_db = MySQLDatabase('sdpc',
                         user='cosearch',
                         password='123456',
                         host='192.168.1.190',
                         autocommit=True)
mysql_db.connect()


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Document(BaseModel):
    id = BigIntegerField(null=False, primary_key=True, verbose_name='URL数字ID')
    module = CharField(max_length=1000, null=True, verbose_name='所属模块')
    url = CharField(null=False, max_length=1000, verbose_name='法律文书URL')
    title = CharField(null=True, max_length=1000, verbose_name='法律文书标题')
    author = CharField(max_length=1000, null=True, verbose_name='作者')
    pubtime = CharField(max_length=1000, null=True, verbose_name='Publish_time')
    content = TextField(null=True, verbose_name='Content')
    img_url = CharField(max_length=5000, null=True, verbose_name='img_url')
    belong = CharField(max_length=1000, null=False, verbose_name='所属网站')

    created_time = DateTimeField(default=datetime.now, verbose_name='创建时间')


if __name__ == '__main__':
    Document.create_table()
