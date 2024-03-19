import openai
import telebot
from config import OPEN_AI,BOT_API
chatstr=''
def chatModel(prompt):
    global chatstr
    openai.api_key=OPEN_AI
    chatstr+= f"Luffy:{prompt}/nvitts:"
    response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=chatstr,
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
    print(response)
    chatstr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']


bot=telebot.TeleBot(BOT_API)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"hello,...welcome to luffyBot")
    #print(message)
@bot.message_handler()
def chat(message):
   

    #print(message.text)
    try:
        reply=chatModel(message.text)
        bot.reply_to(message,reply)
    except Exception as e:
        bot.reply_to(message,e)
    
print('Bot started......')
bot.polling()