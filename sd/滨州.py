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


def bmdt(url):  # 部门动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentomknmhjbmgkcbbodkoijohpfaaoaecgh .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentomknmhjbmgkcbbodkoijohpfaaoaecgh tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'lbcffoogmgkabbodkoijohpfaaoaecgh',
                     'moduleID': 'omknmhjbmgkcbbodkoijohpfaaoaecgh',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/lbcffoogmgkabbodkoijohpfaaoaecgh/omknmhjbmgkcbbodkoijohpfaaoaecgh.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentomknmhjbmgkcbbodkoijohpfaaoaecgh .cxzy_list').items() if
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
                                                       '#newslistComponentenbfkhgmminjbbodkoijohpfaaoaecgh .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    # print first_page_table_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentenbfkhgmminjbbodkoijohpfaaoaecgh tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'oleiefbbminibbodkoijohpfaaoaecgh',
                     'moduleID': 'enbfkhgmminjbbodkoijohpfaaoaecgh',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/oleiefbbminibbodkoijohpfaaoaecgh/enbfkhgmminjbbodkoijohpfaaoaecgh.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentenbfkhgmminjbbodkoijohpfaaoaecgh .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def jcyw(url):  # 检察要闻
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
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'jnjgpfnbfchobbodimdigaolgjmolkjk',
                     'moduleID': 'lklmkjccfchobbodimdigaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk/lklmkjccfchobbodimdigaolgjmolkjk.do',
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
        'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
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
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'meapooclfcelbbodlcbjgaolgjmolkjk',
                     'moduleID': 'khkkhgebfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk/khkkhgebfceobbodlcbjgaolgjmolkjk.do',
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
            'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
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
                                                       '#newslistComponentpeoindppminhbbodkoijohpfaaoaecgh .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentpeoindppminhbbodkoijohpfaaoaecgh .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentpeoindppminhbbodkoijohpfaaoaecgh tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'jbnkggceminhbbodkoijohpfaaoaecgh',
                     'moduleID': 'peoindppminhbbodkoijohpfaaoaecgh',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/jbnkggceminhbbodkoijohpfaaoaecgh/peoindppminhbbodkoijohpfaaoaecgh.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentpeoindppminhbbodkoijohpfaaoaecgh .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentpeoindppminhbbodkoijohpfaaoaecgh .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def bmtz(url):  # 部门通知
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentpjbiklkdnppcbbodkfjjppchcmpncdfj .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentpjbiklkdnppcbbodkfjjppchcmpncdfj .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentpjbiklkdnppcbbodkfjjppchcmpncdfj tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'loghmmgjnppcbbodkfjjppchcmpncdfj',
                     'moduleID': 'pjbiklkdnppcbbodkfjjppchcmpncdfj',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/loghmmgjnppcbbodkfjjppchcmpncdfj/pjbiklkdnppcbbodkfjjppchcmpncdfj.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentpjbiklkdnppcbbodkfjjppchcmpncdfj .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentpjbiklkdnppcbbodkfjjppchcmpncdfj .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        # break
    return news_list


def xcbb(url):  # 宣传播报
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in
                                                   d(
                                                       '#newslistComponentodiibfcgoohibboekoablcphdeakabeh .cxzy_list').items()
                                                   if
                                                   i('a').attr('href') is not None])
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentodiibfcgoohibboekoablcphdeakabeh .cxzy_list').items() if
        i('a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    # print len(first_page_table_urls)
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentodiibfcgoohibboekoablcphdeakabeh tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'bzsrmjcy', 'pageID': 'odiglfjfoohibboekoablcphdeakabeh',
                     'moduleID': 'odiibfcgoohibboekoablcphdeakabeh',
                     'moreURI': '/ecdomain/framework/bzsrmjcy/odiglfjfoohibboekoablcphdeakabeh/odiibfcgoohibboekoablcphdeakabeh.do',
                     'var_temp': 'eepmiaheeppebbodlahcnhmaoeclmjka',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('a').attr('href') for i in post_d(
            '#newslistComponentodiibfcgoohibboekoablcphdeakabeh .cxzy_list').items() if
                                                       i('a').attr('href') is not None])
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.152.100:8080' + i('a').attr('onclick').replace('checkUser("', '').replace('")', '') for
            i
            in
            post_d('#newslistComponentodiibfcgoohibboekoablcphdeakabeh .cxzy_list').items() if
            i('a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
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
                            belong='滨州')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # bmdt('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/lbcffoogmgkabbodkoijohpfaaoaecgh.jsp')
    # jcdt('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/oleiefbbminibbodkoijohpfaaoaecgh.jsp')
    # jcyw('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp')
    # tztg('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp')
    # xxjb('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/jbnkggceminhbbodkoijohpfaaoaecgh.jsp')
    # bmtz('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/loghmmgjnppcbbodkfjjppchcmpncdfj.jsp')
    # xcbb('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/odiglfjfoohibboekoablcphdeakabeh.jsp')

    try:
        bmdt_news_list = remove_duplicate_urls(bmdt('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/lbcffoogmgkabbodkoijohpfaaoaecgh.jsp'))
        for bmdt_news in bmdt_news_list:
            try:
                bmdt_res = parse_news(bmdt_news)
                logger.info(bmdt_res['url'])
                save_return_value = save(bmdt_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        jcdt_news_list = remove_duplicate_urls(jcdt('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/oleiefbbminibbodkoijohpfaaoaecgh.jsp'))
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
        jcyw_news_list = remove_duplicate_urls(jcyw('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/jnjgpfnbfchobbodimdigaolgjmolkjk.jsp'))
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
        tztg_news_list = remove_duplicate_urls(tztg('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/meapooclfcelbbodlcbjgaolgjmolkjk.jsp'))
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
        xxjb_news_list = remove_duplicate_urls(xxjb('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/jbnkggceminhbbodkoijohpfaaoaecgh.jsp'))
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
        bmtz_news_list = remove_duplicate_urls(bmtz('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/loghmmgjnppcbbodkfjjppchcmpncdfj.jsp'))
        for bmtz_news in bmtz_news_list:
            try:
                bmtz_res = parse_news(bmtz_news)
                logger.info(bmtz_res['url'])
                save_return_value = save(bmtz_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        xcbb_news_list = remove_duplicate_urls(xcbb('http://10.137.152.100:8080/ecdomain/framework/bzsrmjcy/odiglfjfoohibboekoablcphdeakabeh.jsp'))
        for xcbb_news in xcbb_news_list:
            try:
                xcbb_res = parse_news(xcbb_news)
                logger.info(xcbb_res['url'])
                save_return_value = save(xcbb_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'bzsy'})