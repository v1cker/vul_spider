# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnvdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()  # 标题
    CNVD_ID = scrapy.Field()  # cnvd id
    entdate = scrapy.Field()  # 录入时间
    subdate = scrapy.Field()  # 提交时间
    archdate = scrapy.Field()  # 归档时间
    pubdate = scrapy.Field()  # 公开时间
    discdate = scrapy.Field()  # 发现时间
    cause = scrapy.Field()  # 产生原因
    level = scrapy.Field()  # 漏洞等级
    effect_production = scrapy.Field()  # 影响产品
    harm = scrapy.Field()  # 引发威胁
    attway = scrapy.Field()  # 攻击位置
    vultype = scrapy.Field()  # 漏洞影响类型
    hot = scrapy.Field()  # 是否热点漏洞
    company = scrapy.Field()  # 设计厂商
    bugtraq_id = scrapy.Field()  # bid id
    bugtraq_url = scrapy.Field()  # bid url
    cve_id = scrapy.Field()   # cve id
    cve_url = scrapy.Field()  # cve url
    vul_detial = scrapy.Field()  # 漏洞描述
    look_link = scrapy.Field()  # 参考链接
    patch = scrapy.Field()  # 厂商补丁
    patchdetial = scrapy.Field()  # 补丁详情
    patchlink = scrapy.Field()  # 补丁链接
    solution = scrapy.Field()  # 解决方案
    solution_url = scrapy.Field()  # 临时解决方案


    url = scrapy.Field()
