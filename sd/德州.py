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


def sydt(url):  # 市院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentjnhgfjfjopidbbodiegglicllklfmgjf .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentjnhgfjfjopidbbodiegglicllklfmgjf tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dzsrmjcy', 'pageID': 'jnhdoifiopidbbodiegglicllklfmgjf',
                     'moduleID': 'jnhgfjfjopidbbodiegglicllklfmgjf',
                     'moreURI': '/ecdomain/framework/dzsrmjcy/jnhdoifiopidbbodiegglicllklfmgjf/jnhgfjfjopidbbodiegglicllklfmgjf.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentjnhgfjfjopidbbodiegglicllklfmgjf .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def jcdt(url):  # 基层动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentjddfoaomopiebbodiegglicllklfmgjf .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentjddfoaomopiebbodiegglicllklfmgjf tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dzsrmjcy', 'pageID': 'jdddgpolopiebbodiegglicllklfmgjf',
                     'moduleID': 'jddfoaomopiebbodiegglicllklfmgjf',
                     'moreURI': '/ecdomain/framework/dzsrmjcy/jdddgpolopiebbodiegglicllklfmgjf/jddfoaomopiebbodiegglicllklfmgjf.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentjddfoaomopiebbodiegglicllklfmgjf .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def tztg(url):  # 通知通告
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.96.22:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dzsrmjcy', 'pageID': 'meapooclfcelbbodlcbjgaolgjmolkjk',
                     'moduleID': 'khkkhgebfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/dzsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk/khkkhgebfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.96.22:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def jwdt(url):  # 检务动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dzsrmjcy', 'pageID': 'ofnlpaldfceobbodlcbjgaolgjmolkjk',
                     'moduleID': 'aegbnaeefcepbbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/dzsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk/aegbnaeefcepbbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def zhxw(url):  # 综合新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dzsrmjcy', 'pageID': 'ncihclbofcenbbodlcbjgaolgjmolkjk',
                     'moduleID': 'ebacbimpfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/dzsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk/ebacbimpfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def video(url):  # 视频点播
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
                         d('#playonsitelistcomponentonhncfaaachibboeipdenjgminghncpn tr a:nth-child(odd)').items() if
                         i('img').attr('src') and i('a[style]').attr('title') is not None]
    # print first_page_result
    video_result.extend(first_page_result)
    contain_page_num_url = d('#playonsitelistcomponentonhncfaaachibboeipdenjgminghncpn tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info('video page num: %s' % total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info('video index: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dzsrmjcy', 'pageID': 'cclolhhonhelbbodipjijnaklcdchppk',
                     'moduleID': 'onhncfaaachibboeipdenjgminghncpn',
                     'moreURI': '/ecdomain/framework/dzsrmjcy/cclolhhonhelbbodipjijnaklcdchppk/onhncfaaachibboeipdenjgminghncpn.do',
                     'var_temp': 'bkpenhebnhbhbbodipjijnaklcdchppk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_result = [
            {'id': int(re.findall(r'fileid=\d+', i('a[style]').attr('href'))[0].replace('fileid=', '')),
             'video_url': i('a[style]').attr('href'),
             'title': i('a[style]').attr('title').split('\n')[0].replace(u'标      题：', ''),
             'author': i('a[style]').attr('title').split('\n')[1].replace(u'作      者：', ''),
             'pubtime': i('a[style]').attr('title').split('\n')[2].replace(u'更新时间：', ''),
             'img_url': i('img').attr('src')} for i in
            post_d('#playonsitelistcomponentonhncfaaachibboeipdenjgminghncpn tr a:nth-child(odd)').items() if
            i('img').attr('src') and i('a[style]').attr('title') is not None]
        # print other_page_result
        # print len(other_page_result)
        video_result.extend(other_page_result)
    return video_result


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
                            belong='德州')
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
                            belong='德州')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # sydt('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/jnhdoifiopidbbodiegglicllklfmgjf.jsp')
    # jcdt('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/jdddgpolopiebbodiegglicllklfmgjf.jsp')
    # tztg('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp')
    # jwdt('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp')
    # zhxw('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp')
    # video('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/cclolhhonhelbbodipjijnaklcdchppk.jsp')
    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/jnhdoifiopidbbodiegglicllklfmgjf.jsp'))
        for sydt_news in sydt_news_list:
            try:
                sydt_res = parse_news(sydt_news)
                logger.info(sydt_res['url'])
                save_return_value = save(sydt_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcdt_news_list = remove_duplicate_urls(jcdt('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/jdddgpolopiebbodiegglicllklfmgjf.jsp'))
        for jcdt_news in jcdt_news_list:
            try:
                jcdt_res = parse_news(jcdt_news)
                logger.info(jcdt_res['url'])
                save_return_value = save(jcdt_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tztg_news_list = remove_duplicate_urls(tztg('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp'))
        for tztg_news in tztg_news_list:
            try:
                tztg_res = parse_news(tztg_news)
                logger.info(tztg_res['url'])
                save_return_value = save(tztg_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jwdt_news_list = remove_duplicate_urls(jwdt('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp'))
        for jwdt_news in jwdt_news_list:
            try:
                jwdt_res = parse_news(jwdt_news)
                logger.info(jwdt_res['url'])
                save_return_value = save(jwdt_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        zhxw_news_list = remove_duplicate_urls(zhxw('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp'))
        for zhxw_news in zhxw_news_list:
            try:
                zhxw_res = parse_news(zhxw_news)
                logger.info(zhxw_res['url'])
                save_return_value = save(zhxw_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        video_res_list = video('http://10.137.96.22:8080/ecdomain/framework/dzsrmjcy/cclolhhonhelbbodipjijnaklcdchppk.jsp')
        for video_res in video_res_list:
            try:
                save_return_value = save_video(video_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'dzsy'})