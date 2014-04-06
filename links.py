#!/usr/bin/env python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.

"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
from json import JSONEncoder
import sys


def get_links(url): 							# It fetches the links of all articles on a specific date
	
	BASE_URL="http://www.bloomberg.com"
	
	try:

		html = urlopen(url).read()					#opens the URL and fetch the HTML
		soup = BeautifulSoup(html, "lxml")			#opens HTML to be parsed 
		data = soup.find("ul","stories")			#finds the tag from HTML with div class = stories
		
		#All the a href links are extracted and stored in a list
		
		links = [BASE_URL + link.a["href"] for link in data.findAll("li")]	
		
		return links

	except:
		print "Error fetching the news links from the website: "
		sys.exit(1)	


def get_articles(url):

	try:
		html = urlopen(url).read()					#opens the url and fetch HTML
		soup = BeautifulSoup(html, "lxml")			#opens HTML to be parsed
	except:
		print "Error fetching the news articles from the website"
		sys.exit(1)


#EXTRACTING DATA FROM HTML TAGS

	heading = soup.find( "h1", "article_title buffer").string 		# Heading of the Article
	author = soup.find( "span", "author").string 					# Author/Writer of the Article
	timestamp = soup.find( "span","date").string 					# Time stamp of article
	content = soup.find('div',{'itemprop':'articleBody'}).text 		# The Content of the Article
	

#EXTRACTING THE DATA FROM META TAGS
#SOME DATA HAVE BEEN EXTRACTED TWICE FROM META TAGS AND FROM THE HTML TAGS (JUST FOR THE SAKE OF DEMONSTRATION)


	category = soup.findAll(attrs={"name":"category"}) 		#category of Article on the basis of which it has been sorted on the website
	category = category[0]['content']

	
	description = soup.findAll(attrs={"name":"description"}) # Brief Description of the Article
	description = description[0]['content']

	
	pubdate = soup.findAll(attrs={"name":"pubdate"}) 		# Publishing Time and Date of the Article
	pubdate = pubdate[0]['content']
	


	jsonString = JSONEncoder().encode( 
			{
			"heading": heading,
			"category": category,
			"author": author,
			"description": description,
			"pubdate": pubdate,
			"content": content
			} )
	return jsonString
	

__name__ == "__main__"