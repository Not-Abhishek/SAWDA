sportnews_url = "http://feeds.feedburner.com/ndtvsports-latest"
topnews_url = "http://feeds.feedburner.com/ndtvnews-top-stories"
worldnews_url = "http://feeds.feedburner.com/ndtvnews-world-news"
latestnews_url = "http://feeds.feedburner.com/ndtvnews-latest"
gadgetsnews_url = "http://feeds.feedburner.com/gadgets360-latest"

import newsfeedparse as feeds
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

def newsFeeds(news_type):
	speak.Speak('Searching news for you from NDTV India')
	if(news_type in latestnews_url):
		print(feeds.getNews(latestnews_url))
	if(news_type in topnews_url):
		print(feeds.getNews(topnews_url))
	if(news_type in worldnews_url):
		print(feeds.getNews(worldnews_url))
	if(news_type in sportnews_url):
		print(feeds.getNews(sportnews_url))
	if(news_type in gadgetsnews_url):
		print(feeds.getNews(gadgetsnews_url))