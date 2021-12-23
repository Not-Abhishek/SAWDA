import speech_recognition as sr
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

def getUserquery():
	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	# recognize speech using Google Speech Recognition
	try:
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		speak.Speak("Google Speech Recognition could not understand audio, Please type your query")
		# print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		speak.Speak("Google Speech Recognition could not understand audio, Please type your query")
		# print("Could not request results from Google Speech Recognition service; {0}".format(e))