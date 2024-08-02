# 30.04 - started
# 01.08 - end
# 01.08 - now need to make searching from all sites in one request, add size filter and paid subsciption
# 05.09 - added size-filters, added paid subscription, succesfully deployed

### This version is public(all names of sites are hidden, because it's paid information)
### This version won't work correctly, here you can just see all alghorytms and use it in your projects, if needeed
### Thanks! If you want use this bot, please follow the link given in repository description

# 17.07 - 4075 lines of code
# 23.07 - 4991 lines of code
# 27.07 - 5763 lines of code
# 29.07 - 6789 lines of code
# 31.07 - 7210 lines of code
# 18.08 - 8553 lines of code

# █████████████████████████████████████████████████
# █───█────█─███───█───█─██─█─█─█─██─█───█───█────█
# █─███─██─█─███─███─███─██─█─█─█──█─██─██─███─██─█
# █───█────█─███───█───█────█─█─█─█──██─██───█────█
# ███─█─██─█─███─█████─█─██─█─█─█─██─██─██─███─█─██
# █───█─██─█───█───█───█─██─█───█─██─██─██───█─█─██
# █████████████████████████████████████████████████

# █▄░▄█ ▄▀▄ █▀▄ █▀▀     █▀▄ ▀▄░▄▀     █▀ █░█ █░█ █░▄▀ ▄▀▀ ▄▀▄ ▄▀ ▀ █▀▀ ▀█▀ ▀▄░▄▀ 
# █░█░█ █▀█ █░█ █▀▀     █▀█ ░░█░░     █▀ █░█ ▄▀▄ █▀▄░ ░▀▄ █░█ █░ █ █▀▀ ░█░ ░░█░░ 
# ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀     ▀▀░ ░░▀░░     ▀░ ░▀░ ▀░▀ ▀░▀▀ ▀▀░ ░▀░ ░▀ ▀ ▀▀▀ ░▀░ ░░▀░░ 


from telebot import types
import asyncio
from aiogram import Bot, Dispatcher, types
import stripe
import re
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramNetworkError, TelegramBadRequest
import subprocess
import json
import os

from other_UI import help_func, list_func, UI_callbacks_handler
from country_choose import countries_choose, country_callbacks_handler
from site_choose import site_callbacks_handler
from brand_choose import brand_callbacks_handler
from size_choose import size_callbacks_handler
from parse_requests.german_parse_requests import german_parse_callbacks_handler
from parse_requests.poland_parse_requests import poland_parse_callbacks_handler
from parse_requests.italy_parse_requests import italy_parse_callbacks_handler
from parse_requests.spain_parse_requests import spain_parse_callbacks_handler
from parse_requests.gb_parse_requests import gb_parse_callbacks_handler
from parse_requests.usa_parse_requests import usa_parse_callbacks_handler
from parse_requests.france_parse_requests import france_parse_callbacks_handler
from parse_requests.turkey_parse_requests import turkey_parse_callbacks_handler
from all_search import allsearch_callbacks_handler
from all_search_requests import all_requests_callbacks_handler


tok = os.getenv('tok')
tok_roflanusers = os.getenv('tok_roflanusers')
token2 = os.getenv('token2')

bot = Bot(token=tok)
userBot = Bot(token=tok_roflanusers)
paymentBot = Bot(token=token2)
dp = Dispatcher()
accessdp = Dispatcher()
paymentdp = Dispatcher()

all_functions = [
    country_callbacks_handler, site_callbacks_handler, brand_callbacks_handler,
    size_callbacks_handler, german_parse_callbacks_handler,
    poland_parse_callbacks_handler, italy_parse_callbacks_handler,
    spain_parse_callbacks_handler, gb_parse_callbacks_handler,
    usa_parse_callbacks_handler, france_parse_callbacks_handler,
    turkey_parse_callbacks_handler, allsearch_callbacks_handler,
    all_requests_callbacks_handler, UI_callbacks_handler
]

stoplist = {}

# def pushfile(userid):
#     with open('user_ids.txt', 'a', encoding='utf-8') as file:
#         file.write(str(userid) + '\n')

@dp.message(Command('start'))
async def begin(message):
    with open('user_ids.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        user_ids_list = [line.strip() for line in lines]
        username = message.chat.username
        firstname = message.chat.first_name
        userid = message.chat.id
        string = f'username - {username} | firstname - {firstname} | ID - {userid}'
        string = str(string)
        try:
            await userBot.send_message('...', f'{string}')
        except TelegramNetworkError:
            pass
    keyboard = InlineKeyboardBuilder()
    start_btn = keyboard.button(text='Start', callback_data='Start')
    help_btn = keyboard.button(text='Help', callback_data='Help')
    list_btn = keyboard.button(text='All sites', callback_data='List')
    try:
        await bot.send_message(message.chat.id, 'Welcome! Цей бот був створений спеціально для ...', reply_markup=keyboard.as_markup())
    except TelegramNetworkError:
        pass

@dp.callback_query(lambda call: True)
async def handle_callback(call: types.CallbackQuery):
    with open('user_ids.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        user_ids_list = [line.strip() for line in lines]
        userid = call.message.chat.id
        username = call.message.chat.username
        firstname = call.message.chat.first_name
        string = f'username - {username} | firstname - {firstname} | ID - {userid}'
        string = str(string)
        if call.data == 'Start':
            if not string in user_ids_list:
                await bot.send_message(
                    userid,
                    'Напишіть будь-ласка свій емаіл \nПриклад: example123@gmail.com'
                )
            else:
                i = 0
                await countries_choose(call, i)
        if call.data == 'Help':
            if string in user_ids_list:
                await help_func(call)
            else:
                await bot.send_message(
                    userid,
                    'Напишіть будь-ласка свій емаіл \nПриклад: example123@gmail.com'
                )
        if call.data == 'List':
            if string in user_ids_list:
                await list_func(call)
            else:
                await bot.send_message(
                    userid,
                    'Напишіть будь-ласка свій емаіл \nПриклад: example123@gmail.com'
                )
        try:
            for handler in all_functions:
                await handler(call)
        except TelegramNetworkError or TelegramBadRequest:
            pass

@dp.message() # content_types=types.ContentTypes.TEXT
async def handle_email(message: types.Message):
    user_text = message.text # .strip()  # Удаляем лишние пробелы в начале и конце

    # Проверяем, соответствует ли введенный текст формату электронной почты
    with open('user_ids.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        user_ids_list = [line.strip() for line in lines]
        userid = message.chat.id
        username = message.chat.username
        firstname = message.chat.first_name
        string = f'username - {username} | firstname - {firstname} | ID - {userid}'
        string = str(string)
        if not string in user_ids_list:
            if re.match(r"[^@]+@[^@]+\.[^@]+", user_text):
                await message.reply("Дякую!")
                mail = user_text
                userid = message.chat.id
                username = message.chat.username
                firstname = message.chat.first_name
                string = f'username - {username} | firstname - {firstname} | ID - {userid} | mail - {mail}'
                await paymentBot.send_message('...', f'{string}')
                keyboard = InlineKeyboardBuilder()
                pay_btn = types.InlineKeyboardButton(
                    text='Оплатити тут',
                    url='...'
                )
                keyboard.row(pay_btn)
                txt = ''
                txt2 = ''
                txt3 = ''
                txt4 = ''
                txt5 = ''
                txt6 = ''
                text = f'{txt}\n{txt2}\n{txt3}\n{txt4}\n{txt5}\n{txt6}'
                await bot.send_message(
                    message.chat.id,
                    text=text,
                    reply_markup=keyboard.as_markup()
                )
            else:
                await message.reply("Введіть будь-ласка коректний адрес почти")

@accessdp.message() # content_types=types.ContentTypes.TEXT
async def access_handle(message: types.Message):
    # if message.text == 'commit':
    #     print(111)
    #     subprocess.run(['git', 'add', '.'], check=True)
    #     subprocess.run(['git', 'commit', '-m', 'auto-commit'], check=True)
    #     subprocess.run(['git', 'push', 'origin', 'master'], check=True)
    # else:
    await bot.send_message(message.text, 'Успішна оплата, дякуємо! Використайте команду "/start"')
    txt = 'Також якщо ви помітили якусь помилку або у вас є якісь пропозиції щодо покращення боту, пишіть у телеграм ... \nГарного використання!'
    await bot.send_message(message.text, txt)

async def main():
    await dp.start_polling(bot)

async def main2():
    await accessdp.start_polling(paymentBot)

if __name__ == '__main__':
    # from aiogram import executor
    # executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(accessdp, skip_updates=True)

    # loop = asyncio.get_event_loop()
    # loop.create_task(dp.start_polling())
    # loop.create_task(accessdp.start_polling())
    # loop.run_forever()
    tasks = [main(), main2()]

    # asyncio.run(asyncio.gather(*tasks))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
