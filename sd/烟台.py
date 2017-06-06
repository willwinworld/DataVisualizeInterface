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


def jcyw(url):  # 检查要闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i('.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dysjcy2017', 'pageID': 'ikalkojobnmnbboejeneocnlcepnhdfo',
                     'moduleID': 'kleilopabnmnbboejeneocnlcepnhdfo',
                     'moreURI': '/ecdomain/framework/dysjcy2017/ikalkojobnmnbboejeneocnlcepnhdfo/kleilopabnmnbboejeneocnlcepnhdfo.do',
                     'var_temp': 'hmmlcmonocbebbodiacnlmllogadpifn',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i('.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def bmdt(url):  # 市院动态，部门动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk .jspcCommand').eq(-1).attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'ytsrmjcy', 'pageID': 'ncihclbofcenbbodlcbjgaolgjmolkjk',
                     'moduleID': 'ebacbimpfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/ytsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk/ebacbimpfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk td').items() if i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i('.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def jcydt(url):  # 基层院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentbelcdhkjogegbbodihgfigcobjhepail td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentbelcdhkjogegbbodihgfigcobjhepail td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentbelcdhkjogegbbodihgfigcobjhepail .jspcCommand').eq(-1).attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'ytsrmjcy', 'pageID': 'bekpmgkhogegbbodihgfigcobjhepail',
                     'moduleID': 'belcdhkjogegbbodihgfigcobjhepail',
                     'moreURI': '/ecdomain/framework/ytsrmjcy/bekpmgkhogegbbodihgfigcobjhepail/belcdhkjogegbbodihgfigcobjhepail.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentbelcdhkjogegbbodihgfigcobjhepail td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentbelcdhkjogegbbodihgfigcobjhepail td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def ggzc(url):  # 改革之窗
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentbmpnamhjogedbbodihgfigcobjhepail td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentbmpnamhjogedbbodihgfigcobjhepail td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentbmpnamhjogedbbodihgfigcobjhepail .jspcCommand').eq(-1).attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'ytsrmjcy', 'pageID': 'bmpkjlhhogedbbodihgfigcobjhepail',
                     'moduleID': 'bmpnamhjogedbbodihgfigcobjhepail',
                     'moreURI': '/ecdomain/framework/ytsrmjcy/bmpkjlhhogedbbodihgfigcobjhepail/bmpnamhjogedbbodihgfigcobjhepail.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentbmpnamhjogedbbodihgfigcobjhepail td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentbmpnamhjogedbbodihgfigcobjhepail td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def fzzx(url):  # 法制在线
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentibllfhmbogeebbodihgfigcobjhepail td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentibllfhmbogeebbodihgfigcobjhepail td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentibllfhmbogeebbodihgfigcobjhepail .jspcCommand').eq(-1).attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'ytsrmjcy', 'pageID': 'iblioglpogeebbodihgfigcobjhepail',
                     'moduleID': 'ibllfhmbogeebbodihgfigcobjhepail',
                     'moreURI': '/ecdomain/framework/ytsrmjcy/iblioglpogeebbodihgfigcobjhepail/ibllfhmbogeebbodihgfigcobjhepail.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentibllfhmbogeebbodihgfigcobjhepail td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentibllfhmbogeebbodihgfigcobjhepail td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def tztg(url):  # 通知通告
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk .jspcCommand').eq(-1).attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'ytsrmjcy', 'pageID': 'meapooclfcelbbodlcbjgaolgjmolkjk',
                     'moduleID': 'khkkhgebfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/ytsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk/khkkhgebfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.48.11:8087' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
    return news_list


def zxsp(url):  # 在线视频
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
                         d('#playonsitelistcomponentdabbnnbinhoabbodjcbojemipbnkledh tr a:nth-child(odd)').items() if
                         i('img').attr('src') and i('a[style]').attr('title') is not None]
    # print first_page_result
    video_result.extend(first_page_result)
    contain_page_num_url = d('#playonsitelistcomponentdabbnnbinhoabbodjcbojemipbnkledh tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info('video page num: %s' % total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info('video index: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'ytsrmjcy', 'pageID': 'hpcfmmdmnhnlbbodjcbojemipbnkledh',
                     'moduleID': 'dabbnnbinhoabbodjcbojemipbnkled',
                     'moreURI': '/ecdomain/framework/ytsrmjcy/hpcfmmdmnhnlbbodjcbojemipbnkledh/dabbnnbinhoabbodjcbojemipbnkledh.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
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
            post_d('#playonsitelistcomponentdabbnnbinhoabbodjcbojemipbnkledh tr a:nth-child(odd)').items() if
            i('img').attr('src') and i('a[style]').attr('title') is not None]
        # print other_page_result
        # print len(other_page_result)
        video_result.extend(other_page_result)
    return video_result


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
                            belong='烟台')
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
                            belong='烟台')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # jcyw('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp')
    # bmdt('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp')
    # jcydt('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/bekpmgkhogegbbodihgfigcobjhepail.jsp')
    # ggzc('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/bmpkjlhhogedbbodihgfigcobjhepail.jsp')
    # fzzx('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/iblioglpogeebbodihgfigcobjhepail.jsp')
    # tztg('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp')
    # zxsp('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/hpcfmmdmnhnlbbodjcbojemipbnkledh.jsp')

    try:
        jcyw_news_list = remove_duplicate_urls(jcyw('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp'))
        for jcyw_news in jcyw_news_list:
            try:
                jcyw_res = parse_news(jcyw_news)
                logger.info(jcyw_res['url'])
                save_return_value = save(jcyw_res)
                if save_return_value:
                    break
                logger.info('saving 检察要闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        bmdt_news_list = remove_duplicate_urls(bmdt('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp'))
        for bmdt_news in bmdt_news_list:
            try:
                bmdt_res = parse_news(bmdt_news)
                logger.info(bmdt_res['url'])
                save_return_value = save(bmdt_res)
                if save_return_value:
                    break
                logger.info('saving 部门动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcdt_news_list = remove_duplicate_urls(jcydt('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/bekpmgkhogegbbodihgfigcobjhepail.jsp'))
        for jcdt_news in jcdt_news_list:
            try:
                jcdt_res = parse_news(jcdt_news)
                logger.info(jcdt_res['url'])
                save_return_value = save(jcdt_res)
                if save_return_value:
                    break
                logger.info('saving 基层动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        ggzc_news_list = remove_duplicate_urls(ggzc('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/bmpkjlhhogedbbodihgfigcobjhepail.jsp'))
        for ggzc_news in ggzc_news_list:
            try:
                ggzc_res = parse_news(ggzc_news)
                logger.info(ggzc_res['url'])
                save_return_value = save(ggzc_res)
                if save_return_value:
                    break
                logger.info('saving 改革之窗')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        fzzx_news_list = remove_duplicate_urls(fzzx('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/iblioglpogeebbodihgfigcobjhepail.jsp'))
        for fzzx_news in fzzx_news_list:
            try:
                fzzx_res = parse_news(fzzx_news)
                logger.info(fzzx_res['url'])
                save_return_value = save(fzzx_res)
                if save_return_value:
                    break
                logger.info('saving 法制在线')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tztg_news_list = remove_duplicate_urls(tztg('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp'))
        for tztg_news in tztg_news_list:
            try:
                tztg_res = parse_news(tztg_news)
                logger.info(tztg_res['url'])
                save_return_value = save(tztg_res)
                if save_return_value:
                    break
                logger.info('saving 通知通告')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        zxsp_video_list = zxsp('http://10.137.48.11:8087/ecdomain/framework/ytsrmjcy/hpcfmmdmnhnlbbodjcbojemipbnkledh.jsp')
        for zxsp_res in zxsp_video_list:
            try:
                save_return_value = save_video(zxsp_res)
                if save_return_value:
                    break
                logger.info('saving 在线视频')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'ytsy'})