import wolframalpha
import wikipedia
import requests
import warnings

warnings.filterwarnings('ignore')
appId = 'APER4E-58XJGHAVAK'
client = wolframalpha.Client(appId)

# method that search wikipedia... 
def search_wiki(keyword=''):
  # running the query
	searchResults = wikipedia.search(keyword)
	# If there is no result, print no result
	if not searchResults:
		return "No result from Wikipedia"
	# Search for page... try block 
	try:
		page = wikipedia.page(searchResults[0])
	except wikipedia.DisambiguationError as err:
		page = wikipedia.page(err.options[0])
  
	wikiTitle = str(page.title.encode('utf-8'))
	wikiSummary = str(page.summary)
	return "Result from wikipedia:\n"+wikiSummary
    

def search(text=''):
	res = client.query(text)
	# Wolfram cannot resolve the question
	if res['@success'] == 'false':
		return 'Question cannot be resolved'
	# Wolfram was able to resolve question
	else:
		result = ''
		# pod[0] is the question
		pod0 = res['pod'][0]
		# pod[1] may contains the answer
		pod1 = res['pod'][1]
		# checking if pod1 has primary=true or title=result|definition
		if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
		# extracting result from pod1
			result = resolveListOrDict(pod1['subpod'])
			return "Result from wolframalpha:\n"+result
		else:
			# extracting wolfram question interpretation from pod0
			question = resolveListOrDict(pod0['subpod'])
			# removing unnecessary parenthesis
			question = removeBrackets(question)
			# searching for response from wikipedia
			return search_wiki(question)


def removeBrackets(variable):
  return variable.split('(')[0]

def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']
	
#####
# Code credit goes to https://github.com/salisuwy/Python-AI-Assistant/blob/master/main.py
####