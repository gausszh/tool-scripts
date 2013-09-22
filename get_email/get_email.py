#coding=utf8
from pyquery import PyQuery as pq
import pdb

#陶瓷
r = 'http://fair.mingluji.com'
root = 'http://fair.mingluji.com/Ceramics/%s'
f=open('/home/gausszh/project/ceramics.csv','w')
d=pq(url=root)
tb=d('#bodyContent table td')
td=tb.eq(0)
ahref = td('ol li a')
lt = []
for a in ahref:
    url = r + a.attrib.get('href')
    lt.append(url)
count = 0
for a in lt:
    count += 1
    if count > 3:
        break
    d = pq(url=a)
    tb = d('#bodyContent table')
    tb  = tb.eq(0)
    tr = tb.children('tr')
    m = tr.eq(3)
    span = m('span')
    y = []
    for b in span:
        y.append(b.text)
    f.write('%s\n' % '\t'.join(y))
f.close()
