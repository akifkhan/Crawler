#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""

from bs4 import BeautifulSoup
from urllib2 import urlopen

url="http://www.bloomberg.com/archive/news/2014-02-01/philippine-storm-batters-areas-still-reeling-from-haiyan-quake.html"

def get_links(url):
	
	BASE_URL="http://www.bloomberg.com"

	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	data = soup.find("ul","stories")
	links = [BASE_URL + link.a["href"] for link in data.findAll("li")]
	return links


def get_articles(url):

	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")

#EXTRACTING DATA FROM HTML TAGS

	heading = soup.find( "h1", "article_title buffer").string 		# Heading of the Article
	author = soup.find( "span", "author").string 					# Author/Writer of the Article
	timestamp = soup.find( "span","date").string 					# Time stamp of article
	content = soup.find('div',{'itemprop':'articleBody'}).text 		# The Content of the Article
	

#EXTRACTING THE DATA FROM META TAGS
#SOME DATA HAVE BEEN EXTRACTED TWICE FROM META TAGS


	category = soup.findAll(attrs={"name":"category"}) 		#category of Article on the basis of which it has been sorted on the website
	category = category[0]['content']

	
	description = soup.findAll(attrs={"name":"description"}) # Brief Description of the Article
	description = description[0]['content']

	
	pubdate = soup.findAll(attrs={"name":"pubdate"}) 		# Publishing Time and Date of the Article
	pubdate = pubdate[0]['content']
	

	print category, description, pubdate


#get_articles(url)

__name__ == "__main__"