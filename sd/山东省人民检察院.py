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
from dateutil.parser import parse


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


def get_module_urls(url):  # 获取所有标题链接
    r = requests.get(url)
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    urls = [{i.text(): i.attr('href')} for i in d('.nav a:gt(1)').items()]
    return urls


def ljyw(url): # 鲁检要闻
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    total_page_content = d('#newslistComponentehnddklifelhbbocifbbmbfldfhbdbpn #a41').attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', total_page_content)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_duplicate_links = [i('.cxzy_list .ALink').attr('href') for i in d('#newslistComponentehnddklifelhbbocifbbmbfldfhbdbpn tr').items() if i('.cxzy_list .ALink').attr('href') is not None]
    first_page_links = remove_duplicate_urls(first_page_duplicate_links)
    news_list.extend(first_page_links)  # 加入第一页url

    for idx in xrange(2, total_page_num+1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': 'ncpbbphhfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'ehnddklifelhbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/sdjcy/ncpbbphhfelebbocifbbmbfldfhbdbpn/ehnddklifelhbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_duplicate_links = [i('.cxzy_list .ALink').attr('href') for i in post_d('#newslistComponentehnddklifelhbbocifbbmbfldfhbdbpn tr').items() if i('.cxzy_list .ALink').attr('href') is not None]
        other_page_links = remove_duplicate_urls(other_page_duplicate_links)
        news_list.extend(other_page_links)
    #     break
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


def jcdt(url): # 检察动态
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    total_page_content = d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpnJspComponent #a118').attr('href')
    total_page_num = int(re.findall(r'pageNum=\d+', total_page_content)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                                  d('#newslistComponentflpfefpffeljbbocifbbmbfldfhbdbpn .ALink').items()]
    news_list.extend(first_page_links)  # 加入第一页url

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
        news_list.extend(other_page_links)
    print news_list
    logger.info(len(news_list))
    return news_list


def tszs(url):  # 他山之石
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr('href')  # 不通过id选择器进行总页数的抓取，因为id选择器可能会变
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn .ALink').items()]
    news_list.extend(first_page_links)  # 加入第一页url

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': 'nfmiflfkfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'ihnkgcnnfellbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/sdjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn/ihnkgcnnfellbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentihnkgcnnfellbbocifbbmbfldfhbdbpn .ALink').items()]
        print '@@@'
        print other_page_links
        news_list.extend(other_page_links)
    print news_list
    logger.info(len(news_list))
    return news_list


def myds(url):  # 每月大事
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponenthdblifokfcoibbockffejgpigkloknma tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponenthdblifokfcoibbockffejgpigkloknma .ALink').items()]
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': 'anoamcjiepdjbboclifklppkbkkligai',
                     'moduleID': 'hdblifokfcoibbockffejgpigkloknma',
                     'moreURI': '/ecdomain/framework/sdjcy/anoamcjiepdjbboclifklppkbkkligai/hdblifokfcoibbockffejgpigkloknma.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponenthdblifokfcoibbockffejgpigkloknma .ALink').items()]
        print other_page_links
        print '@@@'
        news_list.extend(other_page_links)
    print news_list
    logger.info(len(news_list))
    return news_list


def zhxw(url):  # 综合新闻
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_page_num_url = d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn tr').eq(-1).find('a').eq(-1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info(total_page_num)
    first_page_links = [i.attr('href') for i in
                        d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn .ALink').items()]
    print '###'
    print first_page_links
    print '###'
    news_list.extend(first_page_links)

    for idx in xrange(2, total_page_num + 1):  # post请求构造页数
        logger.info(idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': 'ngkbfgdlfelebbocifbbmbfldfhbdbpn',
                     'moduleID': 'iabjecfhfelmbbocifbbmbfldfhbdbpn',
                     'moreURI': '/ecdomain/framework/sdjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn/iabjecfhfelmbbocifbbmbfldfhbdbpn.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_links = [i.attr('href') for i in
                            post_d('#newslistComponentiabjecfhfelmbbocifbbmbfldfhbdbpn .ALink').items()]
        print '@@@'
        print other_page_links
        print '@@@'
        news_list.extend(other_page_links)
    print news_list
    logger.info(len(news_list))
    return news_list


def tztg(url):  # 通知通告
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_parent_node_value_url = d('iframe').eq(1).attr('src')
    parent_node_value = re.findall(r'currfolderid=\d+', contain_parent_node_value_url)[0].replace('currfolderid=', '')  # 数字
    page_url_value = re.findall(r'pageUrl=\w+', contain_parent_node_value_url)[0].replace('pageUrl=', '')  # 英文字母，如aegkjanjmdfhbbockgocljklfigblnmd
    print contain_parent_node_value_url
    print parent_node_value
    print page_url_value
    parent_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (page_url_value, parent_node_value, '通知通告')  # 构建父节点url
    contain_child_node_value_url = 'http://10.37.0.5/ecdomain/ecplatform/load_folder_nodes.do?type=folder&parentNodeId=root&parentNodeValue=%s&level=0&demin=null&_=' % parent_node_value
    contain_child_node_value_xml = requests.get(contain_child_node_value_url).content
    time.sleep(uniform(2, 6))
    xml_d = Pq(contain_child_node_value_xml).make_links_absolute(base_url=contain_child_node_value_url)
    child_node_value = xml_d('node').attr('value')  # 数字
    child_node_name = xml_d('node').attr('name')  # 文字，如内部信息
    child_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (page_url_value, child_node_value, child_node_name) # 构建子节点url
    print child_url

    # 开始抓取父节点，子节点的所有列表url
    parent_r = requests.get(parent_url)
    time.sleep(uniform(2, 6))
    parent_r.encoding = 'utf-8'
    parent_d = Pq(parent_r.content).make_links_absolute(base_url=url)
    parent_first_page_table_urls = [i.attr('href') for i in parent_d('#listTable td a').items() if i.attr('href') != 'javascript:void(0)']
    parent_first_page_table_encrypt_urls = ['http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in parent_d('#listTable td a').items() if i.attr('onclick') is not None]  # 加密url
    news_list.extend(parent_first_page_table_urls)
    news_list.extend(parent_first_page_table_encrypt_urls)
    print '###'
    print parent_first_page_table_urls
    print parent_first_page_table_encrypt_urls
    print len(parent_first_page_table_encrypt_urls)
    print '###'
    contain_parent_page_num_url = parent_d('#newslistComponentciigpdfkmdfhbbockgocljklfigblnmd tr').eq(-1).find('a').eq(-1).attr(
        'href')
    print '@@@'
    print contain_parent_page_num_url
    print '@@@'
    parent_total_page_num = int(re.findall(r'pageNum=\d+', contain_parent_page_num_url)[0].replace('pageNum=', ''))
    logger.info('parent total page: %s' % parent_total_page_num)
    for idx in xrange(2, parent_total_page_num+1):
        logger.info('parent idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'ciigpdfkmdfhbbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/aegkjanjmdfhbbockgocljklfigblnmd/ciigpdfkmdfhbbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': parent_node_value,
                     'pagination': 'true',
                     'currfolderName': '通知通告',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        parent_post_r = requests.post(parent_url, data=form_data)
        parent_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        parent_post_d = Pq(parent_post_r.content).make_links_absolute(base_url=url)
        parent_other_page_table_urls = [i.attr('href') for i in parent_post_d('#listTable td a').items() if i.attr('href') != 'javascript:void(0)']
        parent_other_page_table_encrypt_urls = ['http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in parent_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(parent_other_page_table_urls)
        news_list.extend(parent_other_page_table_encrypt_urls)
        print '$$$'
        print parent_other_page_table_urls
        print parent_other_page_table_encrypt_urls
        print '$$$'
    print news_list
    logger.info(len(news_list))

    # 开始抓取子节点，子节点的所有列表url
    child_r = requests.get(child_url)
    time.sleep(uniform(2, 6))
    child_r.encoding = 'utf-8'
    child_d = Pq(child_r.content).make_links_absolute(base_url=url)
    child_first_page_table_urls = [i.attr('href') for i in child_d('#listTable td a').items() if i.attr('href') != 'javascript:void(0)']
    child_first_page_table_encrypt_urls = ['http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in child_d('#listTable td a').items() if i.attr('onclick') is not None]
    print '%%%'
    print child_first_page_table_urls
    print child_first_page_table_encrypt_urls
    print '%%%'
    news_list.extend(child_first_page_table_urls)
    news_list.extend(child_first_page_table_encrypt_urls)
    contain_child_page_num_url = child_d('#newslistComponentciigpdfkmdfhbbockgocljklfigblnmd tr').eq(-1).find('a').eq(-1).attr(
        'href')
    child_total_page_num = int(re.findall(r'pageNum=\d+', contain_child_page_num_url)[0].replace('pageNum=', ''))
    logger.info('child total page num: %s' % child_total_page_num)
    for idx in xrange(2, child_total_page_num+1):
        logger.info('child idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'ciigpdfkmdfhbbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/aegkjanjmdfhbbockgocljklfigblnmd/ciigpdfkmdfhbbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': child_node_value,
                     'pagination': 'true',
                     'currfolderName': child_node_name,
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        child_post_r = requests.post(child_url, data=form_data)
        child_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        child_post_d = Pq(child_post_r.content).make_links_absolute(base_url=url)
        child_other_page_table_urls = [i.attr('href') for i in child_post_d('#listTable td a').items() if i.attr('href') != 'javascript:void(0)']
        child_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            child_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(child_other_page_table_urls)
        news_list.extend(child_other_page_table_encrypt_urls)
        print '^^^'
        print child_other_page_table_urls
        print child_other_page_table_encrypt_urls
        print '^^^'
    print news_list
    logger.info(len(news_list))
    return news_list


def ldjh(url):  # 领导讲话
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_parent_node_value_url = d('iframe').eq(1).attr('src')
    parent_node_value = re.findall(r'currfolderid=\d+', contain_parent_node_value_url)[0].replace('currfolderid=',
                                                                                                  '')  # 数字
    page_url_value = re.findall(r'pageUrl=\w+', contain_parent_node_value_url)[0].replace('pageUrl=',
                                                                                          '')  # 英文字母，如aegkjanjmdfhbbockgocljklfigblnmd
    print contain_parent_node_value_url
    print parent_node_value
    print page_url_value
    parent_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (
    page_url_value, parent_node_value, '领导讲话')  # 构建父节点url
    contain_child_node_value_url = 'http://10.37.0.5/ecdomain/ecplatform/load_folder_nodes.do?type=folder&parentNodeId=root&parentNodeValue=%s&level=0&demin=null&_=' % parent_node_value
    contain_child_node_value_xml = requests.get(contain_child_node_value_url).content
    time.sleep(uniform(2, 6))
    xml_d = Pq(contain_child_node_value_xml).make_links_absolute(base_url=contain_child_node_value_url)
    child_node_value = xml_d('node').attr('value')  # 数字
    child_node_name = xml_d('node').attr('name')  # 文字，如内部信息
    child_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (
    page_url_value, child_node_value, child_node_name)  # 构建子节点url
    print child_url

    # 开始抓取父节点，子节点的所有列表url
    parent_r = requests.get(parent_url)
    time.sleep(uniform(2, 6))
    parent_r.encoding = 'utf-8'
    parent_d = Pq(parent_r.content).make_links_absolute(base_url=url)
    parent_first_page_table_urls = [i.attr('href') for i in parent_d('#listTable td a').items() if
                                    i.attr('href') != 'javascript:void(0)']
    parent_first_page_table_encrypt_urls = [
        'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        parent_d('#listTable td a').items() if i.attr('onclick') is not None]  # 加密url
    news_list.extend(parent_first_page_table_urls)
    news_list.extend(parent_first_page_table_encrypt_urls)
    print '###'
    print parent_first_page_table_urls
    print parent_first_page_table_encrypt_urls
    print len(parent_first_page_table_encrypt_urls)
    print '###'
    contain_parent_page_num_url = parent_d('#newslistComponentojdclgkgmdejbbockgocljklfigblnmd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')  # newslistComponent + moduleID
    print '@@@'
    print contain_parent_page_num_url
    print '@@@'
    parent_total_page_num = int(re.findall(r'pageNum=\d+', contain_parent_page_num_url)[0].replace('pageNum=', ''))
    logger.info('parent total page: %s' % parent_total_page_num)
    for idx in xrange(2, parent_total_page_num + 1):
        logger.info('parent idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'ojdclgkgmdejbbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/najbfihmfcojbbockffejgpigkloknma/ojdclgkgmdejbbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': parent_node_value,
                     'pagination': 'true',
                     'currfolderName': '领导讲话',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        parent_post_r = requests.post(parent_url, data=form_data)
        parent_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        parent_post_d = Pq(parent_post_r.content).make_links_absolute(base_url=url)
        parent_other_page_table_urls = [i.attr('href') for i in parent_post_d('#listTable td a').items() if
                                        i.attr('href') != 'javascript:void(0)']
        parent_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            parent_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(parent_other_page_table_urls)
        news_list.extend(parent_other_page_table_encrypt_urls)
        print '$$$'
        print parent_other_page_table_urls
        print parent_other_page_table_encrypt_urls
        print '$$$'
    print news_list
    logger.info(len(news_list))

    # 开始抓取子节点，子节点的所有列表url
    child_r = requests.get(child_url)
    time.sleep(uniform(2, 6))
    child_r.encoding = 'utf-8'
    child_d = Pq(child_r.content).make_links_absolute(base_url=url)
    child_first_page_table_urls = [i.attr('href') for i in child_d('#listTable td a').items() if
                                   i.attr('href') != 'javascript:void(0)']
    child_first_page_table_encrypt_urls = [
        'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        child_d('#listTable td a').items() if i.attr('onclick') is not None]
    print '%%%'
    print child_first_page_table_urls
    print child_first_page_table_encrypt_urls
    print '%%%'
    news_list.extend(child_first_page_table_urls)
    news_list.extend(child_first_page_table_encrypt_urls)
    contain_child_page_num_url = child_d('#newslistComponentojdclgkgmdejbbockgocljklfigblnmd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    child_total_page_num = int(re.findall(r'pageNum=\d+', contain_child_page_num_url)[0].replace('pageNum=', ''))
    logger.info('child total page num: %s' % child_total_page_num)
    for idx in xrange(2, child_total_page_num + 1):
        logger.info('child idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'ojdclgkgmdejbbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/najbfihmfcojbbockffejgpigkloknma/ojdclgkgmdejbbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': child_node_value,
                     'pagination': 'true',
                     'currfolderName': child_node_name,
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        child_post_r = requests.post(child_url, data=form_data)
        child_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        child_post_d = Pq(child_post_r.content).make_links_absolute(base_url=url)
        child_other_page_table_urls = [i.attr('href') for i in child_post_d('#listTable td a').items() if
                                       i.attr('href') != 'javascript:void(0)']
        child_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            child_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(child_other_page_table_urls)
        news_list.extend(child_other_page_table_encrypt_urls)
        print '^^^'
        print child_other_page_table_urls
        print child_other_page_table_encrypt_urls
        print '^^^'
    print news_list
    logger.info(len(news_list))
    return news_list


def sywj(url): # 省院文件
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_parent_node_value_url = d('iframe').eq(1).attr('src')
    parent_node_value = re.findall(r'currfolderid=\d+', contain_parent_node_value_url)[0].replace('currfolderid=',
                                                                                                  '')  # 数字
    page_url_value = re.findall(r'pageUrl=\w+', contain_parent_node_value_url)[0].replace('pageUrl=',
                                                                                          '')  # 英文字母，如aegkjanjmdfhbbockgocljklfigblnmd
    print contain_parent_node_value_url
    print parent_node_value
    print page_url_value
    parent_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (
    page_url_value, parent_node_value, '省院文件')  # 构建父节点url
    contain_child_node_value_url = 'http://10.37.0.5/ecdomain/ecplatform/load_folder_nodes.do?type=folder&parentNodeId=root&parentNodeValue=%s&level=0&demin=null&_=' % parent_node_value
    contain_child_node_value_xml = requests.get(contain_child_node_value_url).content
    time.sleep(uniform(2, 6))
    xml_d = Pq(contain_child_node_value_xml).make_links_absolute(base_url=contain_child_node_value_url)
    child_node_value = xml_d('node').attr('value')  # 数字
    child_node_name = xml_d('node').attr('name')  # 文字，如内部信息
    child_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (
    page_url_value, child_node_value, child_node_name)  # 构建子节点url
    print child_url

    # 开始抓取父节点，子节点的所有列表url
    parent_r = requests.get(parent_url)
    time.sleep(uniform(2, 6))
    parent_r.encoding = 'utf-8'
    parent_d = Pq(parent_r.content).make_links_absolute(base_url=url)
    parent_first_page_table_urls = [i.attr('href') for i in parent_d('#listTable td a').items() if
                                    i.attr('href') != 'javascript:void(0)']
    parent_first_page_table_encrypt_urls = [
        'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        parent_d('#listTable td a').items() if i.attr('onclick') is not None]  # 加密url
    news_list.extend(parent_first_page_table_urls)
    news_list.extend(parent_first_page_table_encrypt_urls)
    print '###'
    print parent_first_page_table_urls
    print parent_first_page_table_encrypt_urls
    print len(parent_first_page_table_encrypt_urls)
    print '###'
    contain_parent_page_num_url = parent_d('#newslistComponentplbccenkmdelbbockgocljklfigblnmd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    print '@@@'
    print contain_parent_page_num_url
    print '@@@'
    parent_total_page_num = int(re.findall(r'pageNum=\d+', contain_parent_page_num_url)[0].replace('pageNum=', ''))
    logger.info('parent total page: %s' % parent_total_page_num)
    for idx in xrange(2, parent_total_page_num + 1):
        logger.info('parent idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'plbccenkmdelbbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/gdmjokdafdngbbockfljijcbihpdiifa/plbccenkmdelbbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': parent_node_value,
                     'pagination': 'true',
                     'currfolderName': '省院文件',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        parent_post_r = requests.post(parent_url, data=form_data)
        parent_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        parent_post_d = Pq(parent_post_r.content).make_links_absolute(base_url=url)
        parent_other_page_table_urls = [i.attr('href') for i in parent_post_d('#listTable td a').items() if
                                        i.attr('href') != 'javascript:void(0)']
        parent_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            parent_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(parent_other_page_table_urls)
        news_list.extend(parent_other_page_table_encrypt_urls)
        print '$$$'
        print parent_other_page_table_urls
        print parent_other_page_table_encrypt_urls
        print '$$$'
    print news_list
    logger.info(len(news_list))

    # 开始抓取子节点，子节点的所有列表url
    child_r = requests.get(child_url)
    time.sleep(uniform(2, 6))
    child_r.encoding = 'utf-8'
    child_d = Pq(child_r.content).make_links_absolute(base_url=url)
    child_first_page_table_urls = [i.attr('href') for i in child_d('#listTable td a').items() if
                                   i.attr('href') != 'javascript:void(0)']
    child_first_page_table_encrypt_urls = [
        'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        child_d('#listTable td a').items() if i.attr('onclick') is not None]
    print '%%%'
    print child_first_page_table_urls
    print child_first_page_table_encrypt_urls
    print '%%%'
    news_list.extend(child_first_page_table_urls)
    news_list.extend(child_first_page_table_encrypt_urls)
    contain_child_page_num_url = child_d('#newslistComponentplbccenkmdelbbockgocljklfigblnmd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    child_total_page_num = int(re.findall(r'pageNum=\d+', contain_child_page_num_url)[0].replace('pageNum=', ''))
    logger.info('child total page num: %s' % child_total_page_num)
    for idx in xrange(2, child_total_page_num + 1):
        logger.info('child idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'plbccenkmdelbbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/gdmjokdafdngbbockfljijcbihpdiifa/plbccenkmdelbbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': child_node_value,
                     'pagination': 'true',
                     'currfolderName': child_node_name,
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        child_post_r = requests.post(child_url, data=form_data)
        child_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        child_post_d = Pq(child_post_r.content).make_links_absolute(base_url=url)
        child_other_page_table_urls = [i.attr('href') for i in child_post_d('#listTable td a').items() if
                                       i.attr('href') != 'javascript:void(0)']
        child_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            child_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(child_other_page_table_urls)
        news_list.extend(child_other_page_table_encrypt_urls)
        print '^^^'
        print child_other_page_table_urls
        print child_other_page_table_encrypt_urls
        print '^^^'
    print news_list
    logger.info(len(news_list))
    return news_list


def jbxx(url):  # 简报信息
    news_list = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    contain_parent_node_value_url = d('iframe').eq(1).attr('src')
    parent_node_value = re.findall(r'currfolderid=\d+', contain_parent_node_value_url)[0].replace('currfolderid=',
                                                                                                  '')  # 数字
    page_url_value = re.findall(r'pageUrl=\w+', contain_parent_node_value_url)[0].replace('pageUrl=',
                                                                                          '')  # 英文字母，如aegkjanjmdfhbbockgocljklfigblnmd
    print contain_parent_node_value_url
    print parent_node_value
    print page_url_value
    parent_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (
    page_url_value, parent_node_value, '简报信息')  # 构建父节点url
    contain_child_node_value_url = 'http://10.37.0.5/ecdomain/ecplatform/load_folder_nodes.do?type=folder&parentNodeId=root&parentNodeValue=%s&level=0&demin=null&_=' % parent_node_value
    contain_child_node_value_xml = requests.get(contain_child_node_value_url).content
    time.sleep(uniform(2, 6))
    xml_d = Pq(contain_child_node_value_xml).make_links_absolute(base_url=contain_child_node_value_url)
    child_node_value = xml_d('node').attr('value')  # 数字
    child_node_name = xml_d('node').attr('name')  # 文字，如内部信息
    child_url = 'http://10.37.0.5/ecdomain/framework/sdjcy/%s.jsp?currfolderid=%s&currfolderName=%s&displayPageLinkFlag=true&showChildFlag=false&pagination=true' % (
    page_url_value, child_node_value, child_node_name)  # 构建子节点url
    print child_url

    # 开始抓取父节点，子节点的所有列表url
    parent_r = requests.get(parent_url)
    time.sleep(uniform(2, 6))
    parent_r.encoding = 'utf-8'
    parent_d = Pq(parent_r.content).make_links_absolute(base_url=url)
    parent_first_page_table_urls = [i.attr('href') for i in parent_d('#listTable td a').items() if
                                    i.attr('href') != 'javascript:void(0)']
    parent_first_page_table_encrypt_urls = [
        'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        parent_d('#listTable td a').items() if i.attr('onclick') is not None]  # 加密url
    news_list.extend(parent_first_page_table_urls)
    news_list.extend(parent_first_page_table_encrypt_urls)
    print '###'
    print parent_first_page_table_urls
    print parent_first_page_table_encrypt_urls
    print len(parent_first_page_table_encrypt_urls)
    print '###'
    contain_parent_page_num_url = parent_d('#newslistComponentmliplfkomdembbockgocljklfigblnmd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    print '@@@'
    print contain_parent_page_num_url
    print '@@@'
    parent_total_page_num = int(re.findall(r'pageNum=\d+', contain_parent_page_num_url)[0].replace('pageNum=', ''))
    logger.info('parent total page: %s' % parent_total_page_num)
    for idx in xrange(2, parent_total_page_num + 1):
        logger.info('parent idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'mliplfkomdembbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/okngakjofapnbbocjakkkacknofbajdj/mliplfkomdembbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': parent_node_value,
                     'pagination': 'true',
                     'currfolderName': '简报信息',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        parent_post_r = requests.post(parent_url, data=form_data)
        parent_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        parent_post_d = Pq(parent_post_r.content).make_links_absolute(base_url=url)
        parent_other_page_table_urls = [i.attr('href') for i in parent_post_d('#listTable td a').items() if
                                        i.attr('href') != 'javascript:void(0)']
        parent_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            parent_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(parent_other_page_table_urls)
        news_list.extend(parent_other_page_table_encrypt_urls)
        print '$$$'
        print parent_other_page_table_urls
        print parent_other_page_table_encrypt_urls
        print '$$$'
    print news_list
    logger.info(len(news_list))

    # 开始抓取子节点，子节点的所有列表url
    child_r = requests.get(child_url)
    time.sleep(uniform(2, 6))
    child_r.encoding = 'utf-8'
    child_d = Pq(child_r.content).make_links_absolute(base_url=url)
    child_first_page_table_urls = [i.attr('href') for i in child_d('#listTable td a').items() if
                                   i.attr('href') != 'javascript:void(0)']
    child_first_page_table_encrypt_urls = [
        'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
        child_d('#listTable td a').items() if i.attr('onclick') is not None]
    print '%%%'
    print child_first_page_table_urls
    print child_first_page_table_encrypt_urls
    print '%%%'
    news_list.extend(child_first_page_table_urls)
    news_list.extend(child_first_page_table_encrypt_urls)
    contain_child_page_num_url = child_d('#newslistComponentmliplfkomdembbockgocljklfigblnmd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    child_total_page_num = int(re.findall(r'pageNum=\d+', contain_child_page_num_url)[0].replace('pageNum=', ''))
    logger.info('child total page num: %s' % child_total_page_num)
    for idx in xrange(2, child_total_page_num + 1):
        logger.info('child idx: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': page_url_value,
                     'moduleID': 'mliplfkomdembbockgocljklfigblnmd',
                     'moreURI': '/ecdomain/framework/sdjcy/okngakjofapnbbocjakkkacknofbajdj/mliplfkomdembbockgocljklfigblnmd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'currfolderid': child_node_value,
                     'pagination': 'true',
                     'currfolderName': child_node_name,
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        child_post_r = requests.post(child_url, data=form_data)
        child_post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        child_post_d = Pq(child_post_r.content).make_links_absolute(base_url=url)
        child_other_page_table_urls = [i.attr('href') for i in child_post_d('#listTable td a').items() if
                                       i.attr('href') != 'javascript:void(0)']
        child_other_page_table_encrypt_urls = [
            'http://10.37.0.5' + i.attr('onclick').replace('checkUser("', '').replace('")', '') for i in
            child_post_d('#listTable td a').items() if i.attr('onclick') is not None]
        news_list.extend(child_other_page_table_urls)
        news_list.extend(child_other_page_table_encrypt_urls)
        print '^^^'
        print child_other_page_table_urls
        print child_other_page_table_encrypt_urls
        print '^^^'
    print news_list
    logger.info(len(news_list))
    return news_list


def video(url):
    video_result = []
    r = requests.get(url)
    time.sleep(uniform(2, 6))
    r.encoding = 'utf-8'
    d = Pq(r.content).make_links_absolute(base_url=url)
    first_page_result = [{'id': int(re.findall(r'fileid=\d+', i('a[style]').attr('href'))[0].replace('fileid=', '')), 'video_url': i('a[style]').attr('href'), 'title': i('a[style]').attr('title').split('\n')[0].replace(u'标      题：', ''), 'author': i('a[style]').attr('title').split('\n')[1].replace(u'作      者：', ''), 'pubtime': i('a[style]').attr('title').split('\n')[2].replace(u'更新时间：', ''), 'img_url': i('img').attr('src')} for i in d('#playonsitelistcomponentmajgccmmniapbbocjkkmngjidmopimbd tr a:nth-child(odd)').items() if i('img').attr('src') and i('a[style]').attr('title') is not None]
    video_result.extend(first_page_result)
    contain_page_num_url = d('#playonsitelistcomponentmajgccmmniapbbocjkkmngjidmopimbd tr').eq(-1).find('a').eq(
        -1).attr(
        'href')
    total_page_num = int(re.findall(r'pageNum=\d+', contain_page_num_url)[0].replace('pageNum=', ''))
    logger.info('video page num: %s' % total_page_num)
    for idx in xrange(2, total_page_num+1):
        logger.info('video index: %s' % idx)
        form_data = {'goPage': 1, 'pageNum': idx, 'siteID': 'sdjcy', 'pageID': 'okbkmcblniaobbockofkmjklogeaijia',
                     'moduleID': 'majgccmmniapbbocjkkmngjidmopimbd',
                     'moreURI': '/ecdomain/framework/sdjcy/okbkmcblniaobbockofkmjklogeaijia/majgccmmniapbbocjkkmngjidmopimbd.do',
                     'var_temp': 'npgfhnlelcabbbofkfadpnoknggemmic',
                     'showChildFlag': 'false',
                     'displayPageLinkFlag': 'true'}
        post_r = requests.post(url, data=form_data)
        post_r.encoding = 'utf-8'
        time.sleep(uniform(2, 6))
        post_d = Pq(post_r.content).make_links_absolute(base_url=url)
        other_page_result = [{'id': int(re.findall(r'fileid=\d+', i('a[style]').attr('href'))[0].replace('fileid=', '')), 'video_url': i('a[style]').attr('href'), 'title': i('a[style]').attr('title').split('\n')[0].replace(u'标      题：', ''), 'author': i('a[style]').attr('title').split('\n')[1].replace(u'作      者：', ''), 'pubtime': i('a[style]').attr('title').split('\n')[2].replace(u'更新时间：', ''), 'img_url': i('img').attr('src')} for i in post_d('#playonsitelistcomponentmajgccmmniapbbocjkkmngjidmopimbd tr a:nth-child(odd)').items() if i('img').attr('src') and i('a[style]').attr('title') is not None]
        print other_page_result
        print len(other_page_result)
        video_result.extend(other_page_result)
    return video_result


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
                        belong='山东省人民检察院')
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
                        belong='山东省人民检察院')
    except IntegrityError as err:
        if 'duplicate key value' in str(err):
            logger.info(err)


if __name__ == '__main__':
    try:
        tztg_news_list = remove_duplicate_urls(tztg('http://10.37.0.5/ecdomain/framework/sdjcy/lcpckilgmdffbbockgocljklfigblnmd.jsp'))
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
        ljyw_news_list = remove_duplicate_urls(ljyw('http://10.37.0.5/ecdomain/framework/sdjcy/ncpbbphhfelebbocifbbmbfldfhbdbpn.jsp'))
        for ljyw_news in ljyw_news_list:
            try:
                ljyw_res = parse_news(ljyw_news)
                logger.info(ljyw_res['url'])
                save_return_value = save(ljyw_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        ldjh_news_list = remove_duplicate_urls(ldjh('http://10.37.0.5/ecdomain/framework/sdjcy/allhclnfepdjbboclifklppkbkkligai.jsp'))
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
        sywj_news_list = remove_duplicate_urls(sywj('http://10.37.0.5/ecdomain/framework/sdjcy/amkiecjgepdjbboclifklppkbkkligai.jsp'))
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
        jcdt_news_list = remove_duplicate_urls(jcdt('http://10.37.0.5/ecdomain/framework/sdjcy/ndnhnfpifelebbocifbbmbfldfhbdbpn.jsp'))
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
        jbxx_news_list = remove_duplicate_urls(jbxx('http://10.37.0.5/ecdomain/framework/sdjcy/aneollmhepdjbboclifklppkbkkligai.jsp'))
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
        tszs_news_list = remove_duplicate_urls(tszs('http://10.37.0.5/ecdomain/framework/sdjcy/nfmiflfkfelebbocifbbmbfldfhbdbpn.jsp'))
        for tszs_news in tszs_news_list:
            try:
                tszs_res = parse_news(tszs_news)
                logger.info(tszs_res['url'])
                save_return_value = save(tszs_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        myds_news_list = remove_duplicate_urls(myds('http://10.37.0.5/ecdomain/framework/sdjcy/anoamcjiepdjbboclifklppkbkkligai.jsp'))
        for myds_news in myds_news_list:
            try:
                myds_res = parse_news(myds_news)
                logger.info(myds_res['url'])
                save_return_value = save(myds_res)
                if save_return_value:
                    break
                logger.info('saving')
            except Exception as err:
                logger.info(err)
    except Exception as err:
        logger.info(err)

    try:
        zhxw_news_list = remove_duplicate_urls(zhxw('http://10.37.0.5/ecdomain/framework/sdjcy/ngkbfgdlfelebbocifbbmbfldfhbdbpn.jsp'))
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

    try:
        video_list = video('http://10.37.0.5/ecdomain/framework/sdjcy/okbkmcblniaobbockofkmjklogeaijia.jsp')
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

    requests.post('http://192.168.1.190:18080/COQuery/pachong', data={'belong': 'sdjcy'})
