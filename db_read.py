# python2.7.5
# author : eric zhang
# email  : ericnomail@gmail.com
# twitter: @loveisbug
#    http://weibo.com/loveisbug
# date        version    PIC    comments
# 20110720    0.0.1      eric   

import urllib
from bs4 import BeautifulSoup
import codecs

def db_read_2014(member):
	fo = codecs.open('2014_readlist.txt', 'w', 'utf-8')
	prefix = 'http://book.douban.com/people/'
	start = '/collect?start='
	suffix = '&sort=time&rating=all&filter=all&mode=grid'
	pagecnt = 0
	nextpage = True
	while nextpage:
		url = prefix + member + start + str(pagecnt) + suffix
		html_src = urllib.urlopen(url).read()
		parser = BeautifulSoup(html_src)
		items = parser.findAll('li', 'subject-item')
		for item in items:
			if int(item.find('span', 'date').text.strip()[:4]) >= 2014:
				fo.write('<' + item.findNext('a').findNext('a')['title'].strip() + '>, ' + item.find('div', 'pub').text.strip().split('/')[0] + ', ' + item.find('span', 'date').text[:-2].strip() + '\n')
			else:
				nextpage = False
				break
		pagecnt += 15
	fo.close()

db_read_2014('blacktulip')