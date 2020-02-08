#Installing collected packages: pint, python-dateutil, pymongo, pyyaml, sqlalchemy, cymem, preshed, wasabi, plac, murmurhash, numpy, srsly, blis, thinc, spacy, pytz, mathparse, nltk, chatterbot

# importing necessary  files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__)

# bot = ChatBot("Candice")
# ChatBot.set_trainer(ListTrainer)
# ChatBot.set_trainer(ChatterBotCorpusTrainer)
# ChatBot.train("chatterbot.corpus.english")

# bot = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(ChatBot)

corpus_path = 'C:/Python/Lib/site-packages/chatterbot_corpus/data/english/'
#trainer.train("chatterbot.corpus.english")

for file in os.listdir(corpus_path):
    print(file)
    #trainer.train(corpus_path + file)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
