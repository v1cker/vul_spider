# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


dbuser = 'root'
dbpass = 'root'
dbname = 'vuldb'
dbhost = '192.168.33.1'
dbport = '3306'
class SQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        k = 0
        self.cursor.execute("""select 1 from cnvdvul_copy where url = %s""", (item['url'],))
        ret = self.cursor.fetchone()
        if ret:
            k = ret[0]
        print "+" * 50
        print k
        print "+" * 50
        if k == 1:
            print "已存在！"
        else:
            try:
                self.cursor.execute("""insert into cnvdvul_copy (title,CNVD_ID,entdate,subdate,archdate,pubdate,discdate,cause,level,effect_production,harm,attway,vultype,hot,company,bugtraq_id,bugtraq_url,cve_id,cve_url,vul_detial,look_link,patch,patchdetial,patchlink,solution,solution_url,url)
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    item['title'].encode('utf-8'),
                    item['CNVD_ID'],
                    item['entdate'],
                    item['subdate'],
                    item['archdate'],
                    item['pubdate'],
                    item['discdate'],
                    item['cause'],
                    item['level'],
                    item['effect_production'],
                    item['harm'],
                    item['attway'],
                    item['vultype'],
                    item['hot'],
                    item['company'],
                    item['bugtraq_id'],
                    item['bugtraq_url'],
                    item['cve_id'],
                    item['cve_url'],
                    item['vul_detial'],
                    item['look_link'],
                    item['patch'],
                    item['patchdetial'],
                    item['patchlink'],
                    item['solution'],
                    item['solution_url'],
                    item['url'],
                ))
                self.conn.commit()
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
            return item


