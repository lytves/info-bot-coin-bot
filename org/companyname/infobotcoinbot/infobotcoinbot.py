import telebot
import os
import requests
import time, threading
from flask import Flask, request

# set up config variables en your heroku environment
# your bot TOKEN
token = os.environ.get('TOKEN')
# your heroku app URL and add path "bot" for active update
appURL = os.environ.get('APPURL') + '/bot'
# your chatID of your channel
chatID = os.environ.get('CHATID')
# end of read config variables

bot = telebot.TeleBot(token)

server = Flask(__name__)

def requestAPI():
    url = "https://api.coinmarketcap.com/v1/ticker/bitcoin"
    response = requests.get(url)
    name = response.json()[0]['name']
    price = response.json()[0]['price_usd']
    rate24h = response.json()[0]['percent_change_24h']
    rate7d = response.json()[0]['percent_change_7d']
    text = "Current " + name + " price - ${}".format(price) \
           + "\nLast 24 hours changed for: " + rate24h + "%" \
           + "\nLast 7 days changed for: " + rate7d + "%"
    # bot.send_message(chatID, text)
    # time period each 3600 seconds = 1 hour
    # threading.Timer(3600, requestAPI).start()

requestAPI()
bot.send_message("@CryptoCoinsInfoBot", "text")

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=appURL)
    return "!", 200


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)