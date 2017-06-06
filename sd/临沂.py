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


def jcyw(url):  # 检察要闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentmpdmcoeeacfjbboelhflnkogmhkpdopg .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentmpdmcoeeacfjbboelhflnkogmhkpdopg tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'mpcmepmcacfjbboelhflnkogmhkpdopg',
                     'moduleID': 'mpdmcoeeacfjbboelhflnkogmhkpdopg',
                     'moreURI': '/ecdomain/framework/linysrmjcy/mpcmepmcacfjbboelhflnkogmhkpdopg/mpdmcoeeacfjbboelhflnkogmhkpdopg.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentmpdmcoeeacfjbboelhflnkogmhkpdopg .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def sydt(url):  # 市院动态
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
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'ofnlpaldfceobbodlcbjgaolgjmolkjk',
                     'moduleID': 'aegbnaeefcepbbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/linysrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk/aegbnaeefcepbbodlcbjgaolgjmolkjk.do',
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
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentlklmkjccfchobbodimdigaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'jnjgpfnbfchobbodimdigaolgjmolkjk',
                     'moduleID': 'lklmkjccfchobbodimdigaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/linysrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk/lklmkjccfchobbodimdigaolgjmolkjk.do',
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
        news_list.extend(other_page_table_urls)
        # print other_page_table_urls
        # break
    return news_list


def xqydt(url):  # 县区院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponenthgfgeifpadbfbboelhflnkogmhkpdopg .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponenthgfgeifpadbfbboelhflnkogmhkpdopg tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'hgfdlaenadbfbboelhflnkogmhkpdopg',
                     'moduleID': 'hgfgeifpadbfbboelhflnkogmhkpdopg',
                     'moreURI': '/ecdomain/framework/linysrmjcy/hgfdlaenadbfbboelhflnkogmhkpdopg/hgfgeifpadbfbboelhflnkogmhkpdopg.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponenthgfgeifpadbfbboelhflnkogmhkpdopg .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def xxjb(url):  # 信息简报
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentibkcehpiadbfbboelhflnkogmhkpdopg .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentibkcehpiadbfbboelhflnkogmhkpdopg tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'ibjpngpgadbfbboelhflnkogmhkpdopg',
                     'moduleID': 'ibkcehpiadbfbboelhflnkogmhkpdopg',
                     'moreURI': '/ecdomain/framework/linysrmjcy/ibjpngpgadbfbboelhflnkogmhkpdopg/ibkcehpiadbfbboelhflnkogmhkpdopg.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentibkcehpiadbfbboelhflnkogmhkpdopg .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def dwjs(url):  # 队伍建设
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponenthlaagpicadbfbboelhflnkogmhkpdopg .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponenthlaagpicadbfbboelhflnkogmhkpdopg tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'hkpnpoiaadbfbboelhflnkogmhkpdopg',
                     'moduleID': 'hlaagpicadbfbboelhflnkogmhkpdopg',
                     'moreURI': '/ecdomain/framework/linysrmjcy/hkpnpoiaadbfbboelhflnkogmhkpdopg/hlaagpicadbfbboelhflnkogmhkpdopg.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponenthlaagpicadbfbboelhflnkogmhkpdopg .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def lljs(url):  # 理论建设
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentfgdmoedgbndjbboeipiaiknjlaafhkfp .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentfgdmoedgbndjbboeipiaiknjlaafhkfp tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'fgdiomjfbndjbboeipiaiknjlaafhkfp',
                     'moduleID': 'fgdmoedgbndjbboeipiaiknjlaafhkfp',
                     'moreURI': '/ecdomain/framework/linysrmjcy/fgdiomjfbndjbboeipiaiknjlaafhkfp/fgdmoedgbndjbboeipiaiknjlaafhkfp.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentfgdmoedgbndjbboeipiaiknjlaafhkfp .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def jjyw(url):  # 经济要闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentepgcooffokjmbboglkjhjmagnjpolpli .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentepgcooffokjmbboglkjhjmagnjpolpli tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'linysrmjcy', 'pageID': 'epfpobbeokjmbboglkjhjmagnjpolpli',
                     'moduleID': 'epgcooffokjmbboglkjhjmagnjpolpli',
                     'moreURI': '/ecdomain/framework/linysrmjcy/epfpobbeokjmbboglkjhjmagnjpolpli/epgcooffokjmbboglkjhjmagnjpolpli.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentepgcooffokjmbboglkjhjmagnjpolpli .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
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
                            belong='临沂')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # jcyw('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/mpcmepmcacfjbboelhflnkogmhkpdopg.jsp')
    # sydt('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp')
    # tpxw('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp')
    # xqydt('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/hgfdlaenadbfbboelhflnkogmhkpdopg.jsp')
    # xxjb('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/ibjpngpgadbfbboelhflnkogmhkpdopg.jsp')
    # dwjs('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/hkpnpoiaadbfbboelhflnkogmhkpdopg.jsp')
    # lljs('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/fgdiomjfbndjbboeipiaiknjlaafhkfp.jsp')
    # jjyw('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/epfpobbeokjmbboglkjhjmagnjpolpli.jsp')

    try:
        jcyw_news_list = remove_duplicate_urls(jcyw('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/mpcmepmcacfjbboelhflnkogmhkpdopg.jsp'))
        for jcyw_news in jcyw_news_list:
            try:
                jcyw_res = parse_news(jcyw_news)
                logger.info(jcyw_res['url'])
                save_return_value = save(jcyw_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp'))
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
        tpxw_news_list = remove_duplicate_urls(tpxw('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp'))
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
        xqydt_news_list = remove_duplicate_urls(xqydt('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/hgfdlaenadbfbboelhflnkogmhkpdopg.jsp'))
        for xqydt_news in xqydt_news_list:
            try:
                xqydt_res = parse_news(xqydt_news)
                logger.info(xqydt_res['url'])
                save_return_value = save(xqydt_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        xxjb_news_list = remove_duplicate_urls(xxjb('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/ibjpngpgadbfbboelhflnkogmhkpdopg.jsp'))
        for xxjb_news in xxjb_news_list:
            try:
                xxjb_res = parse_news(xxjb_news)
                logger.info(xxjb_res['url'])
                save_return_value = save(xxjb_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        dwjs_news_list = remove_duplicate_urls(dwjs('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/hkpnpoiaadbfbboelhflnkogmhkpdopg.jsp'))
        for dwjs_news in dwjs_news_list:
            try:
                dwjs_res = parse_news(dwjs_news)
                logger.info(dwjs_res['url'])
                save_return_value = save(dwjs_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        lljs_news_list = remove_duplicate_urls(lljs('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/fgdiomjfbndjbboeipiaiknjlaafhkfp.jsp'))
        for lljs_news in lljs_news_list:
            try:
                lljs_res = parse_news(lljs_news)
                logger.info(lljs_res['url'])
                save_return_value = save(lljs_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jjyw_news_list = remove_duplicate_urls(jjyw('http://www.ly.sd.pro/ecdomain/framework/linysrmjcy/epfpobbeokjmbboglkjhjmagnjpolpli.jsp'))
        for jjyw_news in jjyw_news_list:
            try:
                jjyw_res = parse_news(jjyw_news)
                logger.info(jjyw_res['url'])
                save_return_value = save(jjyw_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'lysy'})