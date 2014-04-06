from pymongo import MongoClient


def mongo_insert(data):
	client = MongoClient('localhost', 27017)
	if not (client):
		print "Database Connection error"
		exit

	db = client.bloomberg
	collection = db.articles

	id = db.articles.insert(data)
	print id
	print "Data inserted in DB"