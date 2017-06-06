#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""不从上面标题处开始采集"""
import re
import time
import requests
from random import uniform
from pyquery import PyQuery as Pq
from dialogue.dumblog import dlog
from sd_model import Document
from peewee import IntegrityError


logger = dlog(__file__, console='debug')


def remove_duplicate_urls(seq):  # 对列表进行去重,并且保持列表顺序
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def jxyw(url):  # 检察要闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
        # break
    # print len(news_list)
    return news_list


def sywj(url):  # 市院文件
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
        # break
    # print len(news_list)
    return news_list


def sydt(url):  # 市院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.80.162/list.aspx?page=%s&big=20140618153135063' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
        # break
    # print len(news_list)
    return news_list


def jbxx(url):  # 简报信息
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    #     break
    # print len(news_list)
    return news_list


def jcydt(url):  # 基层院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    #     break
    # print len(news_list)
    return news_list


def zhxw(url):  # 综合新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    #     break
    # print len(news_list)
    return news_list


def myds(url):  # 每月大事
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 4))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    #     break
    # print len(news_list)
    return news_list


def parse_news(url):
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    id_number = int(re.findall(r'fileid=\d+', url)[0].replace('fileid=', ''))
    title = d('#newscontent title').text().replace('.html', '')
    module_name = d('#newsall td').eq(0).text().replace(u'当前页面：', '')
    author = d('#newsall td').eq(1).text().replace(u'发布人：', '')
    pubtime = d('#newsall td').eq(2).text().replace(u'发布时间：', '')
    editor = d('#newsall td').eq(5).text().replace(u'审核人：', '')
    content = d('#newscontent').html()
    img_url_list = [i.attr('src') for i in d('.iframeStyle img').items()]
    if len(img_url_list) != 0:
        img_url = '  '.join([i.attr('src') for i in d('.iframeStyle img').items()])
    else:
        img_url = None
    # print id_number
    # print title
    # print module_name
    # print author
    # print pubtime
    # print editor
    # print content
    # print img_url
    result = {'id': id_number, 'module': module_name, 'title': title, 'pubtime': pubtime, 'author': author,
               'content': content, 'editor': editor, 'img_url': img_url, 'url': url}
    return result


def save(param):
    try:
        if Document.select().where(Document.id == param['id']).exists():
            logger.info('duplicate key!')
            return True
        else:
            Document.create(id=param['id'],
                            module=param['module'],
                            url=param['url'],
                            title=param['title'],
                            author=param['author'],
                            pubtime=param['pubtime'],
                            content=param['content'],
                            img_url=param['img_url'],
                            belong='济宁')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # jxyw('http://10.137.80.162/list.aspx?big=20140621171717961')
    # sywj('http://10.137.80.162/list.aspx?big=20140621193624603')
    # sydt('http://10.137.80.162/list.aspx?big=20140618153135063')
    # jbxx('http://10.137.80.162/list.aspx?big=20140621173616541')
    # jcydt('http://10.137.80.162/list.aspx?big=20140618153147401')
    # zhxw('http://10.137.80.162/list.aspx?big=20140619114151996')
    # myds('http://10.137.80.162/list.aspx?big=20140621192745536')

    try:
        jxyw_news_list = remove_duplicate_urls(jxyw('http://10.137.80.162/list.aspx?big=20140621171717961'))
        for jxyw_news in jxyw_news_list:
            try:
                jxyw_res = parse_news(jxyw_news)
                logger.info(jxyw_res['url'])
                save_return_value = save(jxyw_res)
                if save_return_value:
                    break
                logger.info('saving 检察要闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        sywj_news_list = remove_duplicate_urls(sywj('http://10.137.80.162/list.aspx?big=20140621193624603'))
        for sywj_news in sywj_news_list:
            try:
                sywj_res = parse_news(sywj_news)
                logger.info(sywj_res['url'])
                save_return_value = save(sywj_res)
                if save_return_value:
                    break
                logger.info('saving 市院文件')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.80.162/list.aspx?big=20140618153135063'))
        for sydt_news in sydt_news_list:
            try:
                sydt_res = parse_news(sydt_news)
                logger.info(sydt_res['url'])
                save_return_value = save(sydt_res)
                if save_return_value:
                    break
                logger.info('saving 市院动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jbxx_news_list = remove_duplicate_urls(jbxx('http://10.137.80.162/list.aspx?big=20140621173616541'))
        for jbxx_news in jbxx_news_list:
            try:
                jbxx_res = parse_news(jbxx_news)
                logger.info(jbxx_res['url'])
                save_return_value = save(jbxx_res)
                if save_return_value:
                    break
                logger.info('saving 简报新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcydt_news_list = remove_duplicate_urls(jcydt('http://10.137.80.162/list.aspx?big=20140618153147401'))
        for jcydt_news in jcydt_news_list:
            try:
                jcydt_res = parse_news(jcydt_news)
                logger.info(jcydt_res['url'])
                save_return_value = save(jcydt_res)
                if save_return_value:
                    break
                logger.info('saving 基层院动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        zhxw_news_list = remove_duplicate_urls(zhxw('http://10.137.80.162/list.aspx?big=20140619114151996'))
        for zhxw_news in zhxw_news_list:
            try:
                zhxw_res = parse_news(zhxw_news)
                logger.info(zhxw_res['url'])
                save_return_value = save(zhxw_res)
                if save_return_value:
                    break
                logger.info('saving 综合新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        myds_news_list = remove_duplicate_urls(myds('http://10.137.80.162/list.aspx?big=20140621192745536'))
        for myds_news in myds_news_list:
            try:
                myds_res = parse_news(myds_news)
                logger.info(myds_res['url'])
                save_return_value = save(myds_res)
                if save_return_value:
                    break
                logger.info('saving 每月大事')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'jningsy'})