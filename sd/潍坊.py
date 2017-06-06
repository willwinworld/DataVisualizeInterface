#! /usr/bin/python
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


def jcydt(url):  # 基层院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    # print first_page_table_urls
    # print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number+1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20140827114409212' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 6))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    return news_list


def xxjb(url):  # 信息简报
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    print first_page_table_urls
    print len(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&big=20141017145036627' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 6))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    return news_list


def tpxw(url):  # 图片新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls(
        [i('a').attr('href') for i in d('#rpt td').items() if i('a').attr('href') is not None])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_number = d('#PageContent a').eq(-1).attr('href')
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.42/list.aspx?page=%s&type=pic&tip=tpxw' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 6))
        new_r.encoding = 'utf-8'
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        other_page_table_urls = remove_duplicate_urls(
            [i('a').attr('href') for i in new_d('#rpt td').items() if i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    return news_list


def spxw(url):  # 视频新闻
    news_list = []
    r = requests.get(url)
    # r.encoding = 'ISO-8859-1'
    d = Pq(r.content).make_links_absolute(base_url=url)
    # video_urls = [i('a').attr('href') for i in d('.acontainer .pright').items()]
    # video_urls_ids = [int(re.findall(r'id=\d+', i('a').attr('href'))[0].replace('id=', '')) for i in d('.acontainer .pright').items()]
    # titles = [i('a').text().encode('ISO-8859-1', 'ignore') for i in d('.acontainer .pright').items()]
    # img_urls = [i('img').attr('src') for i in d('.acontainer .pleft').items()]
    # pubtimes = [i('ul li:eq(1)').text().encode('ISO-8859-1', 'ignore').replace('时  间：', '') for i in d('.acontainer .pright').items()]
    # editors = [i('ul li:eq(2)').text().encode('ISO-8859-1', 'ignore').replace('发布人 ：', '') for i in d('.acontainer .pright').items()]
    right_area = [{'id': int(re.findall(r'id=\d+', i('a').attr('href'))[0].replace('id=', '')), 'video_url': i('a').attr('href'),
                   'title': i('a').text().encode('ISO-8859-1', 'ignore'),
                   'pubtime': i('ul li:eq(1)').text().encode('ISO-8859-1', 'ignore').replace('时  间：', ''),
                   'editor': i('ul li:eq(2)').text().encode('ISO-8859-1', 'ignore').replace('发布人 ：', '')} for i in d('.acontainer .pright').items()]
    left_area = [{'img_url': i('img').attr('src')} for i in d('.acontainer .pleft').items()]
    whole_area = zip(right_area, left_area)
    first_page_result = [dict(i[0], **i[1]) for i in whole_area]
    # print first_page_result
    news_list.extend(first_page_result)
    contain_page_number = d('#PageContent a').eq(-2).attr('href')
    # print contain_page_number
    total_page_number = int(re.findall(r'page=\d+', contain_page_number)[0].replace('page=', ''))
    logger.info(total_page_number)
    for idx in xrange(2, total_page_number + 1):
        new_url = 'http://10.137.64.5/shipin/shipin.aspx?id=28&page=%s' % idx
        logger.info(new_url)
        new_r = requests.get(new_url)
        time.sleep(uniform(2, 6))
        new_d = Pq(new_r.content).make_links_absolute(base_url=new_url)
        right_area = [{'id': int(re.findall(r'id=\d+', i('a').attr('href'))[0].replace('id=', '')),
                       'video_url': i('a').attr('href'),
                       'title': i('a').text().encode('ISO-8859-1', 'ignore'),
                       'pubtime': i('ul li:eq(1)').text().encode('ISO-8859-1', 'ignore').replace('时  间：', ''),
                       'author': i('ul li:eq(2)').text().encode('ISO-8859-1', 'ignore').replace('发布人 ：', '')} for i in
                      new_d('.acontainer .pright').items()]
        left_area = [{'img_url': i('img').attr('src')} for i in new_d('.acontainer .pleft').items()]
        whole_area = zip(right_area, left_area)
        other_page_result = [dict(i[0], **i[1]) for i in whole_area]
        # print other_page_result
        news_list.extend(other_page_result)
        # break
    # print news_list
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
                            belong='潍坊')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


def save_video(param):
    try:
        if Document.select().where(Document.id == param['id']).exists():
            logger.info('duplicate key!')
            return True
        else:
            Document.create(id=param['id'],
                            url=param['video_url'],
                            title=param['title'],
                            author=param['author'],
                            pubtime=param['pubtime'],
                            img_url=param['img_url'],
                            belong='潍坊')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    try:
        jcydt_news_list = remove_duplicate_urls(jcydt('http://10.137.64.42/list.aspx?big=20140827114409212'))
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
        xxjb_news_list = remove_duplicate_urls(xxjb('http://10.137.64.42/list.aspx?big=20141017145036627'))
        for xxjb_news in xxjb_news_list:
            try:
                xxjb_res = parse_news(xxjb_news)
                logger.info(xxjb_res['url'])
                save_return_value = save(xxjb_res)
                if save_return_value:
                    break
                logger.info('saving 信息简报')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tpxw_news_list = remove_duplicate_urls(tpxw('http://10.137.64.42/List.aspx?type=pic&tip=tpxw'))
        for tpxw_news in tpxw_news_list:
            try:
                tpxw_res = parse_news(tpxw_news)
                logger.info(tpxw_res['url'])
                save_return_value = save(tpxw_res)
                if save_return_value:
                    break
                logger.info('saving 图片新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        spxw_video_list  = spxw('http://10.137.64.5/shipin/shipin.aspx')
        for spxw_res in spxw_video_list:
            try:
                save_return_value = save_video(spxw_res)
                if save_return_value:
                    break
                logger.info('saving 视频新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'wfsy'})