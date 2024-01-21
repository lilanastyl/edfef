from config import TOKEN
import random
import keyboards
import telebot
import json

images = [
    'https://www.imgonline.com.ua/examples/bee-on-daisy.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUAX23TLmLUDFMRc-yPictpjVntgpNb0cI2A&usqp=CAU',
    'https://fotorelax.ru/wp-content/uploads/2016/02/Beautiful-photos-and-pictures-on-different-topics-01.jpg',
    'https://png.pngtree.com/thumb_back/fw800/background/20230524/pngtree-an-anime-girl-looking-at-the-sunset-image_2680365.jpg'
]

datas = {}


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! в этом боте ты сможешь найти арты по играм!!", reply_markup=keyboards.menu)
    bot.send_sticker(message.chat.id, 'https://tlgrm.ru/_/stickers/343/879/34387965-f2d4-4e99-b9e9-85e53b0dbd1f/6.webp')

@bot.message_handler(commands=['art'])
def art(message):
    bot.send_photo(message.chat.id, random.choice(images))

@bot.message_handler(commands=['calculator'])
def help(message):
    bot.send_message(message.chat.id, "Введите выражение для калькулятора:", reply_markup=keyboards.inMenu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global datas
    user_id = call.from_user.id
    with open('peppep.json', 'w') as f:
        json.dump(datas, f)


    datas.setdefault(user_id, "")

    if call.data == "C":
        datas[user_id] = ""
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Калькулятор очищен.", reply_markup=keyboards.inMenu)
    elif call.data.isdigit() or call.data in ['+', '-', '/', '*', '.', '()']:
        datas[user_id] += call.data
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=datas[user_id], reply_markup=keyboards.inMenu)
    elif call.data == "=":
        try:
            result = eval(datas[user_id])
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Результат: {result}", reply_markup=keyboards.inMenu)
            datas[user_id] = str(result)
        except Exception as e:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Ошибка: {e}", reply_markup=keyboards.inMenu)
    
bot.polling(none_stop=True)





