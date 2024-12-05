from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

bot = ChatBot("chatbot", read_only = False,
                logic_adapters = [
                    {
                        "import_path":"chatterbot.logic.BestMatch",
                        "default_response": "I am sorry, but I do not understand. I am still learning.",
                        "maximum_similarity_threshold": 0.90
                    }
            ])

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")

# trainer = ListTrainer(bot)
# trainer.train([
#     "Hello",
#     "Hello!",
#     "How it's going?",
#     "Not bad!",
#     "How can i lose weight?",
#     "You've got to work our mate!",
#     "Any suggestions?",
#     "Yes, 1- work out, 2- eat healthy, 3- sleep well",
#     "Other suggestions?",
#     "Please visit this link for more info: https://example.com/"
# ])

@app.route("/")
def home():
    return render_template("index.html")

# while True:
#     user_response = input("User: ")
#     print("Chatbot: ", bot.get_response(user_response))

@app.route("/get")
def get_bot_response():
    userText = request.args.get('userMessage')
    rawData = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + userText + "&appid=7cbb755b0caa0671f1a9ead3fd54dfe7")
    result = rawData.json()
    return result

if __name__ == "__main__":
    app.run(debug = True)