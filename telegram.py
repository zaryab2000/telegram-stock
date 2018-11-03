#!/usr/bin/env python3

import telepot
import time
import requests
from bs4 import BeautifulSoup

token=''
bot=telepot.Bot(token)

def main(cmd):
    company=cmd['text'].upper()
    response=requests.get('https://www.screener.in/company/' +company+ '/')
    soup=BeautifulSoup(response.text, 'html.parser')
    amount=soup.find_all('li',{'class':'four columns'})
    price=amount[1].text
    bot.sendMessage(cmd['chat']['id'], price)

print('bot is listening')
bot.message_loop(main)

while True:
    time.sleep(10)
