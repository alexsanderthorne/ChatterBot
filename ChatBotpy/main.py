from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('TW Chat Bot')

bot.set_trainer(ListTrainer)

for _file in os.listdir('files'):
  chats = open('files/' + _file, 'r').readlines()

  bot.train(chats)
  
while True:
    pergunta = input("User: ")
    resposta = bot.get_response(pergunta)
    
    if float(resposta.confidence) > 0.5:##eae
      print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')
 
