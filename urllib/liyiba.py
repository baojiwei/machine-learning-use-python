# coding=utf-8
import re
import urllib2


def getHtml(url):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    html = res.read()
    res.close()

    return html


def translate(html):
    string = html.strip().decode('utf-8','ignore')

    p2 = re.compile(ur'[^\u4e00-\u9fa5]')

    zh = " ".join(p2.split(string)).strip()
    zh = ",".join(zh.split())

    zh = zh.strip().encode('utf-8')+'\n'
    zh = zh.split(',')
    return zh


def save2doc(zh,filename):
    f = open(filename,'w')
    string = '\t'.join([str(s) for s in zh])
    f.write(string)
    f.close()

