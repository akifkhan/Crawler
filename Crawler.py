#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""
import links

url="http://www.bloomberg.com/archive/news/2014-02-01/"

link1 = links.get_links(url)
total_links= len(link1)
print total_links
for index in range(0,total_links):
	print link1[index]
	links.get_articles(link1[index])