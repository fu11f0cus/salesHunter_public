from bs4 import BeautifulSoup
import requests
from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import time
import os

from all_data import xz_brands, xz_brands

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()


url_1 = '...'
url_2 = '...'


stoplist = {}

### MIGRATED TO AIOGRAM 3

async def end_of_function(call, i, userid, messageid):
    from site_choose import callbacks
    await bot.unpin_chat_message(userid, messageid)
    stoplist.clear()
    callbacks.clear()
    from country_choose import countries_choose
    i = 2
    markup = await countries_choose(call, i)
    await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup.as_markup())

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='TR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '-').lower()
    replaced = url_1.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('li', class_='page-item')
    if pages:
        totalpages = pages[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='h-100 border bc-parchment')

        if not user_id in stoplist:
            for el in div:
                if brand.lower() in el.text.lower():
                    if brand in xz_brands:
                        sale_price = el.find_all('strong', class_='product-price urunKategoriFiyat')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('span', class_='urunEskiFiyat')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('span', class_='product-name')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', class_='card-img-top')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-rsrc']
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_function(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_function(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='TR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_2)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('ul', class_='pagination')
    if pages:
        totalpages = pages.find_all('li')
        totalpages = totalpages[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = url_2.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-item')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='money')
                        x = 0
                        for price in sale_price:
                            x += 1
                            if x % 2 != 0:
                                salepr = ' '.join(price.text.split())
                            else:
                                origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('h3', class_='product-item__title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='img')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-srcset'].split(',')[1]
                            replacedurl = image_url.replace('//', 'https://').strip()
                            image_response = requests.get(replacedurl)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_function(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_function(call, i, user_id, sent.message_id)



def turkey_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def turkey_parse_callbacks_handler(call):
    if call.data == 'TR Stop':
        turkey_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass


all_turkey_functions = {
    '...': xz_products,
    '...': xz_products
}

nonsize_turkey_functions = {
    '...': xz_products,
    '...': xz_products
}