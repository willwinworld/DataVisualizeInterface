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


def jcyw(url):  # 检察要闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponenthpobkhbgcdidbboeilmgkieppbclkbff td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponenthpobkhbgcdidbboeilmgkieppbclkbff tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'tasrmjcy', 'pageID': 'hpnmomcecdidbboeilmgkieppbclkbff',
                     'moduleID': 'hpobkhbgcdidbboeilmgkieppbclkbff',
                     'moreURI': '/ecdomain/framework/tasrmjcy/hpnmomcecdidbboeilmgkieppbclkbff/hpobkhbgcdidbboeilmgkieppbclkbff.do',
                     'var_temp': 'nanaddhkllpdbboeiahejelkdgjpmajk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponenthpobkhbgcdidbboeilmgkieppbclkbff td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def sydt(url):  # 市院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentoeedkpkkoelcbboejlpekkihpmhejnlj td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentoeedkpkkoelcbboejlpekkihpmhejnlj tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'tasrmjcy', 'pageID': 'oeeapaiioelcbboejlpekkihpmhejnlj',
                     'moduleID': 'oeedkpkkoelcbboejlpekkihpmhejnlj',
                     'moreURI': '/ecdomain/framework/tasrmjcy/oeeapaiioelcbboejlpekkihpmhejnlj/oeedkpkkoelcbboejlpekkihpmhejnlj.do',
                     'var_temp': 'nanaddhkllpdbboeiahejelkdgjpmajk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentoeedkpkkoelcbboejlpekkihpmhejnlj td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def jcydt(url):  # 基层院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'tasrmjcy', 'pageID': 'ndnhnfpifelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'flpfefpffeljbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/tasrmjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn/flpfefpffeljbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'nanaddhkllpdbboeiahejelkdgjpmajk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def jcsdt(url):  # 检察室动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponenteemdmclmoeljbboejlpekkihpmhejnlj td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponenteemdmclmoeljbboejlpekkihpmhejnlj tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'tasrmjcy', 'pageID': 'eembckkloeljbboejlpekkihpmhejnlj',
                     'moduleID': 'eemdmclmoeljbboejlpekkihpmhejnlj',
                     'moreURI': '/ecdomain/framework/tasrmjcy/eembckkloeljbboejlpekkihpmhejnlj/eemdmclmoeljbboejlpekkihpmhejnlj.do',
                     'var_temp': 'nanaddhkllpdbboeiahejelkdgjpmajk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponenteemdmclmoeljbboejlpekkihpmhejnlj td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def tszs(url):  # 他山之石
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'tasrmjcy', 'pageID': 'nfmiflfkfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'ihnkgcnnfellbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/tasrmjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn/ihnkgcnnfellbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'nanaddhkllpdbboeiahejelkdgjpmajk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def zhxw(url):  # 综合新闻
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'tasrmjcy', 'pageID': 'ngkbfgdlfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'iabjecfhfelmbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/tasrmjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn/iabjecfhfelmbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'nanaddhkllpdbboeiahejelkdgjpmajk',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
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
                            belong='泰安')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # jcyw('http://10.137.176.5/ecdomain/framework/tasrmjcy/hpnmomcecdidbboeilmgkieppbclkbff.jsp')
    # sydt('http://10.137.176.5/ecdomain/framework/tasrmjcy/oeeapaiioelcbboejlpekkihpmhejnlj.jsp')
    # jcydt('http://10.137.176.5/ecdomain/framework/tasrmjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn.jsp')
    # jcsdt('http://10.137.176.5/ecdomain/framework/tasrmjcy/eembckkloeljbboejlpekkihpmhejnlj.jsp')
    # tszs('http://10.137.176.5/ecdomain/framework/tasrmjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn.jsp')
    # zhxw('http://10.137.176.5/ecdomain/framework/tasrmjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn.jsp')

    try:
        jcyw_news_list = remove_duplicate_urls(jcyw('http://10.137.176.5/ecdomain/framework/tasrmjcy/hpnmomcecdidbboeilmgkieppbclkbff.jsp'))
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
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.176.5/ecdomain/framework/tasrmjcy/oeeapaiioelcbboejlpekkihpmhejnlj.jsp'))
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
        jcydt_news_list = remove_duplicate_urls(jcydt('http://10.137.176.5/ecdomain/framework/tasrmjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn.jsp'))
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
        jcsdt_news_list = remove_duplicate_urls(jcsdt('http://10.137.176.5/ecdomain/framework/tasrmjcy/eembckkloeljbboejlpekkihpmhejnlj.jsp'))
        for jcsdt_news in jcsdt_news_list:
            try:
                jcsdt_res = parse_news(jcsdt_news)
                logger.info(jcsdt_res['url'])
                save_return_value = save(jcsdt_res)
                if save_return_value:
                    break
                logger.info('saving 检察室动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        tszs_news_list = remove_duplicate_urls(tszs('http://10.137.176.5/ecdomain/framework/tasrmjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn.jsp'))
        for tszs_news in tszs_news_list:
            try:
                tszs_res = parse_news(tszs_news)
                logger.info(tszs_res['url'])
                save_return_value = save(tszs_res)
                if save_return_value:
                    break
                logger.info('saving 他山之石')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        zhxw_news_list = remove_duplicate_urls(zhxw('http://10.137.176.5/ecdomain/framework/tasrmjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn.jsp'))
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

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'tasy'})