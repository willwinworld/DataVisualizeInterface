#! python2
# -*- coding: utf-8 -*-
import json
from model import Crime
from peewee import RawQuery


def print_time():
    latest_date = None
    for row in Crime.select().order_by(Crime.created_time.desc()):
        latest_date = row.created_time.date()
        break
    print latest_date
    print latest_date.strftime("%Y-%m-%d")
    total_num = Crime.select().where(Crime.created_time.day <= latest_date).count()
    print total_num
    res = json.dumps({latest_date.strftime("%Y-%m-%d"): total_num})
    print res


def print_time1():
    res = []
    rq = RawQuery(Crime, 'select count(*) as count , date(created_time) as created_time from crime group by date(created_time)')
    rq.execute()
    for obj in rq.execute():
        res.append({obj.created_time.strftime("%Y-%m-%d"): obj.count})
    return res


if __name__ == '__main__':
    print_time1()

