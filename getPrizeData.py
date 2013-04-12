#coding=utf8
import urllib,json,xlwt
getUrl="http://*******/ipl/admin/winner_init?draw_time=%s&limit=200&start=0"
youTime=raw_input("input the time,like 2013-04-08\n")
urls=getUrl % youTime
print urls
ret=json.load(urllib.urlopen(urls))
rows=ret['rows']
excelFile=xlwt.Workbook(encoding='utf8')
sh=excelFile.add_sheet(youTime)
title=[u'Dn',u'中奖时间',u'email',u'name',u'奖品名称']
for t in range(len(title)):
    sh.write(0,t,title[t])
for r in range(len(rows)):
    c=0
    sh.write(r+1,c,rows[r]['Dn'])
    c+=1
    sh.write(r+1,c,rows[r]['DrawTime'])
    c+=1
    sh.write(r+1,c,rows[r]['Email'])
    c+=1
    sh.write(r+1,c,rows[r]['Name'])
    c+=1
    sh.write(r+1,c,rows[r]['PrizeName'])
    c+=1
excelFile.save("D:/%s.xls" % youTime)
print '********* OK  **********'
