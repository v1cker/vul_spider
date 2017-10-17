# -*- coding: gb18030 -*-
import codecs
import sys
import re
import requests
from bs4 import BeautifulSoup

# reload(sys)
# sys.setdefaultencoding('utf-8')
url = 'https://loudong.sjtu.edu.cn/show/CNVD-2017-03364'
resp = requests.get(url, verify=False)
content = resp.text
temps = BeautifulSoup(content, 'lxml').find_all('td')
for temp in temps:
    if temp.text.encode('GB18030') == 'CNVD-ID':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '录入时间':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '报送时间':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '产生原因':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '归档时间':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '引发威胁':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '公开时间':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '攻击位置':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '发现时间':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '影响对象类型':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '是否热点漏洞':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '涉及厂商':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == 'CVE ID':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == 'BID ID':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '漏洞描述':
        print re.sub("\s", "", temp.next_sibling.next_sibling.text)
    if temp.text.encode('GB18030') == '参考链接':
        print temp.next_sibling.next_sibling.a.get('href')
    if temp.text.encode('GB18030') == '解决方案':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '厂商补丁':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '补丁描述':
        print re.sub("\s", '', temp.next_sibling.next_sibling.text)
    if temp.text.encode('GB18030') == '补丁链接':
        print temp.next_sibling.next_sibling.a.get('href')
    if temp.text.encode('GB18030') == '验证信息':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '补丁编号':
        print temp.next_sibling.next_sibling.text
            # a.append(temp.text)
    # if temp.text == '':
    #     print temp.next_sibling.next_sibling.text
    # print temp.encode('gbk')
# for i in a:
#     print type(i)
#     print i
# print content