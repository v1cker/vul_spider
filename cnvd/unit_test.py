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
    if temp.text.encode('GB18030') == '¼��ʱ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '����ʱ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '����ԭ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '�鵵ʱ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '������в':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '����ʱ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '����λ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '����ʱ��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == 'Ӱ���������':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '�Ƿ��ȵ�©��':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '�漰����':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == 'CVE ID':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == 'BID ID':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '©������':
        print re.sub("\s", "", temp.next_sibling.next_sibling.text)
    if temp.text.encode('GB18030') == '�ο�����':
        print temp.next_sibling.next_sibling.a.get('href')
    if temp.text.encode('GB18030') == '�������':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '���̲���':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '��������':
        print re.sub("\s", '', temp.next_sibling.next_sibling.text)
    if temp.text.encode('GB18030') == '��������':
        print temp.next_sibling.next_sibling.a.get('href')
    if temp.text.encode('GB18030') == '��֤��Ϣ':
        print temp.next_sibling.next_sibling.text
    if temp.text.encode('GB18030') == '�������':
        print temp.next_sibling.next_sibling.text
            # a.append(temp.text)
    # if temp.text == '':
    #     print temp.next_sibling.next_sibling.text
    # print temp.encode('gbk')
# for i in a:
#     print type(i)
#     print i
# print content