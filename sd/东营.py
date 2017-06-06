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
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentkleilopabnmnbboejeneocnlcepnhdfo td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i('.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.188.53:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for i
        in
        d('#newslistComponentkleilopabnmnbboejeneocnlcepnhdfo td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentkleilopabnmnbboejeneocnlcepnhdfo tr').eq(-1).find('a').eq(-1).attr(
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
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentkleilopabnmnbboejeneocnlcepnhdfo td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i('.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.188.53:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentkleilopabnmnbboejeneocnlcepnhdfo td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def dwjs(url):  # 队伍建设
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentomknmhjbmgkcbbodkoijohpfaaoaecgh td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    first_page_table_encrypt_urls = remove_duplicate_urls([
        'http://10.137.188.53:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentomknmhjbmgkcbbodkoijohpfaaoaecgh td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    return news_list


def lzjs(url):  # 廉政建设
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentckajbgomcfodbboejeneocnlcepnhdfo td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentckajbgomcfodbboejeneocnlcepnhdfo tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dysjcy2017', 'pageID': 'mlcjfokdcfocbboejeneocnlcepnhdfo',
                     'moduleID': 'ckajbgomcfodbboejeneocnlcepnhdfo',
                     'moreURI': '/ecdomain/framework/dysjcy2017/mlcjfokdcfocbboejeneocnlcepnhdfo/ckajbgomcfodbboejeneocnlcepnhdfo.do',
                     'var_temp': 'hmmlcmonocbebbodiacnlmllogadpifn',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentckajbgomcfodbboejeneocnlcepnhdfo td').items() if
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
        '#newslistComponenteoaimfeibnndbboejeneocnlcepnhdfo td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponenteoaimfeibnndbboejeneocnlcepnhdfo tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dysjcy2017', 'pageID': 'ddchpiogbnndbboejeneocnlcepnhdfo',
                     'moduleID': 'eoaimfeibnndbboejeneocnlcepnhdfo',
                     'moreURI': '/ecdomain/framework/dysjcy2017/ddchpiogbnndbboejeneocnlcepnhdfo/eoaimfeibnndbboejeneocnlcepnhdfo.do',
                     'var_temp': 'hmmlcmonocbebbodiacnlmllogadpifn',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponenteoaimfeibnndbboejeneocnlcepnhdfo td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
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
        'http://10.137.188.53:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '') for
        i
        in
        d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
        i('.cxzy_list a').attr('onclick') is not None])  # 加密url
    # print first_page_table_urls
    # print first_page_table_encrypt_urls
    news_list.extend(first_page_table_urls)
    news_list.extend(first_page_table_encrypt_urls)
    contain_page_num_url = d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dysjcy2017', 'pageID': 'meapooclfcelbbodlcbjgaolgjmolkjk',
                     'moduleID': 'khkkhgebfceobbodlcbjgaolgjmolkjk',
                     'moreURI': '/ecdomain/framework/dysjcy2017/meapooclfcelbbodlcbjgaolgjmolkjk/khkkhgebfceobbodlcbjgaolgjmolkjk.do',
                     'var_temp': 'hmmlcmonocbebbodiacnlmllogadpifn',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        other_page_table_encrypt_urls = remove_duplicate_urls([
            'http://10.137.188.53:8080' + i('.cxzy_list a').attr('onclick').replace('checkUser("', '').replace('")', '')
            for i in
            post_d('#newslistComponentkhkkhgebfceobbodlcbjgaolgjmolkjk td').items() if
            i('.cxzy_list a').attr('onclick') is not None])  # 加密url
        # print other_page_table_urls
        # print other_page_table_encrypt_urls
        news_list.extend(other_page_table_urls)
        news_list.extend(other_page_table_encrypt_urls)
        # break
    return news_list


def xqydt(url):  # 县区院动态
    news_list = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in d(
        '#newslistComponentmancbcneboafbboejeneocnlcepnhdfo td').items() if
                                                   i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                       '.cxzy_list a').attr('href') is not None])  # 要去重
    # print first_page_table_urls
    news_list.extend(first_page_table_urls)
    contain_page_num_url = d('#newslistComponentmancbcneboafbboejeneocnlcepnhdfo tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    for idx in xrange(2, total_page_num + 1):
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'dysjcy2017', 'pageID': 'keokpkacboafbboejeneocnlcepnhdfo',
                     'moduleID': 'mancbcneboafbboejeneocnlcepnhdfo',
                     'moreURI': '/ecdomain/framework/dysjcy2017/keokpkacboafbboejeneocnlcepnhdfo/mancbcneboafbboejeneocnlcepnhdfo.do',
                     'var_temp': 'hmmlcmonocbebbodiacnlmllogadpifn',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 4))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_table_urls = remove_duplicate_urls([i('.cxzy_list a').attr('href') for i in post_d(
            '#newslistComponentmancbcneboafbboejeneocnlcepnhdfo td').items() if
                                                       i('.cxzy_list a').attr('href') != 'javascript:void(0)' and i(
                                                           '.cxzy_list a').attr('href') is not None])  # 要去重
        # print other_page_table_urls
        news_list.extend(other_page_table_urls)
        # break
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
                          belong='东营')
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
                      belong='东营')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    # ldjh('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/ikalkojobnmnbboejeneocnlcepnhdfo.jsp')
    # dwjs('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/lbcffoogmgkabbodkoijohpfaaoaecgh.jsp')
    # lzjs('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/mlcjfokdcfocbboejeneocnlcepnhdfo.jsp')
    # sydt('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/ddchpiogbnndbboejeneocnlcepnhdfo.jsp')
    # tztg('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/meapooclfcelbbodlcbjgaolgjmolkjk.jsp')
    # xqydt('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/keokpkacboafbboejeneocnlcepnhdfo.jsp')

    try:
        ldjh_news_list = remove_duplicate_urls(ldjh('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/ikalkojobnmnbboejeneocnlcepnhdfo.jsp'))
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
        dwjs_news_list = remove_duplicate_urls(dwjs('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/lbcffoogmgkabbodkoijohpfaaoaecgh.jsp'))
        for dwjs_news in dwjs_news_list:
            try:
                dwjs_res = parse_news(dwjs_news)
                logger.info(dwjs_res['url'])
                save_return_value = save(dwjs_res)
                if save_return_value:
                    break
                logger.info('saving 队伍建设')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        lzjs_news_list = remove_duplicate_urls(lzjs('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/mlcjfokdcfocbboejeneocnlcepnhdfo.jsp'))
        for lzjs_news in lzjs_news_list:
            try:
                lzjs_res = parse_news(lzjs_news)
                logger.info(lzjs_res['url'])
                save_return_value = save(lzjs_res)
                if save_return_value:
                    break
                logger.info('saving 廉政建设')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        sydt_news_list = remove_duplicate_urls(sydt('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/ddchpiogbnndbboejeneocnlcepnhdfo.jsp'))
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
        tztg_news_list = remove_duplicate_urls(tztg('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/meapooclfcelbbodlcbjgaolgjmolkjk.jsp'))
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
        xqydt_news_list = remove_duplicate_urls(xqydt('http://10.137.188.53:8080/ecdomain/framework/dysjcy2017/keokpkacboafbboejeneocnlcepnhdfo.jsp'))
        for xqydt_news in xqydt_news_list:
            try:
                xqydt_res = parse_news(xqydt_news)
                logger.info(xqydt_res['url'])
                save_return_value = save(xqydt_res)
                if save_return_value:
                    break
                logger.info('saving 县区院动态')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'dysy'})