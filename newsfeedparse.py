import feedparser

def getFeeds(url):
	feed = feedparser.parse(url)
	feed_entries = feed.entries
	return feed_entries
	
def getNews(url):
	for entry in getFeeds(url):
		article_title = entry.title
		article_description = entry.description
		print("Title: {}".format(article_title))
		print("Description: {}\n".format(article_description))
		
