from bs4 import BeautifulSoup
import requests
from telebot import types
from aiogram import Bot, Dispatcher, types
import time
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import os

from all_data import (
    xz_brands, xz_brands, xz_brands
)

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()


url_1 = '...' 
url_2 = '...' 
url_3 = '...' 
url_4 = '...' 


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
    user_id = call.message.chat.id
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='FR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '_').lower()
    clear_size = size.replace('/', '_').lower()
    if size != 'All' and str(size).isalpha():
        replaced = url_1.replace('brand', f'{clear_brand}/taille-{clear_size}')
    if size != 'All' and not str(size).isalpha():
        replaced = url_1.replace('brand', f'{clear_brand}/pointure-{clear_size}')
    else:
        replaced = url_1.replace('brand', f'{clear_brand}')

    if brand == 'Nike':
        totalpages = 2
    else:
        totalpages = 1

    for i in range(1, totalpages + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-container')

        if not user_id in stoplist:
            for el in div:
                span = el.find_all('span', class_='combination')
                for text in span:
                    if size in text.text:
                        if brand in el.text:
                            if brand in xz_brands:
                                sale_price = el.find_all('span', class_='price product-price reduced')
                                for price in sale_price:
                                    salepr = ' '.join(price.text.split())

                                orig_price = el.find_all('span', class_='old-price product-price mr-2')
                                for price in orig_price:
                                    origpr = ' '.join(price.text.split())
                            
                                product_title = el.find_all('a', class_='product-name')
                                for title in product_title:
                                    titletxt = title.text
                                
                                links = el.find_all('a', class_='product-name')
                                for link in links:
                                    link_txt = link['href']
                                images = el.find_all('img', class_='replace-2x img-fluid', attrs={'src': True})
                                caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                                for image in images:
                                    image_url = image['src']
                                    # image_response = requests.get(image_url)
                                    # image_data = image_response.content
                                    await bot.send_photo(chat_id=call.message.chat.id, photo=image_url, caption=caption)
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
    user_id = call.message.chat.id
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='FR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    replaced = url_2.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='u-text-grey-medium')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='c-card-product')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('p', class_='t-surtitle t-surtitle--price')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        # orig_price = el.find_all('del', class_='t-surtitle t-surtitle--price | u-ml-5 3xl:u-ml-5-fluid-width | u-text-grey-medium')
                        # for price in orig_price:
                        #     origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('a', class_='u-block')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='u-block')
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://www.starcowparis.com/products')
                        images = el.find_all('img', class_='c-card-product__thumbnail__img')
                        caption = f'{titletxt} \nPrice - {salepr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-src'].replace('//', 'https://')
                            # image_response = requests.get(image_url)
                            # image_data = image_response.content
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
    user_id = call.message.chat.id
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='FR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    
    response = requests.get(url_3)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='product-container')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price')
                    for price in sale_price:
                        salepr = price.text
                    orig_price = el.find_all('span', class_='old-price')
                    for price in orig_price:
                        origpr = price.text
                    product_title = el.find_all('a', class_='product-name')
                    for title in product_title:
                        titletxt = title.text
                    
                    links = el.find_all('a', class_='product-name')
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', class_='replace-2x img-responsive')
                    caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                    x = 0
                    for image in images:
                        x += 1
                        if x % 2 != 0:
                            image_url = image['src']
                            image_response = requests.get(image['src']).content
                            await bot.send_photo(user_id, photo=image_url, caption=caption)
        else:
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

    stop_keyboard = types.InlineKeyboardMarkup()
    stop_btn = types.InlineKeyboardButton('Stop', callback_data='FR Stop')
    stop_keyboard.add(stop_btn)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard)
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_4)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='ficheArticle ficheListe minibox')

    for el in div:
        print(el)
                



def france_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def france_parse_callbacks_handler(call):
    if call.data == 'FR Stop':
        france_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass


all_france_functions = {
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products
}

size_france_functions = {
    '...': xz_products
}

nonsize_france_functions = {
    '...': xz_products,
    '...': xz_products,
    '...': xz_products
}