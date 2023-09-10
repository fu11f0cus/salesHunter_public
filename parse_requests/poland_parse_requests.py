from bs4 import BeautifulSoup
import requests
from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import time
import os

from all_data import (
    xz_brands, xz_brands, xz_brands, xz_brands_ids,
    xz_brands, xz_brands, xz_brands, xz_brands_ids,
    xz_size_ids
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

stoplist = {}

### need to add 'stoplist.clear()' in beginning of each function

### MIGRATED TO AIOGRAM 3

async def send_keyboard(call, i, userid, messageid):
    from site_choose import callbacks
    await bot.unpin_chat_message(userid, messageid)
    stoplist.clear()
    callbacks.clear()
    from country_choose import countries_choose
    markup = await countries_choose(call, i)
    await bot.send_message(call.message.chat.id, 'choose country: ', reply_markup=markup.as_markup())

async def process_product_info(call, el):
        for link in el.find_all('a', class_='cvn-product'):
            href = link['href']
        titles = el.find_all('h4', class_='title')
        for title in el.find_all('h4', class_='title'):
            pass
        sale_price = el.find_all('span', class_='new')
        for salepr in sale_price:
            pass
        orig_price = el.find_all('del')
        for origpr in orig_price:
            pass
        images = el.find_all('img', class_='lazy', attrs={'data-srcset': True})
        caption = f'{title.text} \nSale price - {salepr.text} \nOld price - {origpr.text} \nLink: {href}'

        image_url = images[0]['data-srcset'].split(',')[1] if images else ''
        if image_url:
            url = image_url.strip()
            image_response = requests.get(image_url)
            image_data = image_response.content
            await bot.send_photo(call.message.chat.id, photo=url, caption=caption)
        

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id

    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='PL Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    clear_brand = brand.replace(' ', '-')
    replaced = url_1.replace('/wy', f'/{clear_brand}/wy')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('li', class_='pagination-span')
    if pages is not None:
        pagestxt = pages.text
        totalpages = pagestxt[-1]
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        clear_brand = brand.replace(' ', '-')
        replaced = url_1.replace('/wy', f'/{clear_brand}/wy')
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product-box')
        i = 0

        if not user_id in stoplist:
            if not div:
                break
            for el in div:
                variants = el.find_all('div', class_='variants')
                for var in variants:
                    if brand in el.text:
                        i += 1
                        if size in var.text:
                            if brand in xz_brands:
                                await process_product_info(call, el)
                    if brand in el.text:
                        i += 1
                        if size == 'All':
                            if brand in xz_brands:
                                await process_product_info(call, el)
                    if user_id in stoplist:
                        flag = True
                        break
                if flag:
                    break
        if flag:
            i = 2
            if not all_search_brand:
                await send_keyboard(call, i, user_id, sent.message_id)
            break

    else:
        i = 2
        if not all_search_brand:
            await send_keyboard(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id

    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='PL Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    clear_brand = ''
    if 'Lyle & Scott' in brand:
        clear_brand = 'lyle_scott'
    elif "Levi's" in brand:
        clear_brand = 'levis_r'
    elif 'C.P. Company' in brand:
        clear_brand = 'c_p_company'
    else:
        clear_brand = brand.replace(' ', '_')
    replaced = url_2.replace('okazja', f'okazja/marka:{clear_brand.lower()}')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination-item')
    if pages:
        totalpages = pages[-1].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product')

        if not user_id in stoplist:
            for el in div:
                i += 1
                if brand in el.text and 'Cena regularna' in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', class_='product-card-link')
                        for link in links:
                            href = link['href'].replace('/p', 'https://.../p')

                        titles = el.find_all('span', class_='product-card-name')
                        for title in titles:
                            title.text

                        sale_price = el.find_all('div', class_='price is-sale')
                        for salepr in sale_price:
                            salepr.text
                        
                        orig_price = el.find_all('div', class_='price-information')
                        for origpr in orig_price:
                            origpr.text

                        images = el.find_all('img', class_='image', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {salepr.text} \nOld price - {origpr.text} \nLink: {href}'
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
                await send_keyboard(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await send_keyboard(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id

    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='PL Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    brand_id = xz_brands_ids[brand]
    replaced = url_3.replace('sale', f'sale?brand_id={brand_id}')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('div', class_='listing-menu-entry listing-menu-pagination-label listing-pagination-label')
    totalpages = pages.get('data-pages')
    

    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='listing-product')

        if not user_id in stoplist:
            for el in div:
                i += 1
                if brand in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', attrs={'href': True})
                        for link in links:
                            href = link['href']

                        titles = el.find_all('div', class_='listing-product-name')
                        for title in titles:
                            title.text

                        sale_price = el.find_all('div', class_='listing-product-price-new')
                        for salepr in sale_price:
                            clean_salepr = ' '.join(salepr.text.split())
                        
                        orig_price = el.find_all('div', class_='listing-product-price-old')
                        for origpr in orig_price:
                            clean_origpr = ' '.join(origpr.text.split())

                        images = el.find_all('img', class_='listing-product-image')
                        caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink: {href}'
                        for image in images:
                            image_url = image['data-sources'].split(',')[0]
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_url, caption=caption)
                if user_id in stoplist:
                    flag = True
                    break
        if flag:
            if not all_search_brand:
                i = 2
                await send_keyboard(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await send_keyboard(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None):
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id

    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='PL Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    clear_brand = ''
    if "Levi's" in brand:
        clear_brand = 'levis_r'
    else:
        clear_brand = brand.replace(' ', '_')
    replaced = url_4.replace('okazja', f'okazja/marka:{clear_brand.lower()}')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='pagination-item')
    if pages:
        totalpages = pages[-1].text
    if not pages:
        totalpages = 1


    for i in range(1, int(totalpages) + 1):
        url = replaced.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product-item')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', class_='product-card-link')
                        for link in links:
                            href = link['href'].replace('/p', 'https://.../p')

                        titles = el.find_all('h2', class_='product-name')
                        for title in titles:
                            title.text

                        sale_price = el.find_all('div', class_='price-final is-sale')
                        for salepr in sale_price:
                            clean_salepr = ' '.join(salepr.text.split())

                        orig_price = el.find_all('div', class_='information-price')
                        for origpr in orig_price:
                            origpr.text

                        images = el.find_all('img', class_='image')
                        caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {origpr.text} \nLink: {href}'
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
                await send_keyboard(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await send_keyboard(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id

    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='PL Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    brand_id = xz_brands_ids[brand]
    page_replace = url_5.replace('{}', '1')
    if size != 'All':
        size_id = xz_size_ids[size]
        replaced = page_replace.replace('promoted', f'promoted/{size_id}-{brand_id}')
    else:
        replaced = page_replace.replace('promoted', f'promoted/{brand_id}')
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('ul', class_='pages')
    if pages is not None:
        totalpages = list(pages)[-2].text
    else:
        totalpages = 1

    for i in range(0, int(totalpages) + 1):
        ready_url = replaced.replace('/1/', '/{}/')
        url = ready_url.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='product')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', class_='image')
                        for link in links:
                            href = link['href'].replace('/', 'https://.../')

                        titles = el.find_all('h2', attrs={'id': True})
                        for title in titles:
                            title.text

                        sale_price = el.find_all('span', class_='price promotion')
                        for salepr in sale_price:
                            salepr.text

                        orig_price = el.find_all('span', class_='price old')
                        for origpr in orig_price:
                            origpr.text

                        images = el.find_all('img', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {salepr.text} \nOld price - {origpr.text} \nLink: {href}'
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
                await send_keyboard(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await send_keyboard(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    from all_search import all_search_brand
    user_id = call.message.chat.id

    keyboard = InlineKeyboardBuilder()
    stop_btn = keyboard.button(text='Stop', callback_data='PL Stop')
    # keyboard.add(stop_btn)
    keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False
    clean_brand = ''
    if brand == 'C.P. Company':
        clean_brand = 'cp-company'
    elif brand == 'Stüssy':
        clean_brand = 'stussy'
    else:
        clean_brand = brand.replace(' ', '-')
    page_replace = url_6.replace('{}', '1')
    url = page_replace.replace('meska', f'meska/{clean_brand}')
    clear_size = size.replace('.', '-')
    clear_size = clear_size.replace(' ', '+').lower()
    if size != 'All':
        replaced = url.replace(f'{clean_brand}', f'{clean_brand}__{clear_size}')
    else:
        replaced = url
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('li', class_='c-listing-pagination__element')
    totalpages = list(pages)[-1].text

    for i in range(0, int(totalpages) + 1):
        ready_url = replaced.replace('=1', '={}')
        url = ready_url.format(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='p-listing-products__item')

        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        links = el.find_all('a', class_='c-product-card__image-link')
                        for link in links:
                            href = link['href'].replace('/', 'https://.../')

                        titles = el.find_all('span', class_='c-product-card__title-link')
                        for title in titles:
                            title.text

                        sale_price = el.find_all('span', class_='c-product-card__price c-product-card__price--current')
                        for salepr in sale_price:
                            clean_salepr = ' '.join(salepr.text.split())

                        orig_price = el.find_all('span', class_='c-product-card__price c-product-card__price--before')
                        for origpr in orig_price:
                            clean_origpr = ' '.join(origpr.text.split())

                        images = el.find_all('img', class_='c-product-card__image', attrs={'src': True})
                        caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink: {href}'
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
                await send_keyboard(call, i, user_id, sent.message_id)
            break
    else:
        if not all_search_brand:
            i = 2
            await send_keyboard(call, i, user_id, sent.message_id)


def poland_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def poland_parse_callbacks_handler(call):
    if call.data == 'PL Stop':
        poland_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass

all_poland_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products
}

size_poland_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products
}
nonsize_poland_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products
}