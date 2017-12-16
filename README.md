# info-boit-coin-bot

[@CryptoInfoMe](https://t.me/CryptoInfoMe "@CryptoInfoMe") - enjoy it!

This is a simple version of a Telegram Bot, which sending a message to a channel with a price of a CryptoCoin (BitCoin)

Has been used:
* [pyTelegramBotAPI Library ](https://github.com/eternnoir/pyTelegramBotAPI "pyTelegramBotAPI Library GitHub Repository")

with using webhook updates method for recieve the messages.  

Add your bot to your telegram channel and make it an administrator for send the messages. 

For use unicode emojis has been used: 
* [Emoji Library](https://github.com/carpedm20/emoji "Emoji for Python.")
---

Has been deployed on Heroku servers. Put the Token of you bot and the URL of your heroku app to the Heroku environment settings:

+ For setting up variables:
```bash
$ heroku config:set TOKEN=put_your_token_here
$ heroku config:set APPURL=put_your_app_url_here
$ heroku config:set CHATID=put_chatId_of_your_channel_here
```

+ For show your configs vars:
```bash
$ heroku config
```

