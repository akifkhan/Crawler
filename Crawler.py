#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""
import links

url="http://www.bloomberg.com/archive/news/2014-03-01/"

links = links.get_links(url)
total_links= len(links)
for index in range(0,total_links):
	get_articles(links(index))