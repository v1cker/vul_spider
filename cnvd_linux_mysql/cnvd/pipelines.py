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
        try:
            print '=' * 50
            print 'start'
            print '=' * 50
            self.cursor.execute("""insert into cnvdvul_copy (title,CNVD_ID,entdate,subdate,archdate,pubdate,discdate,cause,level,effect_production,harm,attway,vultype,hot,company,bugtraq_id,bugtraq_url,cve_id,cve_url,vul_detial,look_link,patch,patchdetial,patchlink,solution,solution_url,url)
              values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                item['title'],
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




# class CnvdPipeline(object):
#     def __init__(self, dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls, settings):
#         dbargs = dict(
#             host=settings['MYSQL_HOST'],
#             db=settings['MYSQL_DBNAME'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             charset='utf8',
#             cursorclass=MySQLdb.cursors.DictCursor,
#             use_unicode=True,
#         )
#         dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
#         d.addErrback(self._handle_error, item, spider)
#         d.addBoth(lambda _: item)
#         # print d
#         return d
        # url = item['url']
        # ret = Sql.select_title(url)
        # if ret[0] == 1:
        #     print '漏洞已存在'
        # else:
        #     Sql.insert_cnvdvul(item)
        #     print '开始存储漏洞'



    # def _do_upinsert(self, conn, item, spider):
    #     conn.execute("""
    #       select 1 from cnvdvul where url = %s
    #      """, (item['url'],))
    #     ret = conn.fetchone()
    #     print '^' * 50
    #     print '^' * 50
    #     if ret:
    #         print '已存在'
    #     else:
    #         conn.execute("""
    #           insert into cnvdvul_copy (title,CNVD_ID,entdate,subdate,archdate,pubdate,discdate,cause,level,effect_production,harm,attway,vultype,hot,company,bugtraq_id,bugtraq_url,cve_id,cve_url,vul_detial,look_link,patch,patchdetial,patchlink,solution,solution_url,url)
    #           values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #         """, (
    #             str(item['title']),
    #             str(item['CNVD_ID']),
    #             str(item['entdate']),
    #             str(item['subdate']),
    #             str(item['archdate']),
    #             str(item['pubdate']),
    #             str(item['discdate']),
    #             str(item['cause']),
    #             str(item['level']),
    #             str(item['effect_production']),
    #             str(item['harm']),
    #             str(item['attway']),
    #             str(item['vultype']),
    #             str(item['hot']),
    #             str(item['company']),
    #             str(item['bugtraq_id']),
    #             str(item['bugtraq_url']),
    #             str(item['cve_id']),
    #             str(item['cve_url']),
    #             str(item['vul_detial']),
    #             str(item['look_link']),
    #             str(item['patch']),
    #             str(item['patchdetial']),
    #             str(item['patchlink']),
    #             str(item['solution']),
    #             str(item['solution_url']),
    #             str(item['url']),
    #         ))
    #
    #
    # def _handle_error(self, failue, item, spider):
    #     log.err(failure)

# class LianjiaPipeline(object):
#     def process_item(self, item, spider):
#         title = item['title']
#         ret = Sql.select_title(title)
#         if ret[0] ==1:
#
#             print('房子已经存在')
#         else:
#             rental = item['rental']
#             distance = item['distance']
#             area = item['area']
#             room_number = item['room_number']
#             floor = item['floor']
#             direction = item ['direction']
#             year_build = item['year_build']
#             Sql.insert_tenement_message(title,rental,distance,area,room_number,floor,direction,year_build)
#             print('开始存租房信息')