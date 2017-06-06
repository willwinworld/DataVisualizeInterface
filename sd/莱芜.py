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


def jcdt(url):  # 基层动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentfhenmbhpfelkbbocifbbmbfldfhbdbpn .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentfhenmbhpfelkbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'lwsrmjcy', 'pageID': 'nelihbpjfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'fhenmbhpfelkbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/lwsrmjcy/nelihbpjfelebbocifbbmbfldfhbdbpn/fhenmbhpfelkbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'mbmneoaaenigbbocinjhkoalmphlecfg',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentfhenmbhpfelkbbocifbbmbfldfhbdbpn .cxzy_list').items() if
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
                                                       '#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'lwsrmjcy', 'pageID': 'ndnhnfpifelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'flpfefpffeljbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/lwsrmjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn/flpfefpffeljbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'mbmneoaaenigbbocinjhkoalmphlecfg',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn .cxzy_list').items() if
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
                                                       '#newslistComponentcebkpdcmfhlbbbociikmnglmgckkaphe td[style]').items()
                                                   if
                                                   i('a').attr('href') is not None])
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentcebkpdcmfhlbbbociikmnglmgckkaphe tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'lwsrmjcy', 'pageID': 'mdacfhenfhkpbbociikmnglmgckkaphe',
                     'moduleID': 'cebkpdcmfhlbbbociikmnglmgckkaphe',
                     'moreURI': '/ecdomain/framework/lwsrmjcy/mdacfhenfhkpbbociikmnglmgckkaphe/cebkpdcmfhlbbbociikmnglmgckkaphe.do',
                     'var_temp': 'mbmneoaaenigbbocinjhkoalmphlecfg',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentcebkpdcmfhlbbbociikmnglmgckkaphe td[style]').items() if
                                                       i('a').attr('href') is not None])
        news_list.extend(other_page_table_urls)
    return news_list


def jbxx(url):  # 简报信息
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.212.4:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'lwsrmjcy', 'pageID': 'nfmiflfkfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'ihnkgcnnfellbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/lwsrmjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn/ihnkgcnnfellbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'mbmneoaaenigbbocinjhkoalmphlecfg',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.212.4:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def zhxw(url):  # 综合新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.212.4:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'lwsrmjcy', 'pageID': 'ngkbfgdlfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'iabjecfhfelmbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/lwsrmjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn/iabjecfhfelmbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'mbmneoaaenigbbocinjhkoalmphlecfg',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.212.4:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn .cxzy_list').items() if
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
                            belong='莱芜')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # jcdt('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/nelihbpjfelebbocifbbmbfldfhbdbpn.jsp')
    # sydt('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn.jsp')
    # tpxw('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/mdacfhenfhkpbbociikmnglmgckkaphe.jsp')
    # jbxx('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn.jsp')
    # zhxw('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn.jsp')

    try:
        jcdt_news_list = remove_duplicate_urls(jcdt('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/nelihbpjfelebbocifbbmbfldfhbdbpn.jsp'))
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
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn.jsp'))
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
        tpxw_news_list = remove_duplicate_urls(tpxw('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/mdacfhenfhkpbbociikmnglmgckkaphe.jsp'))
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
        jbxx_news_list = remove_duplicate_urls(jbxx('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn.jsp'))
        for jbxx_news in jbxx_news_list:
            try:
                jbxx_res = parse_news(jbxx_news)
                logger.info(jbxx_res['url'])
                save_return_value = save(jbxx_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        zhxw_news_list = remove_duplicate_urls(zhxw('http://10.137.212.4:8080/ecdomain/framework/lwsrmjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn.jsp'))
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

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'lwsy'})
