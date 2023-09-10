from telebot import types
from request_choose import country_request
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import os

from size_choose import size_choosing
from all_data import (
    brands_two, all_brands_by_country,
    ready_to_sizefilter_german, ready_to_sizefilter_all
)

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

chosen_brand = {}

async def brands_choose(call, site):
    from country_choose import countrytest
    user_id = call.message.chat.id
    msg = call.message.message_id
    brands = None

    if site in all_brands_by_country[countrytest[user_id]]:
        brands = all_brands_by_country[countrytest[user_id]][site]

    if site in all_brands_by_country[countrytest[user_id]]:
        brand_keyboard = InlineKeyboardBuilder()
        buttons = []
        for brand in brands:
            brand_keyboard.button(text=brand, callback_data=brand)
        back_to_countries = types.InlineKeyboardButton(text='Back to countries 🔙', callback_data='Back to countries from brands')
        back_to_sites = types.InlineKeyboardButton(text='Back to sites 🔙', callback_data='Back to sites')
        brand_keyboard.adjust(2)
        brand_keyboard.row(back_to_sites)
        brand_keyboard.row(back_to_countries)
        await bot.edit_message_text(site, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=brand_keyboard.as_markup())

def save_brand(id, callback):
    chosen_brand[id] = callback

@dp.callback_query(lambda call: True)
async def brand_callbacks_handler(call):
    i = 0
    msg = call.message.chat.id
    msgId = call.message.message_id
    from country_choose import countrytest
    if call.data == 'Back to countries from brands':
        from country_choose import countries_choose
        i = 2
        markup = await countries_choose(call, i)
        await bot.edit_message_text('choose country:', msg, msgId)
        await bot.edit_message_reply_markup(msg, msgId, reply_markup=markup.as_markup())

    if call.data == 'Back to sites':
        from site_choose import sites_choose
        site_markup = await sites_choose(call, countrytest[msg])
        try:
            await bot.send_message(msg, text='', reply_markup=site_markup)
        except TelegramBadRequest:
            pass

    from site_choose import callbacks
    for brand in brands_two:
        if call.data in brand and len(call.data) > 1:
            if callbacks:
                i += 1
                if i == 1:
                    save_brand(msg, call.data)
                    if callbacks[msg] in ready_to_sizefilter_all:
                        await size_choosing(call, countrytest[msg], callbacks[msg], call.data)
                    else:
                        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                        await country_request(call, countrytest[msg], callbacks[msg], call.data, None)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass