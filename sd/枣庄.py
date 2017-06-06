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


def jcyq(url):  # 检察要情
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentaiidhbaldkdpbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr('href') != 'javascript:void(0)'])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.164.5' + i('.ALink').attr('onclick').replace('checkUser("', '').replace('")', '') for i
        in
        d('#newslistComponentaiidhbaldkdpbboejhfdmlkiedjpgcpn .cxzy_list').items() if
        i('.ALink').attr('onclick') is not None])  # 加密url
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentaiidhbaldkdpbboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'aiiabfkjdkdpbboejhfdmlkiedjpgcpn',
                     'moduleID': 'aiidhbaldkdpbboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/aiiabfkjdkdpbboejhfdmlkiedjpgcpn/aiidhbaldkdpbboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
        '#newslistComponentaiidhbaldkdpbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr('href') != 'javascript:void(0)'])
        other_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.164.5' + i('.ALink').attr('onclick').replace('checkUser("', '').replace('")', '') for i
        in
        post_d('#newslistComponentaiidhbaldkdpbboejhfdmlkiedjpgcpn .cxzy_list').items() if
        i('.ALink').attr('onclick') is not None])
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
    return news_list


def myds(url):  # 每月大事
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentpmoblikhdcejbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentpmoblikhdcejbboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'pmnodgdgdcejbboejhfdmlkiedjpgcpn',
                     'moduleID': 'pmoblikhdcejbboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/pmnodgdgdcejbboejhfdmlkiedjpgcpn/pmoblikhdcejbboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentpmoblikhdcejbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
        news_list.extend(other_page_table_urls)
    return news_list


def sydt(url):  # 市院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentnehfmefmdceebboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentnehfmefmdceebboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'nehbdahldceebboejhfdmlkiedjpgcpn',
                     'moduleID': 'nehfmefmdceebboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/nehbdahldceebboejhfdmlkiedjpgcpn/nehfmefmdceebboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentnehfmefmdceebboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
        news_list.extend(other_page_table_urls)
    return news_list


def jcdt(url):  # 基层动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentliinaigpdcefbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentliinaigpdcefbboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'liijdhnodcefbboejhfdmlkiedjpgcpn',
                     'moduleID': 'liinaigpdcefbboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/liijdhnodcefbboejhfdmlkiedjpgcpn/liinaigpdcefbboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentliinaigpdcefbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
        news_list.extend(other_page_table_urls)
    return news_list


def xxjb(url):  # 信息简报
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentknleihbddcembboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentknleihbddcembboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'knlbfcmcdcembboejhfdmlkiedjpgcpn',
                     'moduleID': 'knleihbddcembboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/knlbfcmcdcembboejhfdmlkiedjpgcpn/knleihbddcembboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentknleihbddcembboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
        news_list.extend(other_page_table_urls)
    return news_list


def ldjh(url):  # 领导讲话
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentpacnlnfgdcembboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentpacnlnfgdcembboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'packbdnfdcembboejhfdmlkiedjpgcpn',
                     'moduleID': 'pacnlnfgdcembboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/packbdnfdcembboejhfdmlkiedjpgcpn/pacnlnfgdcembboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentpacnlnfgdcembboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
        news_list.extend(other_page_table_urls)
    return news_list


def jcxc(url):  # 检察宣传/宣传报道
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentinkicheddcepbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentinkicheddcepbboejhfdmlkiedjpgcpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'inkfbkabdcepbboejhfdmlkiedjpgcpn',
                     'moduleID': 'inkicheddcepbboejhfdmlkiedjpgcpn',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/inkfbkabdcepbboejhfdmlkiedjpgcpn/inkicheddcepbboejhfdmlkiedjpgcpn.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentinkicheddcepbboejhfdmlkiedjpgcpn .cxzy_list').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
        news_list.extend(other_page_table_urls)
    return news_list


def tpxw(url):  # 图片新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in d(
        '#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk td[style]').items() if
                                                   i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                       'href') != 'javascript:void(0)'])  # 要去重
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'zzsrmjcy', 'pageID': 'jnjgpfnbfchobbodimdigaolgjmolkjk',
                     'moduleID': 'lklmkjccfchobbodimdigaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/zzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk/lklmkjccfchobbodimdigaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.ALink').attr('href') for i in post_d(
            '#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk td[style]').items() if
                                                       i('.ALink').attr('href') is not None and i('.ALink').attr(
                                                           'href') != 'javascript:void(0)'])
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
                            belong='枣庄')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # jcyq('http://10.137.164.5/ecdomain/framework/zzsrmjcy/aiiabfkjdkdpbboejhfdmlkiedjpgcpn.jsp')
    # myds('http://10.137.164.5/ecdomain/framework/zzsrmjcy/pmnodgdgdcejbboejhfdmlkiedjpgcpn.jsp')
    # sydt('http://10.137.164.5/ecdomain/framework/zzsrmjcy/nehbdahldceebboejhfdmlkiedjpgcpn.jsp')
    # jcdt('http://10.137.164.5/ecdomain/framework/zzsrmjcy/liijdhnodcefbboejhfdmlkiedjpgcpn.jsp')
    # xxjb('http://10.137.164.5/ecdomain/framework/zzsrmjcy/knlbfcmcdcembboejhfdmlkiedjpgcpn.jsp')
    # ldjh('http://10.137.164.5/ecdomain/framework/zzsrmjcy/packbdnfdcembboejhfdmlkiedjpgcpn.jsp')
    # jcxc('http://10.137.164.5/ecdomain/framework/zzsrmjcy/inkfbkabdcepbboejhfdmlkiedjpgcpn.jsp')
    # tpxw('http://10.137.164.5/ecdomain/framework/zzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp')

    try:
        jcyq_news_list = remove_duplicate_urls(jcyq('http://10.137.164.5/ecdomain/framework/zzsrmjcy/aiiabfkjdkdpbboejhfdmlkiedjpgcpn.jsp'))
        for jcyq_news in jcyq_news_list:
            try:
                jcyq_res = parse_news(jcyq_news)
                logger.info(jcyq_res['url'])
                save_return_value = save(jcyq_res)
                if save_return_value:
                    break
                logger.info('saving 检察要情')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        myds_news_list = remove_duplicate_urls(myds('http://10.137.164.5/ecdomain/framework/zzsrmjcy/pmnodgdgdcejbboejhfdmlkiedjpgcpn.jsp'))
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

    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.164.5/ecdomain/framework/zzsrmjcy/nehbdahldceebboejhfdmlkiedjpgcpn.jsp'))
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
        jcdt_news_list = remove_duplicate_urls(jcdt('http://10.137.164.5/ecdomain/framework/zzsrmjcy/liijdhnodcefbboejhfdmlkiedjpgcpn.jsp'))
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
        xxjb_news_list = remove_duplicate_urls(xxjb('http://10.137.164.5/ecdomain/framework/zzsrmjcy/knlbfcmcdcembboejhfdmlkiedjpgcpn.jsp'))
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
        ldjh_news_list = remove_duplicate_urls(ldjh('http://10.137.164.5/ecdomain/framework/zzsrmjcy/packbdnfdcembboejhfdmlkiedjpgcpn.jsp'))
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
        jcxc_news_list = remove_duplicate_urls(jcxc('http://10.137.164.5/ecdomain/framework/zzsrmjcy/inkfbkabdcepbboejhfdmlkiedjpgcpn.jsp'))
        for jcxc_news in jcxc_news_list:
            try:
                jcxc_res = parse_news(jcxc_news)
                logger.info(jcxc_res['url'])
                save_return_value = save(jcxc_res)
                if save_return_value:
                    break
                logger.info('saving 检察宣传')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tpxw_news_list = remove_duplicate_urls(tpxw('http://10.137.164.5/ecdomain/framework/zzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp'))
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

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'zzsy'})