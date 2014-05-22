#coding=utf8
from redis import  Redis
import random
from flask import Flask, jsonify, request

from ClientConfigMan.utils.mailsend_rest import MailSendRequest, make_msgid

rd = Redis()
app =  Flask(__name__)

total_capcha = 1000000
captcha = random.sample(xrange(total_capcha), total_capcha)
lindex = 0

@app.route('/mobile/captcha/')
def mobile_captcha():
    """
    每次请求进来就选出1000个随机数返回
    """
    global lindex

    if lindex + 1000 >= total_capcha:
        lt = []
    else:
        lt = captcha[lindex: lindex + 1000]
        lindex += 1000
    if lindex % 100000 ==0:
        print lindex,'pass'
    return jsonify(captcha=lt)


@app.route('/success/')
def success():
    success_capcha = request.values.get('success_capcha')
    print success_capcha
    Sender = MailSendRequest()
    Sender.sender = 'dev'
    Sender.subject = '验证码'
    Sender.content = 'captcha : %s ' % success_capcha
    Sender.message_id = make_msgid()
    Sender.to = ["zhangxiaorun@qvod.com"]
    Sender.fetch()
    return jsonify(ok=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8001)
