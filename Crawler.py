#!/usr/bin/python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""
import links
from datetime import date, timedelta
from json import JSONDecoder


Days=0

while(Days < 2920):								# 365*8 = 2920 as the website got news only till 2006

	url="http://www.bloomberg.com/archive/news/"										
	d=date.today()-timedelta(days=Days)
	d=d.strftime('%Y-%m-%d')
	url=url+d+"/"
	print url
	list_links = links.get_links(url)			# It gets Articles published on any single day
	
	total_links = len(list_links)				# Total Articles published on a single day
	print total_links

	
	#Fetches the Article Details by parsing each article page and then return the Data in JSON Format to be stored in DB 
	
	for index in range(0,total_links):	
		print list_links[index]
		data = links.get_articles(list_links[index])
		print data
		data = JSONDecoder().decode(data)
		print data
	Days = Days+1