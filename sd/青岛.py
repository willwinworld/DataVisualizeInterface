#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import requests
from random import uniform
from pyquery import PyQuery as Pq
from dialogue.dumblog import dlog
from dateutil.parser import parse
from sd_model import Document
from peewee import IntegrityError

logger = dlog(__file__, console='debug')


def add_to_redis(queue_name, element):
    if isinstance(element, list):
        for e in element:
            queue_name.put(e)
    else:
        queue_name.put(element)


def remove_duplicate_urls(seq):  # 对列表进行去重,并且保持列表顺序
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def sydt(url):  # 省院动态
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn .ALink').items()]
    # print '###'
    # print first_page_links
    # print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': 'ndnhnfpifelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'flpfefpffeljbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/sdjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn/flpfefpffeljbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn .ALink').items()]
        # print '@@@'
        # print other_page_links
        # print '@@@'
        news_list.extend(other_page_links)
    # print news_list
    logger.info(len(news_list))
    return news_list


def shiydt(url):  # 市院动态
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk .ALink').items()]
    # print '###'
    # print first_page_links
    # print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'qdsrmjcy', 'pageID': 'ofnlpaldfceobbodlcbjgaolgjmolkjk',
                     'moduleID': 'aegbnaeefcepbbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/qdsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk/aegbnaeefcepbbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentaegbnaeefcepbbodlcbjgaolgjmolkjk .ALink').items()]
        # print '@@@'
        # print other_page_links
        # print '@@@'
        news_list.extend(other_page_links)
    # print news_list
    logger.info(len(news_list))
    return news_list


def jcydt(url):  # 基层院动态
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentaaneipmiokhnbbofjlinjkgehgnbbino tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentaaneipmiokhnbbofjlinjkgehgnbbino .ALink').items()]
    # print '###'
    # print first_page_links
    # print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'qdsrmjcy', 'pageID': 'aanaccphokhnbbofjlinjkgehgnbbino',
                     'moduleID': 'aaneipmiokhnbbofjlinjkgehgnbbino',
                     'moreURI': '/ecdomain/framework/qdsrmjcy/aanaccphokhnbbofjlinjkgehgnbbino/aaneipmiokhnbbofjlinjkgehgnbbino.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentaaneipmiokhnbbofjlinjkgehgnbbino .ALink').items()]
        # print '@@@'
        # print other_page_links
        # print '@@@'
        news_list.extend(other_page_links)
        # break
    # print news_list
    logger.info(len(news_list))
    return news_list


def zhxw(url):  # 综合新闻
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk .ALink').items()]
    # print '###'
    # print first_page_links
    # print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'qdsrmjcy', 'pageID': 'ncihclbofcenbbodlcbjgaolgjmolkjk',
                     'moduleID': 'ebacbimpfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/qdsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk/ebacbimpfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentebacbimpfceobbodlcbjgaolgjmolkjk .ALink').items()]
        # print '@@@'
        # print other_page_links
        # print '@@@'
        news_list.extend(other_page_links)
        # break
    # print news_list
    logger.info(len(news_list))
    return news_list


def fzzx(url):  # 法制在线
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentdhlceagkppkkbbofiihdpjjmdnnkmglg tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentdhlceagkppkkbbofiihdpjjmdnnkmglg .ALink').items()]
    # print '###'
    # print first_page_links
    # print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'qdsrmjcy', 'pageID': 'dhkpkifippkkbbofiihdpjjmdnnkmglg',
                     'moduleID': 'dhlceagkppkkbbofiihdpjjmdnnkmglg',
                     'moreURI': '/ecdomain/framework/qdsrmjcy/dhkpkifippkkbbofiihdpjjmdnnkmglg/dhlceagkppkkbbofiihdpjjmdnnkmglg.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentdhlceagkppkkbbofiihdpjjmdnnkmglg .ALink').items()]
        # print '@@@'
        # print other_page_links
        # print '@@@'
        news_list.extend(other_page_links)
        # break
    # print news_list
    logger.info(len(news_list))
    return news_list


def jcck(url):  # 检察参考
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponenteegpinmpppklbbofiihdpjjmdnnkmglg tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponenteegpinmpppklbbofiihdpjjmdnnkmglg .ALink').items()]
    # print '###'
    # print first_page_links
    # print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'qdsrmjcy', 'pageID': 'eegoahcnppklbbofiihdpjjmdnnkmglg',
                     'moduleID': 'eegpinmpppklbbofiihdpjjmdnnkmglg',
                     'moreURI': '/ecdomain/framework/qdsrmjcy/eegoahcnppklbbofiihdpjjmdnnkmglg/eegpinmpppklbbofiihdpjjmdnnkmglg.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponenteegpinmpppklbbofiihdpjjmdnnkmglg .ALink').items()]
        # print '@@@'
        # print other_page_links
        # print '@@@'
        news_list.extend(other_page_links)
    # print news_list
    logger.info(len(news_list))
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
    pubtime = str(parse(d('#newsall td').eq(2).text().replace(u'发布时间：', ''), fuzzy=True))
    # editor = d('#newsall td').eq(4).text().replace(u'审核人：', '')
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
              'content': content, 'img_url': img_url, 'url': url}
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
                            belong='青岛')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://10.37.0.5/ecdomain/framework/sdjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn.jsp'))
        for sydt_news in sydt_news_list:
            try:
                sydt_res = parse_news(sydt_news)
                logger.info(sydt_res['url'])
                save_return_value = save(sydt_res)
                if save_return_value:
                    break
                logger.info('saving 省院动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        shiydt_news_list = remove_duplicate_urls(shiydt('http://10.137.16.27/ecdomain/framework/qdsrmjcy/ofnlpaldfceobbodlcbjgaolgjmolkjk.jsp'))
        for shiydt_news in shiydt_news_list:
            try:
                shiydt_res = parse_news(shiydt_news)
                logger.info(shiydt_res['url'])
                save_return_value = save(shiydt_res)
                if save_return_value:
                    break
                logger.info('saving 市院动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcydt_news_list = remove_duplicate_urls(jcydt('http://10.137.16.27/ecdomain/framework/qdsrmjcy/aanaccphokhnbbofjlinjkgehgnbbino.jsp'))
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
        zhxw_news_list = remove_duplicate_urls(zhxw('http://10.137.16.27/ecdomain/framework/qdsrmjcy/ncihclbofcenbbodlcbjgaolgjmolkjk.jsp'))
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
        fzzx_news_list = remove_duplicate_urls(fzzx('http://10.137.16.27/ecdomain/framework/qdsrmjcy/dhkpkifippkkbbofiihdpjjmdnnkmglg.jsp'))
        for fzzx_news in fzzx_news_list:
            try:
                fzzx_res = parse_news(fzzx_news)
                logger.info(fzzx_res['url'])
                save_return_value = save(fzzx_res)
                if save_return_value:
                    break
                logger.info('saving 法治在线')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcck_news_list = remove_duplicate_urls(jcck('http://10.137.16.27/ecdomain/framework/qdsrmjcy/eegoahcnppklbbofiihdpjjmdnnkmglg.jsp'))
        for jcck_news in jcck_news_list:
            try:
                jcck_res = parse_news(jcck_news)
                logger.info(jcck_res['url'])
                save_return_value = save(jcck_res)
                if save_return_value:
                    break
                logger.info('saving 检察参考')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'qdsy'})