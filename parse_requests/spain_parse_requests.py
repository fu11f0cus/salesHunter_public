from bs4 import BeautifulSoup
import requests
from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import time
import os

from all_data import (
    xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands_ids, xz_brands, xz_brands, xz_brands,
    xz_brands
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


stoplist = {}

### need to add 'stoplist.clear()' in beginning of each function

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

async def xz_products(call, brand, size=None): # not working
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = types.InlineKeyboardMarkup()
    stop_btn = types.InlineKeyboardButton('Stop', callback_data='SP Stop')
    stop_keyboard.add(stop_btn)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard)
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    replaced = url_1.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')

    for i in range(1, 3):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='Grid__Cell 1/2--phone 1/3--tablet-and-up 1/4--desk')

        if not user_id in stoplist:
            i += 1
            for el in div:
                # print(el)
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='ProductItem__Price Price Price--highlight Text--subdued')
                        for price in sale_price:
                            pass
                        orig_price = el.find_all('span', class_='ProductItem__Price Price Price--compareAt Text--subdued')
                        for price2 in orig_price:
                            pass
                        product_title = el.find_all('h2', class_='ProductItem__Title Heading')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='ProductItem__Image Image--lazyLoad Image--fadeIn')
                        caption = f'{title.text} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-src'].replace('//', 'https://')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_data, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
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

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    for i in range(1, 24):
        url = url_2.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product')

        if not user_id in stoplist:
            i += 1

            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='woocommerce-Price-amount amount')
                        x = 0
                        for price in sale_price:
                            x += 1
                            if x % 2 != 0:
                                origprice = price.text
                            else:
                                saleprice = price.text
                        # orig_price = el.find_all('span', class_='ProductItem__Price Price Price--compareAt Text--subdued')
                        # for price2 in orig_price:
                        #     pass
                        product_title = el.find_all('div', class_='product-details')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='product-hover-link')
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail')
                        caption = f'{title.text} \nSale price - {saleprice} \nOld price - {origprice} \nLink - {link_txt}'
                        y = 0
                        for image in images:
                            y += 1
                            if y % 2 != 0:
                                image_url = image['src']
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

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+').lower()
    if size == 'talla+%C3%BAnica':
        clear_size = 'talla+única'
    else:
        clear_size = size
    if size != 'All':
        replaced = url_3.replace('brand', f'{clear_brand}/t/{clear_size}')
    else:
        replaced = url_3.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('ul', class_='page-list clearfix text-sm-center')
    if pages:
        for el in pages:
            li = el.find_all('li')
            if li:
                totalpages = li[-2].text
            else:
                totalpages = 1
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='js-product product col-xs-6 col-xl-3')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price')
                        x = 0
                        for price in sale_price:
                            clearprice = ' '.join(price.text.split())
                        orig_price = el.find_all('span', class_='regular-price')
                        for price2 in orig_price:
                            clearprice2 = ' '.join(price2.text.split())
                        product_title = el.find_all('div', class_='h3 product-title')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='thumbnail product-thumbnail')
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src']
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

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '-').upper()
    if size == 'All' or size == '*':
        replaced = url_4.replace('brand', f'{clear_brand}')
    else:
        replaced = url_4.replace('brand', f'{clear_brand}%2Bes_size_{size}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='product_block')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price product-price sale-price')
                    for price in sale_price:
                        clearprice = ' '.join(price.text.split())
                    orig_price = el.find_all('span', class_='old-price product-price')
                    for price2 in orig_price:
                        clearprice2 = ' '.join(price2.text.split())
                    product_title = el.find_all('a', class_='product-name')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='product-name')
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('img', class_='img-product', attrs={'data-srcset': True})
                    caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['data-srcset'].split(',')[2]
                        replacedurl = image_url.replace('//', 'https://')
                        image_response = requests.get(replacedurl)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
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
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    
    response = requests.get(url_5)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='sectiondataarea')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='PBSalesPrice')
                    for price in sale_price:
                        clearprice = ' '.join(price.text.split())
                    orig_price = el.find_all('div', class_='PBStrike')
                    for price2 in orig_price:
                        clearprice2 = ' '.join(price2.text.split())
                    product_title = el.find_all('h3', class_='PBMainTxt')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='PBLink')
                    for link in links:
                        link_txt = link['href']
                        rdylink = link_txt.replace(f'{link_txt}', f'https://.../{link_txt}')
                    images = el.find_all('img', class_='imgthumbnail')
                    caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {rdylink}'
                    for image in images:
                        image_url = image['src'].replace('Files', 'https://.../Files')
                        image_response = requests.get(image_url)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
        else:
            i = 2
            await end_of_function(call, i, user_id, sent.message_id)
            break

    else:
        i = 2
        await end_of_function(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '+')
    if size != 'All':
        replaced = url_6.replace('brand', f'{clear_brand}/Tallas-{size}')
    else:
        replaced = url_6.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='product_list_item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price st_discounted_price')
                    for price in sale_price:
                        clearprice = ' '.join(price.text.split())
                    orig_price = el.find_all('span', class_='regular-price')
                    for price2 in orig_price:
                        clearprice2 = ' '.join(price2.text.split())
                    product_title = el.find_all('div', class_='flex_box flex_start mini_name')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', attrs={'title': True})
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', class_='front-image')
                    caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['src']
                        image_response = requests.get(image_url)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
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
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '-').lower()
    replaced = url_7.replace('chosenbrand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='ajax_block_product')

    for el in div:
        if not user_id in stoplist:
            if brand.upper() in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price')
                    for price in sale_price:
                        clearprice = ' '.join(price.text.split())
                    orig_price = el.find_all('span', class_='regular-price')
                    for price2 in orig_price:
                        clearprice2 = ' '.join(price2.text.split())
                    product_title = el.find_all('h3', class_='h3 product-title')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='thumbnail product-thumbnail')
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', class_='img-fluid')
                    caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['src']
                        image_response = requests.get(image_url)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
        else:
            i = 2
            await end_of_function(call, i, user_id, sent.message_id)
            break

    else:
        i = 2
        await end_of_function(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter ??????
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='SP Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    brandid = xz_brands_ids[brand]

    clear_brand = brand.replace(' ', '').lower()
    clear_size = size.replace(' ', '_')
    clear_size = clear_size.replace('/', '_').lower()
    if size != 'All':
        replaced = url_8.replace('brand', f'{clear_brand}/talla_eu-{clear_size}')
        replaced = replaced.replace('brid', f'{brandid}')
    else:
        replaced = url_8.replace('brand', f'{clear_brand}')
        replaced = replaced.replace('brid', f'{brandid}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    a = soup.find_all('a', class_='js-search-link')
    if list(a):
        totalpages = a[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product_item')
        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand.upper() in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price')
                        for price in sale_price:
                            clearprice = ' '.join(price.text.split())
                        orig_price = el.find_all('span', class_='regular-price')
                        for price2 in orig_price:
                            clearprice2 = ' '.join(price2.text.split())
                        product_title = el.find_all('span', class_='product-title')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='thumbnail product-thumbnail')
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src']
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

def spain_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def spain_parse_callbacks_handler(call):
    if call.data == 'SP Stop':
        spain_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass

all_spain_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products
}

size_spain_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products
}

nonsize_spain_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products
}