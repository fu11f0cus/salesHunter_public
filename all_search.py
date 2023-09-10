from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.exceptions import TelegramBadRequest
import os

from all_data import (
    all_brands_by_country, brands_two,
    brands
)
from all_search_requests import all_search_request_choose

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

all_search_brand = {}

async def all_brand_choose(call):
    user_id = call.message.chat.id
    buttons = []
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    back_to_main = types.InlineKeyboardButton(text='Back to countries 🔙', callback_data='Back to countries')
    next_page = types.InlineKeyboardButton(text='Next page', callback_data='Next page')
    for el in brands_two[:-65]:
        button = types.InlineKeyboardButton(text=el, callback_data=el + 'allsrch')
        buttons.append(button)
    keyboard.add(*buttons)
    keyboard.add(next_page)
    keyboard.add(back_to_main)
    await bot.edit_message_text('choose brand:', user_id, call.message.message_id)
    await bot.edit_message_reply_markup(user_id, call.message.message_id, reply_markup=keyboard)

async def all_brand_choose2(call):
    user_id = call.message.chat.id
    buttons = []
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    back_to_main = types.InlineKeyboardButton(text='Back to countries 🔙', callback_data='Back to countries')
    prev_page = types.InlineKeyboardButton(text='Previous page', callback_data='Previous page')
    for el in brands_two[65:]:
        button = types.InlineKeyboardButton(text=el, callback_data=el + 'allsrch')
        buttons.append(button)
    keyboard.add(*buttons)
    keyboard.add(prev_page)
    keyboard.add(back_to_main)
    await bot.edit_message_text('choose brand:', user_id, call.message.message_id)
    await bot.edit_message_reply_markup(user_id, call.message.message_id, reply_markup=keyboard)

def allsearch_push(id, callback):
    all_search_brand[id] = callback

@dp.callback_query(lambda call: True)
async def allsearch_callbacks_handler(call):
    user_id = call.message.chat.id
    from country_choose import savesearch
    if call.data == 'Back to countries':
        from country_choose import countries_choose
        await countries_choose(call, 2)
    if call.data == 'Next page':
        await all_brand_choose2(call)
    if call.data == 'Previous page':
        await all_brand_choose(call)
    if user_id in savesearch and 'allsrch' in call.data:
        replaced = call.data.replace('allsrch', '')
        await bot.edit_message_reply_markup(user_id, call.message.message_id, reply_markup=None)
        allsearch_push(call.message.chat.id, replaced)
        await all_search_request_choose(call, replaced)
    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass