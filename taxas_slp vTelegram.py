from requests_html import HTMLSession
import pandas as pd
from datetime import datetime
import time
import telebot
import locale
from secrets import chave_api

# locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
contador = 1


# Site para pegar as ultimas interaçoes do meu bot: "https://api.telegram.org/bot" + chave_api + "/getUpdates"

bot = telebot.TeleBot(chave_api)

while True:
    # Open axie.live website and wait it to render JavaScript
    session = HTMLSession()

    url = "https://axie.live/"

    r = session.get(url)

    r.html.render(sleep=10, keep_page=True)

    #html_code = r.html.html
    #print(html_code)

    # Get all table data and table headers in the HTML file
    td_tags = r.html.find("td")
    th_tags = r.html.find("th")

    #print(td_tags)

    #Pre process lists
    dados_td = [tag.text for tag in td_tags]
    dados_th = [tag.text for tag in th_tags]


    Fast_W_SLP = dados_td[32]
    Std_W_SLP = dados_td[33]
    print(Fast_W_SLP)
    print(type(Fast_W_SLP))

    if locale.atof(Fast_W_SLP.strip("$")) < 90:
        bot.send_message(-593838013, "Fast Withdraw SLP: " + Fast_W_SLP)
        time.sleep(1)

    if locale.atof(Std_W_SLP.strip("$")) < 90:
        bot.send_message(-593838013, "Standard Withdraw SLP: " + Std_W_SLP)
        time.sleep(1)

    time.sleep(50)




