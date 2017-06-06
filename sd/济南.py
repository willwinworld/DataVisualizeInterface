#! /usr/bin/env python
# -*- coding: utf-8 -*-
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


def ldjh(url):  # 领导讲话
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d('#newslistComponentjajbdhfijkmibboekolppkpkpincahbm tr[style]').items() if
                             i('.cxzy_list a').attr('href') != 'javascript:void(0)'])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.0.6:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        d('#newslistComponentjajbdhfijkmibboekolppkpkpincahbm tr[style]').items() if i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentjajbdhfijkmibboekolppkpkpincahbm tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num+1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'jaipponhjkmibboekolppkpkpincahbm',
                     'moduleID': 'jajbdhfijkmibboekolppkpkpincahbm',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/jaipponhjkmibboekolppkpkpincahbm/jajbdhfijkmibboekolppkpkpincahbm.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentjajbdhfijkmibboekolppkpkpincahbm tr[style]').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)'])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.0.6:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentjajbdhfijkmibboekolppkpkpincahbm tr[style]').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
    return news_list


def tztg(url):  # 通知通告
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr[style]').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)'])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.0.6:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for i
        in
        d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr[style]').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'meapooclfcelbbodlcbjgaolgjmolkjk',
                     'moduleID': 'khkkhgebfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk/khkkhgebfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr[style]').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)'])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.0.6:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr[style]').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
    return news_list


def jjdt(url):  # 济检动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentnodpgkpoijbdbboflogpnliadakfmhjf td[style]').items() if i('.ALink').attr('href') is not None]
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentnodpgkpoijbdbboflogpnliadakfmhjf tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'jnjgpfnbfchobbodimdigaolgjmolkjk',
                     'moduleID': 'nodpgkpoijbdbboflogpnliadakfmhjf',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk/nodpgkpoijbdbboflogpnliadakfmhjf.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
        '#newslistComponentnodpgkpoijbdbboflogpnliadakfmhjf td[style]').items() if i('.ALink').attr('href') is not None]
        news_list.extend(other_page_table_urls)
    return news_list


def jczx(url):  # 基层在线
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentndjohlbbaigebbohlmnejhbbadgcjaeh .cxzy_list').items() if i('.ALink').attr('href') is not None]
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentndjohlbbaigebbohlmnejhbbadgcjaeh tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'hdgbjdjjcdfobboeibioklohbpcojgac',
                     'moduleID': 'ndjohlbbaigebbohlmnejhbbadgcjaeh',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/hdgbjdjjcdfobboeibioklohbpcojgac/ndjohlbbaigebbohlmnejhbbadgcjaeh.do',
                     'var_temp': 'templatedefault',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentndjohlbbaigebbohlmnejhbbadgcjaeh .cxzy_list').items() if
                                 i('.ALink').attr('href') is not None]
        news_list.extend(other_page_table_urls)
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


def video(url):  # 视频新闻
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
                         d('#playonsitelistcomponentghhkmpccgfihbbofimohokinkidhlinp tr a:nth-child(odd)').items() if
                         i('img').attr('src') and i('a[style]').attr('title') is not None]
    # print first_page_result
    # print len(first_page_result)
    video_result.extend(first_page_result)
    contain_page_num_url = d('#playonsitelistcomponentghhkmpccgfihbbofimohokinkidhlinp tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info('video page num: %s' % total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info('video index: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'lejkoopcgaakbbofieaamlbffgdpdccj',
                     'moduleID': 'ghhkmpccgfihbbofimohokinkidhlinp',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/lejkoopcgaakbbofieaamlbffgdpdccj/ghhkmpccgfihbbofimohokinkidhlinp.do',
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
            post_d('#playonsitelistcomponentghhkmpccgfihbbofimohokinkidhlinp tr a:nth-child(odd)').items() if
            i('img').attr('src') and i('a[style]').attr('title') is not None]
        # print other_page_result
        # print len(other_page_result)
        video_result.extend(other_page_result)
    return video_result


def mtbb(url):  # 媒体播报
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentbnbohajiibpgbbofjmipikpkpplgdfeb .cxzy_list').items() if
                             i('.ALink').attr('href') is not None]
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentbnbohajiibpgbbofjmipikpkpplgdfeb tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'bnbmenlhibpgbbofjmipikpkpplgdfeb',
                     'moduleID': 'bnbohajiibpgbbofjmipikpkpplgdfeb',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/bnbmenlhibpgbbofjmipikpkpplgdfeb/bnbohajiibpgbbofjmipikpkpplgdfeb.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentbnbohajiibpgbbofjmipikpkpplgdfeb .cxzy_list').items() if
                                 i('.ALink').attr('href') is not None]
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def gjxw(url):  # 国际新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentdhghadlkdjmebboginknjeijnkffjlof .cxzy_list').items() if
                             i('.ALink').attr('href') is not None]
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentdhghadlkdjmebboginknjeijnkffjlof tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'dhgfcopidjmebboginknjeijnkffjlof',
                     'moduleID': 'dhghadlkdjmebboginknjeijnkffjlof',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/dhgfcopidjmebboginknjeijnkffjlof/dhghadlkdjmebboginknjeijnkffjlof.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentdhghadlkdjmebboginknjeijnkffjlof .cxzy_list').items() if
                                 i('.ALink').attr('href') is not None]
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def gnxw(url):  # 国内新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentckgbjoomdjmfbboginknjeijnkffjlof .cxzy_list').items() if
                             i('.ALink').attr('href') is not None]
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentckgbjoomdjmfbboginknjeijnkffjlof tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'ckfpkdbldjmfbboginknjeijnkffjlof',
                     'moduleID': 'ckgbjoomdjmfbboginknjeijnkffjlof',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/ckfpkdbldjmfbboginknjeijnkffjlof/ckgbjoomdjmfbboginknjeijnkffjlof.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentckgbjoomdjmfbboginknjeijnkffjlof .cxzy_list').items() if
                                 i('.ALink').attr('href') is not None]
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def fzyw(url):  # 法治要闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = [i('.ALink').attr('href') for i in d(
        '#newslistComponentcjjkddhedjmjbboginknjeijnkffjlof .cxzy_list').items() if
                             i('.ALink').attr('href') is not None]
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentcjjkddhedjmjbboginknjeijnkffjlof tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'jinansrmjcy', 'pageID': 'cjjiifmddjmjbboginknjeijnkffjlof',
                     'moduleID': 'cjjkddhedjmjbboginknjeijnkffjlof',
                     'moreURI': '/ecdomain/framework/jinansrmjcy/cjjiifmddjmjbboginknjeijnkffjlof/cjjkddhedjmjbboginknjeijnkffjlof.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = [i('.ALink').attr('href') for i in post_d(
            '#newslistComponentcjjkddhedjmjbboginknjeijnkffjlof .cxzy_list').items() if
                                 i('.ALink').attr('href') is not None]
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


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
                            belong='济南')
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
                            belong='济南')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # ldjh('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/jaipponhjkmibboekolppkpkpincahbm.jsp')
    # tztg('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp')
    # jjdt('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp')
    # jczx('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/hdgbjdjjcdfobboeibioklohbpcojgac.jsp')
    # video('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/lejkoopcgaakbbofieaamlbffgdpdccj.jsp')
    # mtbb('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/bnbmenlhibpgbbofjmipikpkpplgdfeb.jsp')
    # gjxw('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/dhgfcopidjmebboginknjeijnkffjlof.jsp')
    # gnxw('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/ckfpkdbldjmfbboginknjeijnkffjlof.jsp')
    # fzyw('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/cjjiifmddjmjbboginknjeijnkffjlof.jsp')

    try:
        ldjh_news_list = remove_duplicate_urls(ldjh('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/jaipponhjkmibboekolppkpkpincahbm.jsp'))
        for ldjh_news in ldjh_news_list:
            try:
                ldjh_res = parse_news(ldjh_news)
                logger.info(ldjh_res['url'])
                save_return_value = save(ldjh_res)
                if save_return_value:
                    break
                logger.info('saving 领导讲话')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tztg_news_list = remove_duplicate_urls(tztg('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp'))
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
        jjdt_news_list = remove_duplicate_urls(jjdt('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp'))
        for jjdt_news in jjdt_news_list:
            try:
                jjdt_res = parse_news(jjdt_news)
                logger.info(jjdt_res['url'])
                save_return_value = save(jjdt_res)
                if save_return_value:
                    break
                logger.info('saving 济检动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jczx_news_list = remove_duplicate_urls(jczx('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/hdgbjdjjcdfobboeibioklohbpcojgac.jsp'))
        for jczx_news in jczx_news_list:
            try:
                jczx_res = parse_news(jczx_news)
                logger.info(jczx_res['url'])
                save_return_value = save(jczx_res)
                if save_return_value:
                    break
                logger.info('saving 基层在线')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        video_list = video('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/lejkoopcgaakbbofieaamlbffgdpdccj.jsp')
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

    try:
        mtbb_list = remove_duplicate_urls(mtbb('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/bnbmenlhibpgbbofjmipikpkpplgdfeb.jsp'))
        for mtbb_news in mtbb_list:
            try:
                mtbb_res = parse_news(mtbb_news)
                logger.info(mtbb_res['url'])
                save_return_value = save(mtbb_res)
                if save_return_value:
                    break
                logger.info('saving 媒体播报')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        gjxw_list = remove_duplicate_urls(gjxw('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/dhgfcopidjmebboginknjeijnkffjlof.jsp'))
        for gjxw_news in gjxw_list:
            try:
                gjxw_res = parse_news(gjxw_news)
                logger.info(gjxw_res['url'])
                save_return_value = save(gjxw_res)
                if save_return_value:
                    break
                logger.info('saving 国际新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        gnxw_list = remove_duplicate_urls(gnxw('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/ckfpkdbldjmfbboginknjeijnkffjlof.jsp'))
        for gnxw_news in gnxw_list:
            try:
                gnxw_res = parse_news(gnxw_news)
                logger.info(gnxw_res['url'])
                save_return_value = save(gnxw_res)
                if save_return_value:
                    break
                logger.info('saving 国内新闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        fzyw_list = remove_duplicate_urls(fzyw('http://10.137.0.6:8080/ecdomain/framework/jinansrmjcy/cjjiifmddjmjbboginknjeijnkffjlof.jsp'))
        for fzyw_news in fzyw_list:
            try:
                fzyw_res = parse_news(fzyw_news)
                logger.info(fzyw_res['url'])
                save_return_value = save(fzyw_res)
                if save_return_value:
                    break
                logger.info('saving 法制要闻')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'jnsy'})