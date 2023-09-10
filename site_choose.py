from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import os

from brand_choose import brands_choose
from all_data import stores, all_stores

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

callbacks = {}
callbacks2 = {}

async def sites_choose(call, country):
    user_id = call.message.chat.id
    msg = call.message.message_id
    keys = list(all_stores.keys())
    if country in keys:
        sites = all_stores[country]
        site_keyboard = InlineKeyboardBuilder()
        # site_keyboard = types.InlineKeyboardMarkup(row_width=2) 
        buttons = []
        for site in sites:
            site_keyboard.button(text=site, callback_data=site)
            # buttons.append(button)

        # site_keyboard.add(*buttons)
        back_to_countries = types.InlineKeyboardButton(text='Back to countries 🔙', callback_data='Back to countries')
        site_keyboard.adjust(2)
        site_keyboard.row(back_to_countries)
        # site_keyboard.add(back_to_countries)

        await bot.edit_message_text(country, user_id, msg)
        await bot.edit_message_reply_markup(user_id, message_id=msg, reply_markup=site_keyboard.as_markup())

def savecallback(id, callback):
    callbacks[id] = callback
    callbacks2[id] = callback

@dp.callback_query(lambda call: True)
async def site_callbacks_handler(call):
    msg = call.message.chat.id
    if call.data == 'Back to countries':
        from country_choose import countries_choose
        i = 2
        markup = await countries_choose(call, i)
        msgId = call.message.message_id
        await bot.edit_message_text('choose country:', msg, msgId)
        await bot.edit_message_reply_markup(msg, msgId, reply_markup=markup.as_markup())
    for store in stores:
        if call.data in store:
            await brands_choose(call, call.data)
            savecallback(msg, call.data)
    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass