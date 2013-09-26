#coding=utf8
from pyquery import PyQuery as pq
from redis import Redis
import pdb

#陶瓷
total_page = 15
rd = Redis()
URL_key = 'GET_EMAIL:URL'
r = 'http://fair.mingluji.com'
root = 'http://fair.mingluji.com/Ceramics/%s'
for i in range(total_page):
    index_url = root % i
    d = pq(url=index_url)
    print index_url
    tb = d('#bodyContent table td')
    td = tb.eq(0)
    ahref = td('ol li a')
    for a in ahref:
        url = r + a.attrib.get('href')
        rd.lpush(URL_key, url)
