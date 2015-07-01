import pprint
import requests
	# install request before via pip:
		# pip install requests
		# pip install requests[security]
import time
from Bot import *
from token import *

repeat = True
delay = 0.5

bot = Bot(BotName)

while repeat:
	# repeat = False
	receive = {'offset': bot.update_id}
	r = requests.post("https://api.telegram.org/bot"+token+"/getUpdates", params=receive)
	if r.status_code==200:
		update = r.json()
		for elem in update['result']:
			if not bot.answer(elem):
				print "Error during answere"
		time.sleep(delay)
	else :
		print "Error ",r.status_code
		print r.history
		time.sleep(delay)