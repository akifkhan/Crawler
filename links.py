#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""

from bs4 import BeautifulSoup
from urllib2 import urlopen


def get_links(url):
	
	BASE_URL="http://www.bloomberg.com/archive"

	data = urlopen(url).read()
	soup = BeautifulSoup(data, "lxml")
	html = soup.find("ul","stories")
	links = [BASE_URL + link.a["href"] for link in html.findAll("li")]
	return links


def get_articles(url):

	data = urlopen(url).read()
	soup = BeautifulSoup(data, "lxml")
	html = soup.find("h1","article_title buffer")


__name__ == "__main__"