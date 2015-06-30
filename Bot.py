import pprint
import requests
import time

from token import *

class Bot:
	"""docstring for ClassName"""

	def __init__(self, name):
		self.name = name
		self.update_id = 0
		
	def answere(self, message={}):
		# pprint.pprint(message)
		payload = {'chat_id': '', 'text': ''}
		try:
			payload['chat_id'] = message['message']['chat']['id']
			payload['text'] = self.generateAnswere(message['message']['text'])
		except Exception, e:
			# raise e
			return False
		self.r = requests.post("https://api.telegram.org/bot"+token+"/sendMessage", params=payload)
		self.update_id = message['update_id']
		self.update_id += 1
		# print self.update_id
		return self.r.json()['ok']

	def generateAnswere(self, message):
		return "Ciao!"