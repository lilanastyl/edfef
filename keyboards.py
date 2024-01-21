from telebot import types


btn1 = types.KeyboardButton("/calculator")
btn2 = types.KeyboardButton("/start")
btn3 = types.KeyboardButton("/art")

menu = types.ReplyKeyboardMarkup()



inMenu = types.InlineKeyboardMarkup(row_width=4)


inBtnnC = types.InlineKeyboardButton(text="C", callback_data="C")
inBtnnSK = types.InlineKeyboardButton(text="(", callback_data="(")
inBtnnSKS = types.InlineKeyboardButton(text=")", callback_data=")")
inBtnnPR = types.InlineKeyboardButton(text="%", callback_data="%")
inBtn8 = types.InlineKeyboardButton(text="/", callback_data="/")
inBtnn7 = types.InlineKeyboardButton(text="7", callback_data="7")
inBtnn8 = types.InlineKeyboardButton(text="8", callback_data="8")
inBtnn9 = types.InlineKeyboardButton(text="9", callback_data="9")
inBtn9 = types.InlineKeyboardButton(text="*", callback_data="*")
inBtnn4 = types.InlineKeyboardButton(text="4", callback_data="4")
inBtnn5 = types.InlineKeyboardButton(text="5", callback_data="5")
inBtnn6 = types.InlineKeyboardButton(text="6", callback_data="6")
inBtn6 = types.InlineKeyboardButton(text="-", callback_data="-")
inBtnn1 = types.InlineKeyboardButton(text="1", callback_data="1")
inBtnn2 = types.InlineKeyboardButton(text="2", callback_data="2")
inBtnn3 = types.InlineKeyboardButton(text="3", callback_data="3")
inBtn7 = types.InlineKeyboardButton(text="+", callback_data="+")
inBtnn0 = types.InlineKeyboardButton(text="0", callback_data="0")
inBtn90 = types.InlineKeyboardButton(text=".", callback_data=".")
inBtn5 = types.InlineKeyboardButton(text="=", callback_data="=")





inMenu.add(inBtnnC,inBtnnSK, inBtnnSKS, inBtn8, inBtnn7, inBtnn8, inBtnn9, inBtn9, inBtnn4, inBtnn5, inBtnn6, inBtn6, inBtnn1, inBtnn2, inBtnn3, inBtn7, inBtnnPR, inBtnn0, inBtn90, inBtn5) 
menu.add(btn1,btn2,btn3)