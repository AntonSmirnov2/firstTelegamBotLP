import telebot
import apiai
import json

token = '487042194:AAE2LdNjwuKQ3DgSiSWQPCyUsq-HLWZ_0dU'

AItoken = '830407320d444bb48a79bc10443cd7c6'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def welcome_func(message):
    bot.send_message(message.chat.id, 'Привет, я бот Антона С. Я уже умею отвечать на несложные '
                                      'сообщения. Можете написать мне что-нибудь')


@bot.message_handler(content_types=["text"])
def AI_reply(message):
    request = apiai.ApiAI(AItoken).text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял')
    # responce = 'Получил ваше сообщение:\n' + message.text
    # bot.send_message(message.chat.id, responce)


if __name__ == '__main__':
    bot.polling()
