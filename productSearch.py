import webbrowser

def productSearch(vendor, query):
	amazon_search = "https://www.amazon.in/s/keywords={}"
	flipkart_search = "https://www.flipkart.com/search?q={}"
	if( vendor in "amazon"):
		amazon_search = amazon_search.format(' '.join(query.split()[1:]))
		webbrowser.open(amazon_search)
		
	if( vendor in "flipkart"):
		flipkart_search = flipkart_search.format(' '.join(query.split()[1:]))
		webbrowser.open(flipkart_search)
