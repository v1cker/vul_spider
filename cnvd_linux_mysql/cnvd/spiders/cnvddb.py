# -*- coding: utf-8 -*-
import scrapy
import sys
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
from cnvd.items import CnvdItem

# reload(sys)
# sys.setdefaultencoding('utf-8')

class CnvddbSpider(scrapy.Spider):
    name = "cnvddb"
    allowed_domains = ["sjtu.edu.cn"]
    start_urls = ['https://loudong.sjtu.edu.cn/?page=%s' % str(i) for i in range(5, 6)]
        # 'http://www.cnvd.org.cn/flaw/list.htm?field=&startDate=&flag=%5BLjava.lang.String%3B%40b611c5b&max=20&order=&number=%E8%AF%B7%E8%BE%93%E5%85%A5%E7%B2%BE%E7%A1%AE%E7%BC%96%E5%8F%B7&endDate=&offset='+ str(i) for i in range(1, 3)
    hds = {'Content-Type': 'text/html; charset=UTF-8'}

    def parse(self, response):
        print "=" * 50
        print "[*]  " + response.url
        print "=" * 50
        body = BeautifulSoup(response.body, 'lxml')
        vuls = body.find_all('tr')
        # print vuls
        for vul in vuls:
            if vul.get('class') == ['warning'] or vul.get('class') == ['danger'] or vul.get('class') == ['success']:
                url = vul.a.get('href')
                title = vul.a.string
                level = vul.b.string
                yield Request(
                    url=url, headers=self.hds, callback=self.parse_item,
                    meta={'url': url, 'title': title, 'level': level}
                )
                break


    def parse_item(self, response):
        item = CnvdItem()
        item['title'] = response.meta['title'].encode('utf-8')
        item['url'] = response.meta['url']
        item['level'] = response.meta['level']
        body = response.body
        soup = BeautifulSoup(body, 'lxml')
        temps = soup.find_all('td')
        item['CNVD_ID'] = None
        item['entdate'] = None
        item['subdate'] = None
        item['archdate'] = None
        item['pubdate'] = None
        item['discdate'] = None
        item['cause'] = None
        item['effect_production'] = None
        item['harm'] = None
        item['attway'] = None
        item['vultype'] = None
        item['hot'] = None
        item['company'] = None
        item['bugtraq_id'] = None
        item['bugtraq_url'] = None
        item['cve_id'] = None
        item['cve_url'] = None
        item['vul_detial'] = None
        item['look_link'] = None
        item['patch'] = None
        item['patchdetial'] = None
        item['patchlink'] = None
        item['solution'] = None
        item['solution_url'] = None
        for temp in temps:
            print '=-=' * 10
            print temp.text
            print temp.text.encode('utf-8')
            print type(temp.text)
            print '=-=' * 10
            if temp.text.encode('utf-8') == 'CNVD-ID':
                item['CNVD_ID'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '录入时间':
                item['entdate'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '报送时间':
                item['subdate'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '产生原因':
                item['cause'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '归档时间':
                item['archdate'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '引发威胁':
                item['harm'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '公开时间':
                item['pubdate'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '攻击位置':
                item['attway'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '发现时间':
                item['discdate'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '影响对象类型':
                item['vultype'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '是否热点漏洞':
                item['hot'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '涉及厂商':
                item['company'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '影响产品':
                item['effect_production'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == 'CVE ID':
                item['cve_id'] = temp.next_sibling.next_sibling.text.encode('utf-8')
                item['cve_url'] = temp.next_sibling.next_sibling.a.get('href')
            if temp.text.encode('utf-8') == 'BID ID':
                item['bugtraq_id'] = temp.next_sibling.next_sibling.text.encode('utf-8')
                item['bugtraq_url'] = temp.next_sibling.next_sibling.a.get('href')
            if temp.text.encode('utf-8') == '漏洞描述':
                item['vul_detial'] = re.sub("\s", "", temp.next_sibling.next_sibling.text).encode('utf-8')
            if temp.text.encode('utf-8') == '参考链接':
                if temp.next_sibling.next_sibling.a:
                    item['look_link'] = temp.next_sibling.next_sibling.a.get('href')
            if temp.text.encode('utf-8') == '解决方案':
                item['solution'] = temp.next_sibling.next_sibling.text.encode('utf-8')
                item['solution_url'] = temp.next_sibling.next_sibling.text.encode('utf-8')
            if temp.text.encode('utf-8') == '厂商补丁' and temp.text.encode('utf-8') == '(暂无补丁信息)':
                item['patch'] = temp.next_sibling.next_sibling.text
            else:
                if temp.text.encode('utf-8') == '厂商补丁':
                    item['patch'] = temp.next_sibling.next_sibling.text.encode('utf-8')
                if temp.text.encode('utf-8') == '补丁描述':
                    item['patchdetial'] = temp.next_sibling.next_sibling.text.encode('utf-8')
                if temp.text.encode('utf-8') == '补丁链接':
                    if temp.next_sibling.next_sibling.a:
                        item['patchlink'] = temp.next_sibling.next_sibling.a.get('href')
        # print '-------item------' + item['CNVD_ID']
        # print '---------item level----' + item['level']
        yield item
