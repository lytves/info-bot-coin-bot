import telebot
import os
import requests
import threading
from flask import Flask, request
from emoji import emojize

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


@bot.message_handler(content_types=["text"])
def handle_text(message):
    requestAPI(message)


def requestAPI(message):
    url = "https://api.coinmarketcap.com/v1/ticker/bitcoin"
    response = requests.get(url)
    name = response.json()[0]['name']
    price = response.json()[0]['price_usd']

    # 24 hours price change with emoji
    rate24h = response.json()[0]['percent_change_24h']
    if float(rate24h) > 20:
        rate24hemoji = emojize(":rocket:", use_aliases=True)
    elif float(rate24h) < 0:
        rate24hemoji = emojize(":small_red_triangle_down:", use_aliases=True)
    elif float(rate24h) > 0:
        rate24hemoji = emojize(":white_check_mark:", use_aliases=True)

    # 7 days price change with emoji
    rate7d = response.json()[0]['percent_change_7d']
    if float(rate7d) > 20:
        rate7demoji = emojize(":rocket:", use_aliases=True)
    elif float(rate7d) < 0:
        rate7demoji = emojize(":small_red_triangle_down:", use_aliases=True)
    elif float(rate7d) > 0:
        rate7demoji = emojize(":white_check_mark:", use_aliases=True)

    text = "Current *" + name + "* price - *${}".format(price) + "*" \
           + "\nLast 24 hours changed for: *" + rate24h + "%*" + rate24hemoji \
           + "\nLast 7 days changed for: *" + rate7d + "%*" + rate7demoji

    # bot.send_message(chatID, text, parse_mode="Markdown")
    # time period each 3600 seconds = 1 hour
    # threading.Timer(3600, requestAPI).start()

    bot.send_message(message.from_user.id, text, parse_mode="Markdown")


@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=appURL)
    return "!", 200


server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
server = Flask(__name__)