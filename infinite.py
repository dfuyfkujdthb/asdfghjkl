import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = '1193133723:AAEYOyi1qAOPNBsQMknpc6CnIXr33G7t4Ts'
    bot_chatID = '772671984'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    my_balance = 10   ## Replace this number with an API call to fetch your account balance
    my_message = "https://www.acko.tech/amazon-mobile/download-policy/GuF71M6Cy5lhYT-Jek9law"   ## Customize your message
    telegram_bot_sendtext(my_message)


    
schedule.every().day.at("02:51").do(report)

while True:
    schedule.run_pending()
    time.sleep(1)
