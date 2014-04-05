from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL="http://www.bloomberg.com/archive"

url="http://www.bloomberg.com/archive/news/2014-03-01/"

def get_links(url):
	data = urlopen(url).read()
	soup = BeautifulSoup(data, "lxml")
	html = soup.find("ul","stories")
	links = [BASE_URL + link.a["href"] for link in html.findAll("li")]
	
	total_links= len(links)
	print total_links
	for index in range(0,total_links):
		print index, links[index]

get_links(url)