from bs4 import BeautifulSoup
import requests
from telebot import types
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import time
import os

from all_data import (
    xz_brands, xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands_ids, xz_brands, xz_brands,
    xz_brands, xz_brands, xz_brands, xz_brands_ids,
    xz_brands, xz_size_ids
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
url_13 = '...'


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

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    
    if brand == "Levi's":
        clear_brand = 'Levi%27s'
    else:
        clear_brand = brand.replace(' ', '+')

    clear_size = size.replace(' ', '+')
    clear_size = clear_size.replace(':', '%3A')
    if size != 'All':
        replaced = url_1.replace('brand', f'{clear_brand}&filter.v.option.size={clear_size}')
    else:
        replaced = url_1.replace('brand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination__item link')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='grid__item')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='money')
                        x = 0
                        for price in sale_price:
                            x += 1
                            if x % 2 != 0:
                                salepr = price.text
                            else:
                                origpr = price.text

                        product_title = el.find_all('a', class_='full-unstyled-link')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='full-unstyled-link')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://www..../collections')
                        images = el.find_all('img', class_='motion-reduce')
                        caption = f'{title.text} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        y = 0
                        for image in images:
                            y += 1
                            if y % 2 != 0:
                                image_url = image['srcset'].split(',')[1]
                                replacedurl = image_url.replace('//', 'https://')
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

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    for i in range(1, 3):
        url = url_2.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='fbProduct')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand.upper() in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='newPrice')
                        for price in sale_price:
                            clearprice = ' '.join(price.text.split())
                        orig_price = el.find_all('span', class_='oldPrice')
                        for price2 in orig_price:
                            clearprice2 = ' '.join(price2.text.split())
                        product_title = el.find_all('p', attrs={'class': False})
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href'].replace(f'{link["href"]}', f'https://www..../{link["href"]}')
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src'].replace('/Content', 'https://www..../Content')
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    clear_size = size.replace(' ', '+')
    clear_size = clear_size.replace('/', '%2F')
    if size != 'All':
        replaced = url_3.replace('brand', f'{clear_brand}&filter.v.option.size={clear_size}')
    else:
        replaced = url_3.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination__item link')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='grid__item')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='money')
                        x = 0
                        for price in sale_price:
                            x += 1
                            if x % 2 != 0:
                                salepr = price.text
                            else:
                                origpr = price.text

                        product_title = el.find_all('a', class_='full-unstyled-link')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='full-unstyled-link')
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://www..../products')
                        images = el.find_all('img', class_='motion-reduce')
                        caption = f'{title.text} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        y = 0
                        for image in images:
                            y += 1
                            if y % 2 != 0:
                                image_url = image['srcset'].split(',')[1]
                                replacedurl = image_url.replace('//', 'https://')
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

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_4)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('span', class_='page')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1


    for i in range(1, int(totalpages) + 1):
        url = url_4.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='one-fourth column medium-down--one-half thumbnail price_align--center')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price sale')
                        for price in sale_price:
                            salepr = price.text

                        product_title = el.find_all('span', class_='title')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {salepr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src'].replace('//', 'https://')
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '-').lower()
    clear_size = size.replace('.', '-')
    clear_size = clear_size.replace('/', '-').lower()
    if size != 'All':
        replaced = url_5.replace('brand', f'{clear_brand}+size-{clear_size}')
    else:
        replaced = url_5.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='grid__item small--one-half large--one-third medium--one-half has-secondary-image')

    if brand == 'Rassvet':
        brand_to_check = 'Paccbet'
    else:
        brand_to_check = brand

    for el in div:
        if not user_id in stoplist:
            if brand_to_check in el.text and 'OFF' in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='sale-price')
                    for price in sale_price:
                        pass

                    orig_price = el.find_all('s', class_='old-price')
                    for price2 in orig_price:
                        pass

                    product_title = el.find_all('p', attrs={'class': False})
                    for title in product_title:
                        index = title.text.find('Regular')
                        txt = title.text[:index]

                    
                    links = el.find_all('a', attrs={'href': True})
                    for link in links:
                        link_txt = link['href'].replace('/products', 'https://www..../products')
                    images = el.find_all('img', class_='primary-imglazyload')
                    caption = f'{txt} \nSale price - {price.text} \nOld price - {price2.text} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['data-src'].replace('//', 'https://')
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = xz_brands_ids[brand]
    replaced = url_5.replace('brand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='product')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='product__details__prices__price product__details__prices__price--sale')
                    for price in sale_price:
                        saleprice = ' '.join(price.text.split())
                        salepr = saleprice.replace('Jetzt', '')

                    orig_price = el.find_all('span', class_='product__details__prices__rrp product__details__prices__was')
                    for price2 in orig_price:
                        origprice = ' '.join(price2.text.split())
                        origpr = origprice.replace('Vorher', '')

                    product_title = el.find_all('div', class_='product__details__title')
                    for title in product_title:
                        txt = ' '.join(title.text.split())

                    
                    links = el.find_all('a', class_='infclick')
                    for link in links:
                        link_txt = link['href'].replace(f'{link["href"]}', f'https://....com/{link["href"]}')
                    images = el.find_all('img', attrs={'data-src': True})
                    caption = f'{txt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['data-src']
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    if brand == "Levi's":
        clear_brand = 'levis'
    elif brand == 'Lyle & Scott':
        clear_brand = 'lyle-and-scott'
    else:
        clear_brand = brand.replace(' ', '-').lower()

    replaced = url_6.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    viewed = soup.find('div', class_='viewed-products')
    viewtxt = viewed.text

    nums = re.findall(r'\d+', viewtxt)
    totalproducts = int(nums[-1])

    if totalproducts > 60 and totalproducts < 120:
        totalpages = 2
    elif totalproducts > 120:
        totalpages = 3
    elif totalproducts < 60:
        totalpages = 1
    
    for i in range(1, totalpages + 1):
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product-cell box-product')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price product-price')
                        for price in sale_price:
                            clearprice = ' '.join(price.text.split())
                        orig_price = el.find_all('span', class_='value')
                        for price2 in orig_price:
                            clearprice2 = ' '.join(price2.text.split())
                        product_title = el.find_all('a', class_='fn url')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', class_='fn url')
                        for link in links:
                            link_txt = link['href'].replace(f'{link["href"]}', f'https://www..../{link["href"]}')
                        images = el.find_all('img', class_='photo')
                        caption = f'{title.text} \nSale price - {clearprice} \nOld price - {clearprice2} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-src'].replace('//', 'https://')
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    if brand == "Levi's":
        clear_brand = 'levis'
    else:
        clear_brand = brand.replace(' ', '-').lower()

    clear_size = size.replace('.', '-')
    clear_size = clear_size.replace(' ', '-').lower()
    if size != 'All':
        replaced = url_7.replace('name', f'{clear_brand}+size_{clear_size}')
    else:
        replaced = url_7.replace('name', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('span', class_='pagination__page')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='card card--product collection__product')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='money')
                        for price in sale_price:
                            salepr = price.text

                        product_title = el.find_all('h4', class_='card__title card--product__title')
                        for title in product_title:
                            pass
                        
                        links = el.find_all('a', attrs={'aria-label': True})
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://www..../products')
                        images = el.find_all('img', class_='fade-in')
                        caption = f'{title.text} \nSale price - {salepr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-src']
                            replacedurl = image_url.replace('//', 'https://')
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

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    if brand == 'Adidas':
        clear_brand = 'adidas-skateboarding'
    elif brand == 'Dime':
        clear_brand = 'dime-mtl'
    elif brand == 'Rassvet':
        clear_brand = 'rassvet-paccbet'
    elif brand == 'New Balance':
        clear_brand = 'new-balance-numeric'
    else:
        clear_brand = brand.replace(' ', '-').lower()

    clear_size = size.replace(' ', '-').lower()
    if size != 'All':
        replaced = url_7.replace('brand', f'{clear_brand}+size-{clear_size}')
    else:
        replaced = url_7.replace('brand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='product_thumb')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('p', class_='price')
                    for price in sale_price:
                        pass
                    # orig_price = el.find_all('strike')
                    # for price2 in orig_price:
                    #     pass

                    product_title = el.find_all('h3', class_='desktop')
                    for title in product_title:
                        pass

                    
                    links = el.find_all('a', attrs={'href': True})
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('img', attrs={'class': False})
                    caption = f'{title.text} \nPrices - {price.text} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['src'].replace('//', 'https://')
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    
    if brand == "Levi's":
        clear_brand = 'levis'
    else:
        clear_brand = brand.replace(' ', '-').lower()

    replaced = url_8.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='nowPrice-betterSearch')
                    for price in sale_price:
                        salepr = ' '.join(price.text.split())

                    orig_price = el.find_all('span', class_='standardPrice-betterSearch')
                    for price2 in orig_price:
                        origpr = ' '.join(price2.text.split())

                    product_title = el.find_all('a', class_='frItemName')
                    for title in product_title:
                        txt = title.text
                        # txt = ' '.join(title.text.split())

                    
                    links = el.find_all('a', class_='col-1 frItemName')
                    for link in links:
                        link_txt = link['href'].replace('/clothing', 'https://.../clothing')
                    images = el.find_all('img', attrs={'src': True})
                    caption = f'{txt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                    for image in images:
                        print(image)
                        # image_url = image['data-src']
                        # image_response = requests.get(image_url)
                        # image_data = image_response.content
                        # await bot.send_photo(call.message.chat.id, photo=image_data, caption=caption)
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
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    brandid = xz_brands_ids[brand]
    if size != 'All':
        sizeid = xz_size_ids[size]
        replaced = url_8.replace('brid', f'{brandid}&size={sizeid}')
    else:
        replaced = url_8.replace('brid', f'{brandid}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('li', class_='item product product-item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price')
                    i = 0
                    for price in sale_price:
                        i += 1
                        if i % 2 != 0:
                            salepr = price.text
                        else:
                            origpr = price.text

                    product_title = el.find_all('a', class_='product-item-link')
                    for title in product_title:
                        pass

                    
                    links = el.find_all('a', class_='product-item-link')
                    for link in links:
                        link_txt = link['href']
                    images = el.find_all('img', class_='product-image-photo default_image')
                    caption = f'{title.text} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    if size == 'UK 8':
        clear_size = 'uk-8-us-9'
    if size == 'UK 11':
        clear_size = 'uk-11-us-12'
    else:
        clear_size = size.lower()

    if size != 'All':
        replaced = url_9.replace('brand', f'{brand.lower()}+size-{clear_size}')
    else:
        replaced = url_9.replace('brand', f'{brand.lower()}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('li', class_='grid__item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price-item price-item--sale price-item--last')
                    for price in sale_price:
                        salepr = price.text

                    product_title = el.find_all('h3', class_='card__heading h5')
                    for title in product_title:
                        pass

                    
                    links = el.find_all('a', class_='full-unstyled-link')
                    for link in links:
                        link_txt = link['href'].replace('/products', 'https://.../products')
                    images = el.find_all('img', class_='motion-reduce')
                    caption = f'{title.text} \nSale price - {salepr} \nLink - {link_txt}'
                    i = 0
                    for image in images:
                        i += 1
                        if i % 2 != 0:
                            image_url = image['srcset'].split(',')[1]
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

async def xz_products(call, brand, size=None): # unable to make brand filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id
    await bot.send_message(user_id, f'brand - {brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='GB Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '+')
    replaced = url_10.replace('chosenbrand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='Pagination__NavItem')
    for el in pages:
        print(el)
    if pages:
        totalpages = pages[-2].text
    else:
        totalpages = 1

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='ProductItem')

    for i in range(1, int(totalpages) + 1):

        if not user_id in stoplist:
            for el in div:
            # if brand in el.text:
                # if brand in xz_brands:
                sale_price = el.find_all('span', class_='ProductItem__Price Price Price--highlight Text--subdued')
                for price in sale_price:
                    salepr = price.text

                orig_price = el.find_all('span', class_='ProductItem__Price Price Price--compareAt Text--subdued')
                for price in orig_price:
                    origpr = price.text

                product_title = el.find_all('a', attrs={'href': True})
                for title in product_title:
                    pass

                
                links = el.find_all('a', attrs={'href': True})
                for link in links:
                    link_txt = link['href'].replace('/products', 'https://.../products')
                images = el.find_all('img', class_='ProductItem__Image')
                caption = f'{title.text} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                for image in images:
                    image_url = image['src'].replace('//', 'https://')
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


def gb_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def gb_parse_callbacks_handler(call):
    if call.data == 'GB Stop':
        gb_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass


all_gb_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products
}

size_gb_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products
}

nonsize_gb_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products
}