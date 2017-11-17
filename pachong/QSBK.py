from urllib import request, error
import urllib
import re
import os
patten = '<div class="content">.<span>(.*?)</span>'
patten = re.compile(patten, re.S)


def getHTML(page=1):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = request.Request(url, headers=headers)
    res = request.urlopen(req)
    return res


try:
    f = open('joke.txt', 'a+')
    for page in range(1, 10, 1):
        res = getHTML(page)
        content = res.read().decode('utf-8')
        items = patten.findall(content)
        f.write('joke at page{}: \n'.format(page))
        index = 1
        for item in items:
            f.write('笑话%d:' % index + item.split()[0] + '\n')
            index += 1
        f.write('\n')
    f.close()
    print('finished write!')
except error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
