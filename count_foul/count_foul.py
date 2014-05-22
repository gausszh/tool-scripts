# coding=utf8

from BeautifulSoup import BeautifulSoup
import Queue
import re
import sys
import threading
import urllib

url_queue = Queue.Queue()
rex = re.compile(u'(犯规|哨)')  # 需要统计的词
total_floors_count = 0  # 总楼数
foul_floors_count = 0  # 提到犯规、哨的楼数


def count_hot_line_page():
    """
    热线会有很多页，从队列中取出某一页面的url，用BeautifulSoup解析html。
    获取所有楼层的评论，从而计算有多少楼提到了“犯规”、“哨”
    """
    global total_floors_count, foul_floors_count
    while 1:
        if url_queue.empty():
            break
        page_url = url_queue.get()
        content = urllib.urlopen(page_url).read()
        page = BeautifulSoup(content.decode('gb2312', 'ignore'))
        # hupu的网页编码是gb2312的
        floors = page.findAll(attrs={'class': 'floor'})
        total_floors_count += len(floors)
        fouls = reduce(lambda count, floor: count + (rex.findall(floor.td.text)
                                                     and 1 or 0), floors, 0)
        foul_floors_count += fouls

if __name__ == '__main__':
    # 从命令行中输入热线首页的url, 以及需要统计的页数
    # 比如：http://bbs.hupu.com/9552100.html 172
    if len(sys.argv) != 3:
        print '从命令行中输入热线首页的url, 以及需要统计的页数'
        print '比如：http://bbs.hupu.com/9552100.html 172'
        sys.exit(1)
    hot_line_home_page = sys.argv[1]
    total_page = int(sys.argv[2])
    for i in range(total_page):
        url_queue.put(hot_line_home_page[:-5] + '-' + str(i) + '.html')
    thread_list = []
    thread_count = 5
    # 一般起5个线程就可以了
    for _ in range(thread_count):
        thread_list.append(threading.Thread(target=count_hot_line_page))
    for th in thread_list:
        th.start()
    for th in thread_list:
        th.join()
    print '**********  ok  **************'
    print '总计楼层数为: %s, 提到“犯规”、“哨”的楼层数为: %s' % \
        (total_floors_count, foul_floors_count)
