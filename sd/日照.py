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
                             d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk .cxzy_list').items() if
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
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'ncihclbofcenbbodlcbjgaolgjmolkjk',
                     'moduleID': 'ebacbimpfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk/ebacbimpfceobbodlcbjgaolgjmolkjk.do',
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


def qxydt(url):  # 区县院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                             d('#newslistComponentlehdhlbkbjplbboelemgibmgbpenneil .cxzy_list').items() if
                             i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentlehdhlbkbjplbboelemgibmgbpenneil tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'lehbdbcibjplbboelemgibmgbpenneil',
                     'moduleID': 'lehdhlbkbjplbboelemgibmgbpenneil',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/lehbdbcibjplbboelemgibmgbpenneil/lehdhlbkbjplbboelemgibmgbpenneil.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentlehdhlbkbjplbboelemgibmgbpenneil .cxzy_list').items() if
                                 i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def tpxw(url):  # 图片新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk td[style]').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'jnjgpfnbfchobbodimdigaolgjmolkjk',
                     'moduleID': 'lklmkjccfchobbodimdigaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk/lklmkjccfchobbodimdigaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk td[style]').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


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
                         d('#playonsitelistcomponentdabbnnbinhoabbodjcbojemipbnkledh tr a:nth-child(odd)').items() if
                         i('img').attr('src') and i('a[style]').attr('title') is not None]
    # print first_page_result
    video_result.extend(first_page_result)
    return video_result


def ldjh(url):  # 领导讲话
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('a').attr('href') for i in
                             d('#newslistComponentaijfeepiapkfbbohkpecmhbedjnnalkn .cxzy_list').items() if
                             i('a').attr('href') is not None and i('a').attr('href') != 'javascript:void(0)']
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentaijfeepiapkfbbohkpecmhbedjnnalkn .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    return news_list


def sywj(url):  # 市院文件
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('a').attr('href') for i in
                             d('#newslistComponentdeffadapbkagbboelemgibmgbpenneil .cxzy_list').items() if
                             i('a').attr('href') is not None]
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.196.19' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentdeffadapbkagbboelemgibmgbpenneil .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentdeffadapbkagbboelemgibmgbpenneil tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'defcjcanbkagbboelemgibmgbpenneil',
                     'moduleID': 'deffadapbkagbboelemgibmgbpenneil',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/defcjcanbkagbboelemgibmgbpenneil/deffadapbkagbboelemgibmgbpenneil.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('a').attr('href') for i in post_d(
            '#newslistComponentdeffadapbkagbboelemgibmgbpenneil .cxzy_list').items() if
                                 i('a').attr('href') is not None]
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.196.19' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentdeffadapbkagbboelemgibmgbpenneil .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def jcxc(url):  # 检察宣传
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('a').attr('href') for i in
                             d('#newslistComponentnhbgokinbkabbboelemgibmgbpenneil .cxzy_list').items() if
                             i('a').attr('href') is not None]
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentnhbgokinbkabbboelemgibmgbpenneil .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentnhbgokinbkabbboelemgibmgbpenneil tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'nhbekajlbkabbboelemgibmgbpenneil',
                     'moduleID': 'nhbgokinbkabbboelemgibmgbpenneil',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/nhbekajlbkabbboelemgibmgbpenneil/nhbgokinbkabbboelemgibmgbpenneil.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('a').attr('href') for i in post_d(
            '#newslistComponentnhbgokinbkabbboelemgibmgbpenneil .cxzy_list').items() if
                                 i('a').attr('href') is not None]
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentnhbgokinbkabbboelemgibmgbpenneil .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def nbkw(url):  # 内部刊物
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('a').attr('href') for i in
                             d('#newslistComponentdhjokpncbkagbboelemgibmgbpenneil .cxzy_list').items() if
                             i('a').attr('href') is not None]
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentdhjokpncbkagbboelemgibmgbpenneil .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentdhjokpncbkagbboelemgibmgbpenneil tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'dhjmdonabkagbboelemgibmgbpenneil',
                     'moduleID': 'dhjokpncbkagbboelemgibmgbpenneil',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/dhjmdonabkagbboelemgibmgbpenneil/dhjokpncbkagbboelemgibmgbpenneil.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('a').attr('href') for i in post_d(
            '#newslistComponentdhjokpncbkagbboelemgibmgbpenneil .cxzy_list').items() if
                                 i('a').attr('href') is not None]
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentdhjokpncbkagbboelemgibmgbpenneil .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def hyjy(url):  # 会议纪要
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('a').attr('href') for i in
                             d('#newslistComponentmogfakpcbkadbboelemgibmgbpenneil .cxzy_list').items() if
                             i('a').attr('href') is not None and i('a').attr('href') != 'javascript:void(0)']
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentmogfakpcbkadbboelemgibmgbpenneil .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    # print len(first_page_table_encrypt_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentmogfakpcbkadbboelemgibmgbpenneil tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'mogcmbabbkadbboelemgibmgbpenneil',
                     'moduleID': 'mogfakpcbkadbboelemgibmgbpenneil',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/mogcmbabbkadbboelemgibmgbpenneil/mogfakpcbkadbboelemgibmgbpenneil.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('a').attr('href') for i in post_d(
            '#newslistComponentdeffadapbkagbboelemgibmgbpenneil .cxzy_list').items() if
                                 i('a').attr('href') is not None]
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentdeffadapbkagbboelemgibmgbpenneil .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def mydsj(url):  # 每月大事记
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('a').attr('href') for i in
                             d('#newslistComponentobhklikecdilbboelemgibmgbpenneil .cxzy_list').items() if
                             i('a').attr('href') is not None]
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentobhklikecdilbboelemgibmgbpenneil .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentobhklikecdilbboelemgibmgbpenneil tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'rzsrmjcy', 'pageID': 'obhiehkdcdilbboelemgibmgbpenneil',
                     'moduleID': 'obhiehkdcdilbboelemgibmgbpenneil',
                     'moreURI': '/ecdomain/framework/rzsrmjcy/obhiehkdcdilbboelemgibmgbpenneil/obhklikecdilbboelemgibmgbpenneil.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('a').attr('href') for i in post_d(
            '#newslistComponentobhklikecdilbboelemgibmgbpenneil .cxzy_list').items() if
                                 i('a').attr('href') is not None]
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.204.76' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentobhklikecdilbboelemgibmgbpenneil .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
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
                            belong='日照')
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
                      belong='日照')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # sydt('http://10.137.204.76/ecdomain/framework/rzsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp')
    # qxydt('http://10.137.204.76/ecdomain/framework/rzsrmjcy/lehbdbcibjplbboelemgibmgbpenneil.jsp')
    # tpxw('http://10.137.204.76/ecdomain/framework/rzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp')
    # video('http://10.137.204.76/ecdomain/framework/rzsrmjcy/hpcfmmdmnhnlbbodjcbojemipbnkledh.jsp')
    # ldjh('http://10.137.204.76/ecdomain/framework/rzsrmjcy/aiiobjahapkfbbohkpecmhbedjnnalkn.jsp')
    # sywj('http://10.137.204.76/ecdomain/framework/rzsrmjcy/defcjcanbkagbboelemgibmgbpenneil.jsp')
    # jcxc('http://10.137.204.76/ecdomain/framework/rzsrmjcy/nhbekajlbkabbboelemgibmgbpenneil.jsp')
    # nbkw('http://10.137.204.76/ecdomain/framework/rzsrmjcy/dhjmdonabkagbboelemgibmgbpenneil.jsp')
    # hyjy('http://10.137.204.76/ecdomain/framework/rzsrmjcy/mogcmbabbkadbboelemgibmgbpenneil.jsp')
    # mydsj('http://10.137.204.76/ecdomain/framework/rzsrmjcy/obhiehkdcdilbboelemgibmgbpenneil.jsp')

    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.204.76/ecdomain/framework/rzsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp'))
        for sydt_news in sydt_news_list:
            try:
                rz_res = parse_news(sydt_news)
                logger.info(rz_res['url'])
                save_return_value = save(rz_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        qxydt_news_list = remove_duplicate_urls(qxydt('http://10.137.204.76/ecdomain/framework/rzsrmjcy/lehbdbcibjplbboelemgibmgbpenneil.jsp'))
        for qxydt_news in qxydt_news_list:
            try:
                qxydt_res = parse_news(qxydt_news)
                logger.info(qxydt_res['url'])
                save_return_value = save(qxydt_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tpxw_news_list = remove_duplicate_urls(tpxw('http://10.137.204.76/ecdomain/framework/rzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp'))
        for tpxw_news in tpxw_news_list:
            try:
                tpxw_res = parse_news(tpxw_news)
                logger.info(tpxw_res['url'])
                save_return_value = save(tpxw_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        video_list = video('http://10.137.204.76/ecdomain/framework/rzsrmjcy/hpcfmmdmnhnlbbodjcbojemipbnkledh.jsp')
        for video_res in video_list:
            try:
                save_return_value = save_video(video_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        ldjh_news_list = remove_duplicate_urls(ldjh('http://10.137.204.76/ecdomain/framework/rzsrmjcy/aiiobjahapkfbbohkpecmhbedjnnalkn.jsp'))
        for ldjh_news in ldjh_news_list:
            try:
                ldjh_res = parse_news(ldjh_news)
                logger.info(ldjh_res['url'])
                save_return_value = save(ldjh_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        sywj_news_list = remove_duplicate_urls(sywj('http://10.137.204.76/ecdomain/framework/rzsrmjcy/defcjcanbkagbboelemgibmgbpenneil.jsp'))
        for sywj_news in sywj_news_list:
            try:
                sywj_res = parse_news(sywj_news)
                logger.info(sywj_res['url'])
                save_return_value = save(sywj_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcxc_news_list = remove_duplicate_urls(jcxc('http://10.137.204.76/ecdomain/framework/rzsrmjcy/nhbekajlbkabbboelemgibmgbpenneil.jsp'))
        for jcxc_news in jcxc_news_list:
            try:
                jcxc_res = parse_news(jcxc_news)
                logger.info(jcxc_res['url'])
                save_return_value = save(jcxc_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        nbkw_news_list = remove_duplicate_urls(nbkw('http://10.137.204.76/ecdomain/framework/rzsrmjcy/dhjmdonabkagbboelemgibmgbpenneil.jsp'))
        for nbkw_news in nbkw_news_list:
            try:
                nbkw_res = parse_news(nbkw_news)
                logger.info(nbkw_res['url'])
                save_return_value = save(nbkw_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        hyjy_news_list = remove_duplicate_urls(hyjy('http://10.137.204.76/ecdomain/framework/rzsrmjcy/mogcmbabbkadbboelemgibmgbpenneil.jsp'))
        for hyjy_news in hyjy_news_list:
            try:
                hyjy_res = parse_news(hyjy_news)
                logger.info(hyjy_res['url'])
                save_return_value = save(hyjy_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        mydsj_news_list = remove_duplicate_urls(mydsj('http://10.137.204.76/ecdomain/framework/rzsrmjcy/obhiehkdcdilbboelemgibmgbpenneil.jsp'))
        for mydsj_news in mydsj_news_list:
            try:
                mydsj_res = parse_news(mydsj_news)
                logger.info(mydsj_res['url'])
                save_return_value = save(mydsj_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'rzsy'})