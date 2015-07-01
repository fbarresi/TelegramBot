import pprint
import requests
import time

from token import *

class Bot:
	"""docstring for ClassName"""

	def __init__(self, name):
		self.name = name
		self.update_id = 0
		
	def answer(self, message={}):
		# pprint.pprint(message)
		payload = {'chat_id': '', 'text': ''}
		try:
			payload['chat_id'] = message['message']['chat']['id']
			payload['text'] = self.generateAnswer(message['message']['text'])
		except Exception, e:
			# raise e
			return False
		self.r = requests.post("https://api.telegram.org/bot"+token+"/sendMessage", params=payload)
		self.update_id = message['update_id']
		self.update_id += 1
		return self.r.json()['ok']

	def generateAnswer(self, message):
		return {
        	'/status': "Current status: OK!",
        	'/about': "My Name is "+BotName+", I'm a test Bot",
        	'Hi!': "Hi!",
    	}.get(message, "Sorry, I don't understand this message...") 