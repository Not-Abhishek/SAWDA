import requests
from bs4 import BeautifulSoup
import webbrowser
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
def playYoutubeVideo(query):
	query_split = query.split()[1:]
	url = 'https://www.youtube.com/results?search_query={}'.format('+'.join(query_split))
	source_code = requests.get(url, timeout=15)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")
	videoes = soup.findAll('div', {'class': 'yt-lockup-video'})
	video = videoes[0].contents[0].contents[0].contents[0]
	hit = video['href']
	speak.Speak("playing " + ' '.join(query_split))
	webbrowser.open('https://www.youtube.com' + hit)