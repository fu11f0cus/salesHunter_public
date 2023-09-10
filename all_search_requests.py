from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.exceptions import TelegramBadRequest
import os

from all_data import stores, brands_by_site
from parse_requests.german_parse_requests import all_german_functions
from parse_requests.poland_parse_requests import all_poland_functions
from parse_requests.italy_parse_requests import all_italy_functions
from parse_requests.spain_parse_requests import all_spain_functions
from parse_requests.gb_parse_requests import all_gb_functions
from parse_requests.usa_parse_requests import all_usa_functions
from parse_requests.france_parse_requests import all_france_functions
from parse_requests.turkey_parse_requests import all_turkey_functions

all_functions = [
    all_german_functions, all_gb_functions, all_poland_functions,
    all_turkey_functions, all_usa_functions, all_france_functions,
    all_spain_functions, all_italy_functions
]

breaklist = {}

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

async def all_search_request_choose(call, brand):
    from all_search import all_search_brand
    from country_choose import savesearch
    savesearch.clear()
    ready_sites = []
    user_id = call.message.chat.id
    msg = call.message.message_id
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    break_btn = types.InlineKeyboardButton(text='Break', callback_data='Break')
    keyboard.add(break_btn)
    breakmsg = await bot.send_message(user_id, text='Break', reply_markup=keyboard)
    await bot.pin_chat_message(user_id, breakmsg.message_id, disable_notification=True)
    flag = False
    for el in stores:
        for item in el:
            if brand in brands_by_site[item] and user_id in all_search_brand:
                ready_sites.append(item)
            else:
                pass
    for function_list in all_functions:
        for el in function_list:
            if el in ready_sites and user_id in all_search_brand:
                await function_list[el](call, brand, 'All')
            if user_id in breaklist:
                flag = True
                break
        if flag:
            await bot.unpin_chat_message(user_id, breakmsg.message_id)
            breaklist.clear()
            break
    else:
        breaklist.clear()
        await bot.unpin_chat_message(user_id, breakmsg.message_id)

def breaklist_push(id, callback):
    breaklist[id] = callback

@dp.callback_query(lambda call: True)
async def all_requests_callbacks_handler(call):
    if call.data == 'Break':
        breaklist_push(call.message.chat.id, call.data)
        print(breaklist)
    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass