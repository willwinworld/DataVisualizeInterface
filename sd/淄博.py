#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import requests
from random import uniform
from pyquery import PyQuery as Pq
from dialogue.dumblog import dlog
from peewee import IntegrityError
from sd_model import Document

logger = dlog(__file__, console='debug')


def remove_duplicate_urls(seq):  # 对列表进行去重,并且保持列表顺序
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def jczc(url): # 基层之窗/检察动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk .cxzy_list').items() if i('.ALink').attr('href') is not None]
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zbsrmjcy', 'pageID': 'ofnlpaldfceobbodlcbjgaolgjmolkjk',
                     'moduleID': 'aegbnaeefcepbbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/zbsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk/aegbnaeefcepbbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk .cxzy_list').items() if
                                 i('.ALink').attr('href') is not None]
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def tpxw(url): # 图片新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk td[style]').items() if i('.ALink').attr('href') is not None]
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zbsrmjcy', 'pageID': 'jnjgpfnbfchobbodimdigaolgjmolkjk',
                     'moduleID': 'lklmkjccfchobbodimdigaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/zbsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk/lklmkjccfchobbodimdigaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk td[style]').items() if
                                 i('.ALink').attr('href') is not None]
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def parse_news(url):
    r = requests.get(url)
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


def video(url):  # 在线视频
    video_result = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_result = [{'id': int(re.findall(r'fileid=\d+', i('a[style]').attr('href'))[0].replace('fileid=', '')),
                          'video_url': i('a[style]').attr('href'),
                          'title': i('a[style]').attr('title').split('\n')[0].replace(u'标      题：', ''),
                          'author': i('a[style]').attr('title').split('\n')[1].replace(u'作      者：', ''),
                          'pubtime': i('a[style]').attr('title').split('\n')[2].replace(u'更新时间：', ''),
                          'img_url': i('img').attr('src')} for i in
                         d('#playonsitelistcomponentgbbphdkjpnanbbodlofoloklokedjofd tr a:nth-child(odd)').items() if
                         i('img').attr('src') and i('a[style]').attr('title') is not None]
    # print first_page_result
    video_result.extend(first_page_result)
    return video_result


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
                        belong='淄博')
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
                            belong='淄博')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    try:
        jczc_news_list = remove_duplicate_urls(jczc('http://10.137.112.5/ecdomain/framework/zbsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp'))
        for jczc_news in jczc_news_list:
            try:
                jczc_res = parse_news(jczc_news)
                logger.info(jczc_res['url'])
                save_return_value = save(jczc_res)
                if save_return_value:
                    break
                logger.info('saving 基层之窗')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tpxw_news_list = remove_duplicate_urls(tpxw('http://10.137.112.5/ecdomain/framework/zbsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp'))
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
        video_list = video('http://10.137.112.5/ecdomain/framework/zbsrmjcy/feecjddapkhkbbodlofoloklokedjofd.jsp')
        for video_res in video_list:
            try:
                save_return_value = save_video(video_res)
                if save_return_value:
                    break
                logger.info('saving 视频新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'zbsy'})