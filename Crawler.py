#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""
import links
from datetime import date, timedelta

url="http://www.bloomberg.com/archive/news/"

while(1):
	d=date.today()-timedelta(days=1)
	d=d.strftime('%Y-%m-%d')
	url=url+d+"/"
	print url

	list_links = links.get_links(url)
	total_links = len(list_links)
	print total_links
	for index in range(0,total_links):
		print list_links[index]
		links.get_articles(list_links[index])