import telebot
from bs4 import BeautifulSoup
import requests
import time
from telebot import types
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import os

from all_data import (
    xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands, xz_brands_ids, xz_brands,
    xz_brands, xz_shoesize_ids, xz_textilesize_ids
)


tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

url_1 = '...' 
url_2 = '...' 
url_3 = '...'
url_4 = '...'  
url_5 = '...' 
url_6 = '...' 
url_7 = '...' 
url_8 = '...' 
url_9 = '...' 
url_10 = '...' 
url_11 = '...' 
url_12 = '...' 

stoplist = {}
size = {}

### need to add 'stoplist.clear()' in beginning of each function

### MIGRATED TO AIOGRAM 3

async def end_of_fucntion(call, i, userid, messageid):
    from site_choose import callbacks
    await bot.unpin_chat_message(userid, messageid)
    stoplist.clear()
    callbacks.clear()
    from country_choose import countries_choose
    i = 2
    markup = await countries_choose(call, i)
    await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup.as_markup())

### size filter - Done 02.08 - 23:34
async def xz_products(call, brand, size=None):
    start_time = time.time()
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')
    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    if brand == "Levi's":
        clear_brand = 'Levi%27s'
    else:
        clear_brand = brand.replace(' ', '+')
    if size == 'All':
        replaced = url_1.replace('sale/?', f'sale/?brand={clear_brand}&')
    else:
        replaced = url_1.replace('sale/?', f'sale/?brand={clear_brand}&size={size}&')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find_all('div', class_='productCardView___S9aHm')
    i = 0

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('div', class_='discountedPrice')
                    for price in sale_price:
                        pass
                    orig_price = el.find_all('div', class_='regularPrice___kxVni')
                    for price2 in orig_price:
                        pass
                    product_title = el.find_all('div', class_='title___faBdX')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='productCard___dCpiR')
                    for link in links:
                        link_txt = link['href'].replace('/en', 'https://.../en')
                    images = el.find_all('img', class_='image___OjPEl')
                    caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                    for image in images:
                        i += 1
                        if i % 2 == 0: 
                            image_url = image['src']
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            # try:
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                            # except BadRequest:
                            #     await bot.send_message(call.message.chat.id, 'image process failed, please try again')
                            #     stoplist.clear()
                            #     callbacks.clear()
                            #     from country_choose import countries_choose
                            #     i = 2
                            #     markup = await countries_choose(call, i)
                            #     await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup)
                            #     break
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break

    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

    end_time = time.time()
    total = end_time - start_time
    print(f'time - {total}')

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    x = 0
    user_id = call.message.chat.id
    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='GR Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    for i in range(1, 3):
            url = url_2.format(i)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            div = soup.find_all('li', class_='product-type-classic')

            if not user_id in stoplist:

                if not div:
                    break
                for el in div:
                    i += 1
                    if brand in el.text:
                        if brand in xz_brands:
                            links = el.find_all('a', class_='product-thumbnail')
                            for link in links:
                                href = link['href']

                            titles = el.find_all('h3', class_='product-title')
                            for title in titles:
                                title.text

                            price = el.find_all('span', class_='woocommerce-Price-amount')
                            for pr in price:
                                x += 1
                                if x % 2 == 0:
                                    sale_price = pr
                                else:
                                    orig_price = pr

                            images = el.find_all('img', class_='product-img')
                            caption = f'{title.text} \nSale price - {sale_price.text} \nOld price - {orig_price.text} \nLink: {href}'
                            for image in images:
                                image_url = image['src']
                                image_response = requests.get(image_url)
                                image_data = image_response.content
                                await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
            if flag:
                if not all_search_brand:
                    i = 2
                    await end_of_fucntion(call, i, user_id, sent.message_id)
                break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # ?????? need to fix
    stoplist.clear()
    from site_choose import callbacks
    x = 0
    user_id = call.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    stop_btn = types.InlineKeyboardButton('Stop', callback_data='GR Stop')
    keyboard.add(stop_btn)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard)
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    url = url_3
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='col', attrs={'id': False})
    i = 0

    for el in div:
        if not user_id in stoplist:
            i += 1
            if brand in el.text:
                if brand in xz_brands:
                    links = el.find_all('a', class_='product-card')
                    for link in links:
                        href = link['href'].replace('/products', 'https:/.../products')

                    titles = el.find_all('p', class_='card-title')
                    for title in titles:
                        title.text

                    price = el.find_all('span', class_='price')
                    for orig_price in price:
                        orig_price.text
                    
                    saleprice = el.find_all('span', class_='strike')
                    for sale_price in saleprice:
                        sale_price.text

                    images = el.find_all('img', class_='lazyload', attrs={'data-src': True})
                    caption = f'{title.text} \nSale price - {sale_price.text} \nOld price - {orig_price.text} \nLink: {href}'
                    for image in images:
                        image_url = image['data-src'].replace('//', 'https://')
                        image_response = requests.get(image_url)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=image_data, caption=caption)
        else:
            await bot.unpin_chat_message(user_id, sent.message_id)
            stoplist.clear()
            callbacks.clear()
            from country_choose import countries_choose
            i = 2
            markup = await countries_choose(call, i)
            await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup)
            break

    else:
        await bot.unpin_chat_message(user_id, sent.message_id)
        from country_choose import countries_choose
        i = 2
        markup = await countries_choose(call, i)
        callbacks.clear()
        await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id
    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='GR Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    clear_brand = brand.replace(' ', '+')
    if size != 'All':
        replaced = url_4.replace('sale?', f'sale?filter.p.vendor={clear_brand}&filter.v.option.größe={size}&')
    else:
        replaced = url_4.replace('sale?', f'sale?filter.p.vendor={clear_brand}&')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination__item link')
    if pages:
        totalpages = list(pages)[-1].text
    else:
        totalpages = 1


    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='grid__item')
        i = 0

        if not user_id in stoplist:
            if not div:
                break

            for el in div:
                i += 1
                if brand in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', class_='sm-product-card')
                        for link in links:
                            href = link['href'].replace('/products', 'https://.../products')

                        titles = el.find_all('span', class_='sm-product-card__title')
                        for title in titles:
                            title.text

                        price = el.find_all('div', class_='regular')
                        for orig_price in price:
                            orig_price.text
                        
                        saleprice = el.find_all('span', class_='sale-price')
                        for sale_price in saleprice:
                            sale_price.text

                        images = el.find_all('img', class_='sm-product-card__image-source')
                        caption = f'{title.text} \nSale price - {sale_price.text} \nOld price - {orig_price.text} \nLink: {href}'
                        for image in images:
                            image_url = image['srcset'].split(',')[7].replace('//', 'https://')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)

                if user_id in stoplist:
                    flag = True
                    break
        if flag:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id
    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='GR Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    for i in range(1, 3):
        response = requests.get(url_5.format(i))
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find_all('div', class_='product--box')

        for el in div:
            if not user_id in stoplist:
                i += 1
                if brand in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', class_='product--title')
                        for link in links:
                            href = link['href']

                        titles = el.find_all('a', class_='product--title')
                        for title in titles:
                            title.text

                        price = el.find_all('span', class_='price--pseudo')
                        for orig_price in price:
                            orig_price.text
                        
                        saleprice = el.find_all('span', class_='price--default is--nowrap is--discount')
                        for sale_price in saleprice:
                            sale_price.text

                        images = el.find_all('img', attrs={'srcset': True})
                        caption = f'{title.text} \nSale price - {sale_price.text} \nOld price - {orig_price.text} \nLink: {href}'
                        for image in images:
                            image_url = image['srcset'].split(',')[0]
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id
    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='GR Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    response = requests.get(url_6)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='grid-item')
    i = 0

    for el in div:
        if not user_id in stoplist: 
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='special-price')
                    for price in sale_price:
                        pass
                    orig_price = el.find_all('span', class_='old-price')
                    for price2 in orig_price:
                        pass
                    product_title = el.find_all('a', class_='product-title')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='product-grid-image adaptive_height')
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('img', class_='lazyload')
                    caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                    for image in images:
                        i += 1
                        if i % 2 != 0:
                            image_url = image['data-srcset']
                            split = image_url.split(',')[1]
                            replaced = split.replace('//', 'https://')
                            last_index = replaced.rfind(' ')
                            result = replaced[:last_index].strip()
                            image_response = requests.get(replaced)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=result, caption=caption)
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id
    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='GR Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    response = requests.get(url_7)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='group relative')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    links = el.find_all('a', class_='absolute left-0 top-0 h-full w-full')
                    for link in links:
                        href = link['href'].replace('/products', 'https://.../products')

                    titles = el.find_all('a', class_='hover:underline')
                    for title in titles:
                        title.text

                    price = el.find('div', class_='mt-3 flex text-lg')
                    i = 0
                    for prices in price:
                        i += 1
                        if i % 2 != 0:
                            orig_price = prices.text
                        else:
                            sale_price = prices.text

                    images = el.find_all('img', class_='absolute h-full w-full transform bg-cover bg-center object-cover object-center ease-in-out')
                    caption = f'{title.text} \nSale price - {sale_price} \nOld price - {orig_price} \nLink: {href}'
                    for image in images:
                        image_url = image['srcset'].split(',')[4].strip()
                        image_response = requests.get(image_url)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand.lower()}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    upper_brand = brand
    if brand != 'asics':
        upper_brand = brand.upper()

    clear_brand = upper_brand.replace(' ', '%20')
    replaced = url_8.format(clear_brand)

    if ' ' in size:
        clear_size = size.replace(' ', '%20')
    else:
        clear_size = size

    replaced = replaced.replace('f8', f'f4:o{clear_size};f8')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find_all('li', class_='productData')

    for el in div:
        if not user_id in stoplist:
            if upper_brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='new')
                    for price in sale_price:
                        pass
                    orig_price = el.find_all('span', class_='old')
                    for price2 in orig_price:
                        pass
                    product_title = el.find_all('div', class_='gridInfo')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', attrs={'href': True})
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', class_='lazy')
                    caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['data-src']
                        image_response = requests.get(image['data-src']).content
                        await bot.send_photo(user_id, photo=image_url, caption=caption)
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break

    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '_').lower()
    replaced = url_8.format(clear_brand)

    if size != 'All':
        if size in xz_shoesize_ids:
            sizeid = xz_shoesize_ids[size]
            replaced = replaced.replace(f'{clear_brand}', f'{clear_brand}?size_shoe={sizeid}')
        if size in xz_textilesize_ids:
            sizeid = xz_textilesize_ids[size]
            replaced = replaced.replace(f'{clear_brand}', f'{clear_brand}?size_textil={sizeid}')
    else:
        replaced = replaced

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find_all('li', class_='item product product-item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    i = 0
                    prices = el.find_all('span', class_='price')
                    for price in prices:
                        i += 1
                        if i % 2 != 0:
                            sale_price = price.text
                        else:
                            orig_price = price.text

                    product_title = el.find_all('a', class_='product-item-link')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='product-item-link')
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', class_='photo image')
                    caption = f'{title.text} \nSale price - {sale_price} \nLink - {link_txt}'
                    for image in images: 
                        image_url = image['src']
                        image_response = requests.get(image['src']).content
                        await bot.send_photo(user_id, photo=image_url, caption=caption)
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False


    for i in range(1, 3):
        url = url_9.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product--box')
        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price--default')
                        for price in sale_price:
                            pass
                        orig_price = el.find_all('span', class_='price--discount')
                        for price2 in orig_price:
                            pass
                        product_title = el.find_all('a', class_='product--title')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='product--title')
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', attrs={'srcset': True})
                        caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['srcset']
                            split = image_url.split(',')[0]
                            image_response = requests.get(split)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=split, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
                            
async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    brand_id = xz_brands_ids[brand]
    replaced = url_10.replace('sale/', f'sale/?p=1&o=1&n=48&s={brand_id}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find_all('div', class_='product--box')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price--default')
                    for price in sale_price:
                        pass
                    orig_price = el.find_all('span', class_='price--discount')
                    for price2 in orig_price:
                        pass
                    product_title = el.find_all('a', class_='product--title')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='product--title')
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', attrs={'srcset': True})
                    caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                    i = 0
                    for image in images:
                        i += 1
                        if i % 2 != 0:
                            image_url = image['srcset']
                            split = image_url.split(',')[0]
                            image_response = requests.get(split)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=split, caption=caption)
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GR Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    if size != 'All':
        replaced = url_11.replace('sale?', f'sale?filter.p.vendor={brand.upper()}&filter.v.option.size={size}')
    else:
        replaced = url_11.replace('sale?', f'sale?filter.p.vendor={brand.upper()}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find_all('div', class_='product-block')

    for el in div:
        if not user_id in stoplist:
            if brand.upper() in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='product-price__amount--on-sale')
                    for price in sale_price:
                        pass
                    orig_price = el.find_all('span', class_='product-price__compare')
                    for price2 in orig_price:
                        pass
                    product_title = el.find_all('div', class_='product-block__title')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='product-link')
                    for link in links:
                        link_txt = link['href'].replace('/product', 'https://.../product')
                    images = el.find_all('img', class_='rimage__image')
                    caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                    i = 0
                    for image in images:
                        i += 1
                        if i % 2 != 0:
                            image_url = image['src'].replace('//.../cdn', 'https://.../cdn')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
        else:
            if not all_search_brand:
                i = 2
                await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)

def german_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def german_parse_callbacks_handler(call):
    if call.data == 'GR Stop':
        german_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass

all_german_functions = {
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products,
    '...': xz_products
}

size_german_functions = {
    '...': xz_products, '...' :xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products
}

nonsize_german_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products
}