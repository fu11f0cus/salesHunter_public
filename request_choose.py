import time
from aiogram import Bot, Dispatcher
import os

from all_data import (
    german_stores, poland_stores, italy_stores,
    spain_stores, greatbritain_stores, usa_stores,
    france_stores, turkey_stores
)

from parse_requests.usa_parse_requests import (
    all_usa_functions, size_usa_functions,
    nonsize_usa_functions
)
from parse_requests.german_parse_requests import (
    all_german_functions, size_german_functions,
    nonsize_german_functions
)
from parse_requests.poland_parse_requests import (
    all_poland_functions, size_poland_functions,
    nonsize_poland_functions
)
from parse_requests.italy_parse_requests import (
    all_italy_functions, size_italy_functions,
    nonsize_italy_functions
)
from parse_requests.spain_parse_requests import (
    all_spain_functions, size_spain_functions,
    nonsize_spain_functions
)
from parse_requests.gb_parse_requests import (
    all_gb_functions, size_gb_functions,
    nonsize_gb_functions
)
from parse_requests.france_parse_requests import (
    all_france_functions, size_france_functions,
    nonsize_france_functions
)
from parse_requests.turkey_parse_requests import (
    all_turkey_functions, nonsize_turkey_functions
)

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

async def country_request(call, country, site, brand, size):
    if country == '🇩🇪 Germany':
        async def generate_german_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)
            if site in german_stores:
                if size is not None:
                    await size_german_functions[site](call, brand, size)
                else:
                    await nonsize_german_functions[site](call, brand)

        if site in german_stores:
            await generate_german_products(call, site, brand)

    if country == '🇵🇱 Poland':

        async def generate_poland_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)
            if site in poland_stores:
                if size is not None:
                    await size_poland_functions[site](call, brand, size)
                else:
                    await nonsize_poland_functions[site](call, brand)

        if site in poland_stores:
            await generate_poland_products(call, site, brand)

    if country == '🇮🇹 Italy':

        async def generate_italy_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)

            if site in italy_stores:
                if size is not None:
                    await size_italy_functions[site](call, brand, size)
                else:
                    await nonsize_italy_functions[site](call, brand)

        if site in italy_stores:
            await generate_italy_products(call, site, brand)
    
    if country == '🇪🇸 Spain':

        async def generate_spain_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)

            if site in spain_stores:
                if size is not None:
                    await size_spain_functions[site](call, brand, size)
                else:
                    await nonsize_spain_functions[site](call, brand)

        
        if site in spain_stores:
            await generate_spain_products(call, site, brand)

    if country == '🇬🇧 Great Britain':

        async def generate_gb_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)

            if site in greatbritain_stores:
                if size is not None:
                    await size_gb_functions[site](call, brand, size)
                else:
                    await nonsize_gb_functions[site](call, brand)

        if site in greatbritain_stores:
            await generate_gb_products(call, site, brand)

    if country == '🇺🇸 USA':

        async def generate_usa_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)

            if site in usa_stores:
                if size is not None:
                    await size_usa_functions[site](call, brand, size)
                else:
                    await nonsize_usa_functions[site](call, brand)

        if site in usa_stores:
            await generate_usa_products(call, site, brand)

    if country == '🇫🇷 France':

        async def generate_france_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)

            if site in france_stores:
                if size is not None:
                    await size_france_functions[site](call, brand, size)
                else:
                    await nonsize_france_functions[site](call, brand)

        if site in france_stores:
            await generate_france_products(call, site, brand)

    if country == '🇹🇷 Turkey':

        async def generate_turkey_products(call, site, brand):
            generate_msg = await bot.send_message(chat_id=call.message.chat.id, text='generating...')
            time.sleep(1)
            await bot.delete_message(call.message.chat.id, generate_msg.message_id)

            if site in turkey_stores:
                if size is None:
                    await nonsize_turkey_functions[site](call, brand)

        if site in turkey_stores:
            await generate_turkey_products(call, site, brand)