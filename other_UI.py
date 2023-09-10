from telebot import types
import asyncio
from aiogram import Bot, Dispatcher, types
from country_choose import countries_choose
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import os

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

async def help_func(call):
    user_id = call.message.chat.id
    msg = call.message.message_id
    keyboard = InlineKeyboardBuilder()
    start_usage = keyboard.button(text='Start usage', callback_data='Start usage')
    text = 'This bot was created to automatizate default scrolling sites.'
    guide = '❗️ To start, first choose <b>country 🇺🇦</b> which you want, then choose <b>site 🌐</b> and <b>brand 👕</b> ❗️'
    guide2 = 'Bot will give you all sale items according to your choose'
    guide3 = 'Also you can use <b>Stop 🛑</b> button, which appears once you choose brand\n \
Some sites have lots of sale-products, and bot will give you all\n \
❗️ This process may take about 1-10 minutes 🕗, depending on amount of sale-products ❗️\n \
So If you tired 💤 of waiting you can always use this button and look for something else\n \
Good luck! 🍀'
    text2 = 'Now you can do it much faster. If you have questions, write to ...'
    text3 = 'This is my first medium project, so I hope you will enjoy it! Thanks for using, I appreciate it 😌'
    text4 = 'If you find a mistake or something wrong with bot, please write me and I will fix it as soon as possible'
    text5 = 'Thank you!'
    texts = f'{text} \n{text2} \n{text3} \n{text4} \n{text5}'
    guides = f'{guide} \n{guide2} \n{guide3}'
    await bot.edit_message_text(text=f'{texts} \n{guides}', chat_id=user_id, message_id=msg, parse_mode='HTML')
    await bot.edit_message_reply_markup(chat_id=user_id, message_id=msg, reply_markup=keyboard.as_markup())
    return keyboard


async def list_func(call):
    user_id = call.message.chat.id
    msg = call.message.message_id
    keyboard = InlineKeyboardBuilder()
    start_usage = keyboard.button(text='Start usage', callback_data='Start usage')

    poland = 'POLAND \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>'

    germany = 'GERMANY \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>'

    italy = 'ITALY \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>'

    spain = 'SPAIN \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>'

    gb = 'GREAT BRITAIN \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>'

    usa = 'USA \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>'

    france = 'FRANCE \n<a href="...">...</a>, <a href="...">...</a>, \
<a href="...">...</a>'

    turkey = 'TURKEY \n<a href="...">...</a>, <a href="...">...</a>'
    message = f'{poland} \n{germany} \n{italy} \n{spain} \n{gb} \n{usa} \n{france} \n{turkey}'
    await bot.edit_message_text(text=f'{message}', chat_id=user_id, message_id=msg, parse_mode='HTML')
    await bot.edit_message_reply_markup(chat_id=user_id, message_id=msg, reply_markup=keyboard.as_markup())



@dp.callback_query(lambda call: True)
async def UI_callbacks_handler(call):
    if call.data == 'Start usage':
        with open('user_ids.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            user_ids_list = [line.strip() for line in lines]
            userid = call.message.chat.id
            username = call.message.chat.username
            firstname = call.message.chat.first_name
            userid = call.message.chat.id
            string = f'username - {username} | firstname - {firstname} | ID - {userid}'
            string = str(string)
            if not string in user_ids_list:
                await bot.send_message(userid, 'Access denied')
            else:
                i = 0
                await countries_choose(call, i)
    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass