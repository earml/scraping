# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:41:52 2019

@author: elisa
"""
%reset -f
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Test')

conversa = ['oi', 'olá', 'tudo bem', 'Tudo sim, obrigado',
            'Qual o seu nome', 'Meu nome é Betina :)',
            'qual a sua profissão', 'Eu sou Estatístico',
            'Ah, legal, você entende de economia', 'Sim, um pouco',
            'Então você é tchutchuca', 'kkk']

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.train("chatterbot.corpus.portuguese")
while True:
    quest = input("EU: ")
    resposta = chatbot.get_response(quest)
    print('BETINA: ', resposta)
   
    
