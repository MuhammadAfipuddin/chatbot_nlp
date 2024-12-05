from chatterbot import ChatBot

bot = ChatBot ("Units", logic_adapters = ['chatterbot.logic.UnitConversion'])

while True:
    user_text = input("Ask a question (unit conversation): ")
    chatbot_response = str(bot.get_response(user_text))
    print (chatbot_response)