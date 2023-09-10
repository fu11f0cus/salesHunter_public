from bs4 import BeautifulSoup
from aiogram.exceptions import TelegramBadRequest
import requests
from telebot import types
from aiogram import Bot, Dispatcher, types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
import time
import os

from all_data import (
    xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands, xz_brands_ids, xz_brands,
    xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands_ids, xz_brands,
    xz_brands, xz_brands, xz_brands, xz_brands,
    xz_brands, xz_brands
)

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()


### need to fix bug with IMAGE PROCESS FAILED /// fixed

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
url_14 = '...'
url_15 = '...'
url_16 = '...'
url_17 = '...'
url_18 = '...' 
url_19 = '...' 
url_20 = '...' 
url_21 = '...' 
url_22 = '...'  
url_23 = '...'
url_24 = '...' 
url_25 = '...' 

stoplist = {}

### need to add 'stoplist.clear()' at beginning of each function

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

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_1)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='Pagination__NavItem')
    totalpages = int(pages[-2].text)

    for i in range(1, totalpages + 1):
        url = url_1.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='ProductItem')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='ProductItem__Price Price Price--highlight Text--subdued')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('span', class_='ProductItem__Price Price Price--compareAt Text--subdued')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('h2', class_='ProductItem__Title Heading')
                        for title in product_title:
                            titletxt = f'{brand}' + title.text
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='ProductItem__Image', attrs={'src': True})
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        x = 0
                        for image in images:
                            x += 1
                            if x % 2 == 0:
                                image_url = image['src'].replace('//', 'https://')
                                image_response = requests.get(image_url)
                                image_data = image_response.content
                                await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    clear_size = size.replace(' ', '+')
    clear_size = clear_size.replace('/', '%2F')
    if size != 'All':
        replaced = url_2.replace('brand', f'{clear_brand}&filter.v.option.size={clear_size}&filter.v.availability=1')
    else:
        replaced = url_2.replace('brand', f'{clear_brand}&filter.v.availability=1')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('li', class_='mx-8 text-12 text-center w-20 h-20 leading-[20px]')
    if pages:
        totalpages = pages[0].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='collection-grid__grid-item pb-32')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('div', class_='product-card__price')
                        for price in sale_price:
                            if '$' in price.text:
                                replacedpr = price.text.replace('$', f'\n$')
                            # clearprice = ' '.join(price.text.split())
                    
                        product_title = el.find_all('a', class_='product-card__title-link')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='product-card__title-link')
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://.../products')
                        images = el.find_all('img', class_='w-full')
                        caption = f'{titletxt} \nPrices - {replacedpr}\n \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_3)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('li', class_='pagination__item')
    
    totalpages = int(pages[-2].text)

    for i in range(1, totalpages + 1):
        url = url_3.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('a', class_='grid__image')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('h4', class_='p-card__price')
                        for price in sale_price:
                            # if '$' in price.text:
                                # replacedpr = price.text.replace('$', f'\n$')
                            clearprice = ' '.join(price.text.split())
                    
                        product_title = el.find_all('h4', class_='p-card__title')
                        for title in product_title:
                            titletxt = f'{brand} {title.text}'
                        
                        links = el.get('href')
                        linktxt = links.replace('/collections', 'https://.../collections')

                        images = el.find_all('img', class_='rollover__img rollover__img--first')
                        caption = f'{titletxt} \nPrices - {clearprice}\n \nLink - {linktxt}'
                        for image in images:
                            image_url = image['src']
                            replacedurl = image_url.replace('//', 'https://')
                            image_response = requests.get(replacedurl)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '-').lower()
    replaced = url_4.replace('chosenbrand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination--item')
    if pages:
        totalpages = pages[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='productitem')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', attrs={'data-price': True})
                        for price in sale_price:
                            salepr = price.text

                        orig_price = el.find_all('span', attrs={'data-price-compare': True})
                        for price in orig_price:
                            origpr = price.text
                    
                        product_title = el.find_all('h2', class_='productitem--title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='productitem--image-primary')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        y = 0
                        for image in images:
                            y += 1
                            if y % 2 != 0:
                                image_url = image['src'].replace('//', 'https://')
                                image_response = requests.get(image_url)
                                image_data = image_response.content
                                await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    if size != 'All':
        replaced = url_5.replace('brand', f'{brand}&filter.v.option.size={size}')
    else:
        replaced = url_5.replace('brand', f'{brand}')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('li', class_='grid__item')

    for el in div:
        if brand in el.text:
            if brand in xz_brands:
                sale_price = el.find_all('span', class_='price-item price-item--sale price-item--last')
                for price in sale_price:
                    salepr = ' '.join(price.text.split())
                    # clearprice = ' '.join(price.text.split())

                orig_price = el.find_all('s', class_='price-item price-item--regular')
                for price in orig_price:
                    origpr = ' '.join(price.text.split())
            
                product_title = el.find_all('a', class_='full-unstyled-link')
                for title in product_title:
                    titletxt = f'{brand}' + title.text
                
                links = el.find_all('a', class_='full-unstyled-link')
                for link in links:
                    link_txt = link['href'].replace('/products', 'https://.../products')
                images = el.find_all('img', class_='motion-reduce')
                caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                y = 0
                for image in images:
                    y += 1
                    if y % 2 != 0:
                        image_url = image['srcset'].split(',')[1]
                        replacedurl = image_url.replace('//', 'https://')
                        image_response = requests.get(replacedurl)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
        else:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break

    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_6)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('li', class_='pagination__page')

    totalpages = pages[-1].text

    for i in range(1, int(totalpages) + 1):
        url = url_6.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-thumbnail')

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
                    
                        product_title = el.find_all('a', class_='product-thumbnail__title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='product-thumbnail__title')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https:/.../collections')
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        y = 0
                        for image in images:
                            y += 1
                            if y % 2 == 0:
                                image_url = image['src'].replace('//', 'https://')
                                image_response = requests.get(image_url)
                                image_data = image_response.content
                                await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                            if y % 3 == 0:
                                continue
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_7)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination__item')

    totalpages = pages[-2].text

    for i in range(1, int(totalpages) + 1):
        url = url_7.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='grid__item')

        if not user_id in stoplist:
            for el in div:
                if brand.upper() in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price-item price-item--sale price-item--last')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('s', class_='price-item price-item--regular')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('a', class_='full-unstyled-link')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='full-unstyled-link')
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://.../products')
                        images = el.find_all('img', class_='motion-reduce')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_8)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('span', class_='page')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = url_8.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product-card')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        orig_price = el.find_all('span', class_='old-price')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())

                        sale_price = el.find_all('p', class_='price')
                        for price in sale_price:
                            if len(price.text) > 6:
                                span_tag = price.find('span')
                                span_tag.extract()
                                salepr = ' '.join(price.text.split())
                    
                        # product_title = el.find_all('h3', class_='p0')
                        # for title in product_title:
                        #     print(title.text)
                        #     if len(title.text) > 14:
                        #         titletxt = title.text
                        
                        # links = el.find_all('a', attrs={'href': True})
                        # for link in links:
                        #     if  '/products' in link['href']:
                        #         link_txt = link['href'] # .replace('/products', 'https://.../products')
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'Sale price - {salepr} \nOld price - {origpr} \nLink - {url_8}'
                        x = 0
                        for image in images:
                            x += 1
                            if x == 1:
                                image_url = image['src'].replace('//', 'https://')
                                image_response = requests.get(image_url)
                                image_data = image_response.content
                                await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                            if x == 2 or x == 3 or x == 4:
                                continue
                            if x > 3:
                                x = 0
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    brandid = xz_brands_ids[brand]
    replaced = url_9.replace('brandid', f'{brandid}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    if size != 'All':
        sizes = soup.find_all('a')
        for el in sizes:
            href = el.get('href')
            if 'size' in href and size in el.text:
                replaced2 = href + '&p={}'
    else:
        replaced2 = replaced

    response2 = requests.get(replaced2)
    soup2 = BeautifulSoup(response2.text, 'lxml')
    pages = soup2.find('div', class_='pages')
    if pages:
        page = pages.find_all('li')
        totalpages = int(page[-2].text)
    else:
        totalpages = 1

    for i in range(1, totalpages + 1):
        url = replaced2.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='item last')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('p', class_='old-price')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('p', class_='special-price')
                        x = 0
                        for price in orig_price:
                            x += 1
                            if x % 2 != 0:
                                origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('a', attrs={'title': True})
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', attrs={'title': True})
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', attrs={'id': True})
                        caption = f'{titletxt} \n{salepr} \n{origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src']
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                            if x == 2 or x == 3 or x == 4:
                                continue
                            if x > 3:
                                x = 0
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '+')
    if size != 'All':
        replaced = url_10.replace('brand', f'{clear_brand}&filter.v.option.size={size}')
    else:
        replaced = url_10.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('li', class_='grid__item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price-item price-item--sale grid-sale-price')
                    for price in sale_price:
                        salepr = ' '.join(price.text.split())
                    orig_price = el.find_all('span', class_='price-item price-item--regular')
                    for price2 in orig_price:
                        origpr = ' '.join(price2.text.split())
                    product_title = el.find_all('div', class_='card-information__text h5 no-line-height light')
                    product_title2 = el.find_all('span', class_='card-information__text h5 no-line-height light')
                    for title in product_title:
                        brandtxt = title.text

                    for title2 in product_title2:
                        modeltxt = title2.text
                    
                    links = el.find_all('a', class_='full-unstyled-link')
                    for link in links:
                        link_txt = link['href'].replace('/products', 'https://.../products')
                    images = el.find_all('img', class_='motion-reduce')
                    caption = f'{brandtxt} {modeltxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['srcset'].split(',')[1]
                        replacedurl = image_url.replace('//', 'https://')
                        image_response = requests.get(replacedurl)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
        else:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    if brand == 'A Bathing Ape':
        brandid = 2

    replaced = url_11.replace('brandid', f'{brandid}')
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
        div = soup.find_all('div', class_='col-lg-6 col-md-6 item-entry mb-4')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('strong', class_='item-price')
                        for price in sale_price:
                            saleprice = price.find_all('span')
                            for saleprtxt in saleprice:
                                salepr = saleprtxt.text
                            origprice = price.find_all('del')
                            for origprtxt in origprice:
                                origpr = origprtxt.text
                    
                        product_title = el.find_all('h2', class_='item-title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='product-item md-height bg-gray d-block')
                        for link in links:
                            link_txt = link['href'].replace('/store', 'https://.../store')
                        images = el.find_all('img', class_='img-fluid')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = types.InlineKeyboardMarkup()
    stop_btn = types.InlineKeyboardButton('Stop', callback_data='USA Stop')
    stop_keyboard.add(stop_btn)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard)
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+').upper()
    replaced = url_12.replace('brand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('div', class_='boost-pfs-filter-bottom-pagination boost-pfs-filter-bottom-pagination-default')
    if pages:
        li = pages.find_all('li')
        totalpages = li[-2].text
    else:
        totalpages = 1

    for i in range(1, 9):
        url = replaced.format(i)
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='boost-pfs-filter-product-item boost-pfs-filter-product-item-grid boost-pfs-filter-grid-width-3 boost-pfs-filter-grid-width-mb-2 has-bc-swap-image boost-pfs-action-list-enabled boost-pfs-action-list-single-button')

        if not user_id in stoplist:
            for el in div:
                print(1)
                if brand.upper() in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='boost-pfs-filter-product-item-regular-price')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('p', class_='boost-pfs-filter-product-item-vendor')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='boost-pfs-filter-product-item-title')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='abc boost-pfs-filter-product-item-main-image')
                        caption = f'{titletxt} \n{salepr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src']
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_data, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '-').lower()
    replaced = url_13.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='grid-product__content')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('div', class_='grid-product__price')
                    for price in sale_price:
                        saleprtxt = ' '.join(price.text.split())
                        salepr = saleprtxt.replace('Regular', '\nRegular').replace('Sale', '\nSale').replace('Save', '\nSave')
                        salepr = salepr.replace('price', 'price - ')

                    product_title = el.find_all('div', class_='grid-product__title grid-product__title--body')
                    for title in product_title:
                        brandtxt = title.text
                    
                    links = el.find_all('a', class_='grid-product__link')
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('div', class_='grid__image-ratio grid__image-ratio--square lazyload')
                    caption = f'{brandtxt} \n{salepr} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['data-bgset'].split(',')[1]
                        replacedurl = image_url.replace('//', 'https://').strip()
                        image_response = requests.get(replacedurl)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
        else:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    response = requests.get(url_14)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='grid-item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='money')
                    x = 0
                    for price in sale_price:
                        x += 1
                        if x % 2 == 0:
                            salepr = ' '.join(price.text.split())
                        else:
                            origpr = ' '.join(price.text.split())

                    product_title = el.find_all('a', class_='product-title change-text')
                    for title in product_title:
                        brandtxt = title.text
                    
                    links = el.find_all('a', class_='product-title change-text')
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('img', class_='lazyload')
                    caption = f'{brandtxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                    y = 0
                    for image in images:
                        y += 1
                        if y % 2 != 0:
                            image_url = image['data-srcset'].split(',')[1]
                            replacedurl = image_url.replace('//', 'https://').strip()
                            image_response = requests.get(replacedurl)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
        else:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '%20')
    replaced = url_15.replace('brand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('span', class_='pagination__number')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-block')

        if not user_id in stoplist:
            for el in div:
                # if brand in el.text:
                if brand in xz_brands:
                        sale_price = el.find_all('span', class_='product-price__item product-price__amount--on-sale')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('span', class_='product-price__item product-price__compare')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())
                    
                        product_title = el.find_all('div', class_='product-block__title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='product-link')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='rimage__image', attrs={'src': True})
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    replaced = url_16.replace('brand', f'{clear_brand}')
    response = requests.get(replaced)

    for i in range(1, 3):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-card')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('div', class_='product-card__price')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())
                            salepr = salepr.replace('$', '\n$')

                        product_title = el.find_all('a', class_='product-card__link')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='product-card__link')
                        for link in links:
                            link_txt = link['href'].replace('/collections/sale', ' ')
                            link_txt = link_txt.replace('/products', 'https://.../collections/sale/products')
                        images = el.find_all('img', class_='product-card__media-primary product-card__image')
                        caption = f'{titletxt} \nPrices - {salepr} \nLink - {link_txt}'
                        for image in images:
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_17)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='Pagination__NavItem Link Link--primary')

    totalpages = pages[-2].text

    for i in range(1, int(totalpages) + 1):
        url = url_17.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='ProductItem')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='ProductItem__Price Price Price--highlight')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        product_title = el.find_all('h2', class_='ProductItem__Title Heading')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='ProductItem__Image Image--lazyLoad Image--fadeIn')
                        caption = f'{titletxt} \nPrices - {salepr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['src']
                            replacedurl = image_url.replace('//', 'https://')
                            image_response = requests.get(replacedurl)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    brandid = xz_brands_ids[brand]
    replaced = url_19.replace('brandid', f'{brandid}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    sizes = soup.find_all('ul', class_='filter__properties filter__properties--size')
    if size != 'All':
        for el in sizes:
            a = el.find_all('a')
            for elm in a:
                if size in elm.text:
                    href = elm.get('href')
                    href = href.replace('/en', 'https://.../en')
                    replaced2 = href.replace('sale?', 'sale/{}?')
                    replaced = replaced2
    else:
        replaced = replaced
    pages = soup.find('span', class_='pagination__total')
    if pages:
        totalpages = pages.text
    else:
        totalpages = 1


    for i in range(1, int(totalpages) + 1):
        # replacedurl = replaced.replace('sale/1', 'sale/{}')
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('article', class_='card product')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price__current')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('del', class_='price__original')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())

                        product_title = el.find_all('strong', class_='card__name')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='card__link')
                        for link in links:
                            link_txt = link['href'].replace('/en', 'https://.../en')
                        images = el.find_all('img', attrs={'srcset': True})
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['srcset'].split(',')[1]
                            replacedurl = image_url.replace('/images', 'https://.../images').strip()
                            image_response = requests.get(replacedurl)
                            image_data = image_response.content
                            # try:
                            await bot.send_photo(call.message.chat.id, photo=replacedurl, caption=caption)
                            # except BadRequest:
                            #     await bot.send_message(call.message.chat.id, 'too much requests, try again later')
                            #     stoplist.clear()
                            #     callbacks.clear()
                            #     from country_choose import countries_choose
                            #     i = 2
                            #     markup = await countries_choose(call, i)
                            #     await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup)
                            #     break

                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    for i in range(1, 20):
        url = url_21.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='item')

        if not user_id in stoplist:
            for el in div:
                if brand.lower() in el.text.lower():
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='price')
                        x = 0
                        for price in sale_price:
                            x += 1
                            if x % 2 != 0:
                                origpr = ' '.join(price.text.split())
                            else:
                                salepr = ' '.join(price.text.split())

                        # orig_price = el.find_all('del', class_='price__original')
                        # for price in orig_price:
                        #     origpr = ' '.join(price.text.split())

                        product_title = el.find_all('h2', class_='product-name')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', attrs={'title': True})
                        for link in links:
                            link_txt = link['href']
                        images = el.find_all('img', class_='defaultImage')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    response = requests.get(url_22)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('ul', class_='pagination')

    page = pages.find_all('li')
    totalpages = page[-2].text

    for i in range(1, int(totalpages) + 1):
        url = url_22.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-item')

        if not user_id in stoplist:
            for el in div:
                if brand.upper() in el.text and 'Sale' in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='money')
                        x = 0
                        for price in sale_price:
                            x += 1
                            if x % 2 != 0:
                                salepr = ' '.join(price.text.split())
                            else:
                                origpr = ' '.join(price.text.split())

                        product_title = el.find_all('p', class_='title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='circle sale')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    clear_size = size.replace(' ', '+')
    clear_size = clear_size.replace('/', '%2F')
    if size != 'All':
        replaced = url_23.replace('brand', f'{clear_brand}&filter.v.option.size={clear_size}')
    else:
        replaced = url_23.replace('brand', f'{clear_brand}')

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

                        product_title = el.find_all('a', class_='full-unstyled-link')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='full-unstyled-link')
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://.../products')
                        images = el.find_all('img', class_='motion-reduce')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['srcset'].split(',')[1].replace('//', 'https://')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '-').lower()
    if size != 'All':
        replaced = url_24.replace('brand', f'{clear_brand}&shoeSize={size}')
    else:
        replaced = url_24.replace('brand', f'{clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='button pagination-next')
    if pages:
        totalpages = 3
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product-list-item')

        if not user_id in stoplist:
            for el in div:
                if brand.lower() in el.text.lower():
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='discounted')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())
                            salepr = salepr.replace('sale/discounted price', ' ')

                        orig_price = el.find_all('span', class_='original')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())
                            origpr = origpr.replace('original price', ' ')

                        product_title = el.find_all('h2', class_='product-tile-title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='product-tile-link')
                        for link in links:
                            link_txt = link['href'].replace('/products', 'https://.../products')
                        images = el.find_all('img', class_='product-tile-image')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
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
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+').upper()
    replaced = url_25.replace('chosenbrand', f'{clear_brand}')

    totalpages = 3

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='boost-pfs-filter-product-item-inner')

        if not user_id in stoplist:
            for el in div:
                if brand.upper() in el.text.upper():
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='boost-pfs-filter-product-item-sale-price')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('s')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())

                        product_title = el.find_all('a', class_='boost-pfs-filter-product-item-title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='boost-pfs-filter-product-item-title')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='boost-pfs-filter-product-item-main-image')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-src'].split(',')[0].replace('//', 'https://')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+').upper()
    replaced = url_25.replace('chosenbrand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('div', class_='boost-pfs-filter-bottom-pagination boost-pfs-filter-bottom-pagination-default')
    if pages:
        page = pages.find_all('li')
        totalpages = page[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='boost-pfs-filter-product-item-inner')

        if not user_id in stoplist:
            for el in div:
                if brand.lower() in el.text.lower():
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='boost-pfs-filter-product-item-sale-price')
                        for price in sale_price:
                            salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('s')
                        for price in orig_price:
                            origpr = ' '.join(price.text.split())

                        product_title = el.find_all('a', class_='boost-pfs-filter-product-item-title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='boost-pfs-filter-product-item-title')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='boost-pfs-filter-product-item-main-image')
                        caption = f'{titletxt} \nSale price - {salepr} \nOld price - {origpr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-src'].split(',')[0].replace('//', 'https://')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='USA Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    clear_size = size.replace(' ', '+')
    clear_size = clear_size.replace('/', '%2F')
    if size != 'All':
        replaced = url_25.replace('brand', f'{clear_brand}&filter.v.option.size={clear_size}')
    else:
        replaced = url_25.replace('brand', f'{clear_brand}')
    
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('ul', class_='pagination flex items-center')
    if pages:
        page = pages.find_all('li')
        totalpages = page[-2].text.replace('page', ' ')
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='col-span-1 lg:col-span-3 bg-scheme-background text-scheme-text')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('div', class_='text-left lg:w-2/5 lg:text-right mt-1 lg:mt-0 lg:pl-2')
                        for price in sale_price:
                            saleprice = price.find_all('span', class_='text-scheme-accent')
                            for pr in saleprice:
                                salepr = ' '.join(pr.text.split())
                            # origprice = price.find_all('s')
                            # for pr in origprice:
                            #     origpr = ' '.join(pr.text.split())


                        # orig_price = el.find_all('s')
                        # for price in orig_price:
                        #     origpr = ' '.join(price.text.split())

                        product_title = el.find_all('p', class_='product-grid-title')
                        for title in product_title:
                            titletxt = title.text
                        
                        links = el.find_all('a', class_='increase-target')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('div', class_='product-item-hover bg-scheme-background lazyload absolute top-0 left-0 bottom-0 right-0 opacity-0 z-10 bg-cover bg-no-repeat bg-center transition-opacity duration-200 ease-in-out group-hover:opacity-100')
                        caption = f'{titletxt} \n{salepr} \nLink - {link_txt}'
                        for image in images:
                            image_url = image['data-bgset'].split(',')[2].replace('//', 'https://').strip()
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                    if user_id in stoplist:
                        flag = True
                        break
        if flag:
            i = 2
            await end_of_fucntion(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_fucntion(call, i, user_id, sent.message_id)


def usa_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def usa_parse_callbacks_handler(call):
    if call.data == 'USA Stop':
        usa_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass


all_usa_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products
}

size_usa_functions = {
    '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products
}

nonsize_usa_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products, '...': xz_products
}