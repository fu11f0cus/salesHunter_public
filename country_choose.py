from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import os

from site_choose import sites_choose
from all_data import countries
from all_search import all_brand_choose

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

async def countries_choose(call, i):
    i += 1
    user_id = call.message.chat.id
    if user_id in savesearch:
        del savesearch[user_id]
    msg = call.message.message_id
    keyboard = InlineKeyboardBuilder()
    # keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = []

    for country in countries:
        keyboard.button(text=country, callback_data=country)
        # buttons.append(button)

    keyboard.adjust(2, 2)
    # search_from_all = types.InlineKeyboardButton('Search from all', callback_data='search all')
    # keyboard.add(*buttons)
    # keyboard.add(search_from_all)
    if i <= 1:
        await bot.edit_message_text(text='choose country:', chat_id=user_id, message_id=msg)
        await bot.edit_message_reply_markup(chat_id=user_id, message_id=msg, reply_markup=keyboard.as_markup())
    return keyboard

countrytest = {}
savesearch = {}

def savecountry(id, country):
    countrytest[id] = country

def savesearch_all(id, callback):
    savesearch[id] = callback

@dp.callback_query(lambda call: True)
async def country_callbacks_handler(call):
    if call.data in countries:
        country = call.data
        savecountry(call.message.chat.id, country)
        await sites_choose(call, country)
    # if call.data == 'search all':
    #     savesearch_all(call.message.chat.id, call.data)
    #     print(savesearch)
    #     await all_brand_choose(call)
    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass