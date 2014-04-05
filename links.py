#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""

from bs4 import BeautifulSoup
from urllib2 import urlopen

url="http://www.bloomberg.com/news/2014-04-05/bank-of-england-rates-to-australian-unemployment-global-economy.html"

def get_links(url):
	
	BASE_URL="http://www.bloomberg.com/archive"

	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	data = soup.find("ul","stories")
	links = [BASE_URL + link.a["href"] for link in data.findAll("li")]
	return links


def get_articles(url):

	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	heading = soup.find( "h1", "article_title buffer").string
	author = soup.find( "span", "author").string
	timestamp = soup.find( "span","date").string
	content = soup.find('div',{'itemprop':'articleBody'}).text
	content1 = soup.find('meta',{'name':'title'})

	category = soup.findAll(attrs={"name":"category"}) 
	category = category[0]['content']

	print category

	

	#print heading, author, timestamp, content1


get_articles(url)



__name__ == "__main__"