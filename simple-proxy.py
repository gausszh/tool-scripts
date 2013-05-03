# -*- coding: utf-8 -*-
#
# author: gausszh
# 一个简单的代理转发。
from bottle import route, run,BaseRequest,request
import urllib,time

cach={}
@route('/<path:path>')
def hello(path):
    yy=path
    path=path[10:]
    url="http://192.168.33.141:8000/Schedule/Schedule/"+path
    if path.startswith('resources'):
        print 'resources'
        return ''
    if cach.has_key(path):
        print 'cache'
        return cach[path]
    if path.startswith('plugin.js'):
        cach[path]= open('./data/plugin.js').read()
        print 'plugin.js'
        return cach[path]
    elif path.startswith('scripts'):
        cach[path]= open('./data/'+path[8:]).read()
        print 'scripts'
        return cach[path]
    
    dic=request.query
    d=dic.items()
    params=''
    for one in d:
        params+="%s=%s&" % (one[0],one[1])
    print url+'?'+params
    print yy+'ddddddddd'
    return 'dd'
    if yy.find('favicon'):
        print 'favicon'
        return ''
    print 'aaaaaaaaaaaaaa'
    return urllib.urlopen(url+'?'+params).read()

run(host='0.0.0.0', port=8020, debug=True)
