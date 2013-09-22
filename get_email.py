#coding=utf8
from pyquery import PyQuery as pq

#陶瓷
r = 'http://fair.mingluji.com'
root = 'http://fair.mingluji.com/Ceramics'
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
print len(lt)
for a in lt:
    count += 1
    if count > 10:
        break
    d = pq(url=a)
    print a
    tb = d('#bodyContent table')
    tb =td.eq(0)
    tr = tb('tr')
    m = tr.eq(6)
    span = m('span')
    y = []
    for b in span:
        y.append(b.text)
        print b.text
    print '\t'.join(y)
    f.write('%s\n' % '\t'.join(y))
f.close()
