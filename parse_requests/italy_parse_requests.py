from bs4 import BeautifulSoup
import requests
from telebot import types
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import time
import os

from all_data import (
    xz_brands, xz_brands,xz_brands, xz_brands,
   xz_brands_ids, xz_brands, xz_brands, xz_brands
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
url_9 = '...'


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

async def xz_products(call, brand, size=None): # ??? not enough time to make request
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='IT Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    if brand == "Levi's":
        clear_brand = 'levis'
    elif brand == 'Lyle & scott':
        clear_brand = 'lyle-scott'
    else:
        clear_brand = brand.replace(' ', '-')
    
    replaced = url_1.replace('/?', f'/?berocket_brand={clear_brand}')

    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find_all('a', class_='page-numbers')
    if pages:
        totalpages = pages[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        url = replaced.replace('1', '{}').format(i)
        response = requests.get(url)
        print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='product type-product')
        
        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand in el.text:
                    if brand in xz_brands:
                        pass

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='IT Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '+')

    url = url_2.replace('brand', f'{clear_brand}')
    if size != 'All':
        replaced = url.replace(f'{clear_brand}', f'{clear_brand}&filter.v.option.size={size}')
    else:
        replaced = url
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('li', class_='grid__item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price-item price-item--sale price-item--last')
                    for price in sale_price:
                        clean_salepr = ' '.join(price.text.split())
                    orig_price = el.find_all('s', class_='price-item price-item--regular')
                    for price2 in orig_price:
                        clean_origpr = ' '.join(price2.text.split())
                    product_title = el.find_all('h3', class_='card__heading h5')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='full-unstyled-link')
                    for link in links:
                        link_txt = link['href'].replace('/products', 'https://.../products')
                    images = el.find_all('img', class_='motion-reduce', attrs={'srcset': True})
                    caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink - {link_txt}'
                    for image in images:
                        image_url = image['srcset'].split(',')[1]
                        replace = image_url.replace('//', 'https://')
                        image_response = requests.get(replace)
                        image_data = image_response.content
                        await bot.send_photo(call.message.chat.id, photo=replace, caption=caption)
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
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='IT Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    if brand == "Levi's":
        clear_brand = 'LEVI%27S®'
    elif brand == 'Lyle & Scott':
        clear_brand = 'LYLE+%26+SCOTT'
    else:
        upper_brand = brand.upper()
        clear_brand = upper_brand.replace(' ', '+')

    clear_size = size.replace('/', '%2F')
    clear_size = clear_size.replace(' ', '+')
    url = url_3.replace('brand', f'{clear_brand}')
    if size != 'All':
        replaced = url.replace(f'{clear_brand}', f'&filter.v.option.taglia={clear_size}')
    else:
        replaced = url
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='sf__col-item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='f-price-item--sale')
                    for price in sale_price:
                        clean_salepr = ' '.join(price.text.split())
                    orig_price = el.find_all('s', class_='f-price-item--regular')
                    for price2 in orig_price:
                        clean_origpr = ' '.join(price2.text.split())
                    product_title = el.find_all('a', class_='sf__pcard-name')
                    for title in product_title:
                        pass
                    
                    links = el.find_all('a', class_='sf__pcard-name')
                    for link in links:
                        link_txt = link['href'].replace('/products', 'https://.../products')
                    images = el.find_all('img', attrs={'srcset': True})
                    caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink - {link_txt}'
                    i = 0
                    for image in images:
                        i += 1
                        if i % 2 != 0:
                            image_url = image['srcset'].split(',')[1]
                            replace = image_url.replace('//', 'https://')
                            image_response = requests.get(replace)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=replace, caption=caption)
        else:
            i = 2
            await end_of_function(call, i, user_id, sent.message_id)
            break
    else:
        i = 2
        await end_of_function(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # ??? img problem
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = types.InlineKeyboardMarkup()
    stop_btn = types.InlineKeyboardButton('Stop', callback_data='IT Stop')
    stop_keyboard.add(stop_btn)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard)
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    brand_id = xz_brands_ids[brand]

    brand_replace = url_4.replace('brand', f'{brand_id}')

    response = requests.get(brand_replace)
    soup = BeautifulSoup(response.text, 'lxml')
    ul = soup.find('ul', class_='pagination')
    if ul is not None:
        pages = soup.find_all('a', class_='page-link')
        totalpages = pages[-2].text
    else:
        totalpages = 1

    for i in range(1, int(totalpages) + 1):
        response = requests.get(brand_replace)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('div', class_='col-sm-6 col-md-6 col-lg-4 col-6')
        if not user_id in stoplist:
            i += 1
            for el in div:
                if brand.upper() in el.text:
                    if brand in xz_brands:

                        sale_price = el.find_all('span', class_='discount-price')
                        for price in sale_price:
                            clean_salepr = ' '.join(price.text.split())

                        orig_price = el.find_all('span', class_='before-discount-price')
                        for price2 in orig_price:
                            clean_origpr = ' '.join(price2.text.split())

                        product_title = el.find_all('div', class_='brand-category text-center mb-5')
                        for title in product_title:
                            name = title.find_all('p')
                            for nametitle in name:
                                pass
                        
                        links = el.find_all('a', attrs={'alt': True})
                        for link in links:
                            link_txt = link['href'].replace('/uomo', 'https://.../uomo')
                        images = el.find_all('img')
                        caption = f'{nametitle.text.lower()} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink - {link_txt}'
                        for image in images:
                            print(image) # ???
                            # image_url = image['src']
                            # replace = image_url.replace('/public', 'https://.../public')
                            # image_response = requests.get(replace)
                            # image_data = image_response.content
                            # await bot.send_photo(call.message.chat.id, photo=image_data, caption=caption)
                else:
                    i = 2
                    await end_of_function(call, i, user_id, sent.message_id)
                    break
    else:
        i = 2
        await end_of_function(call, i, user_id, sent.message_id)

async def xz_products(call, brand, size=None): # not all products but working
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = types.InlineKeyboardMarkup()
    stop_btn = types.InlineKeyboardButton('Stop', callback_data='IT Stop')
    stop_keyboard.add(stop_btn)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard)
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    url = url_5.format(brand)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('div', class_='productitem')

    rdybrand = brand
    if brand == 'Adidas':
        rdybrand = 'adidas'

    for el in div:
        if not user_id in stoplist:
            if rdybrand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='money price__current--min')
                    for price in sale_price:
                        clean_salepr = ' '.join(price.text.split())

                    orig_price = el.find_all('span', class_='money price__compare-at--single')
                    for price2 in orig_price:
                        clean_origpr = ' '.join(price2.text.split())

                    product_title = el.find_all('h2', class_='productitem--title')
                    for title in product_title:
                        title.text
                    
                    links = el.find_all('a', attrs={'data-product-page-link': True})
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('img', class_='productitem--image-primary')
                    caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink - {link_txt}'
                    i = 0
                    for image in images:
                        i += 1
                        if i % 2 != 0:
                            image_url = image['src'].replace('//', 'https://')
                            image_response = requests.get(image_url)
                            image_data = image_response.content
                            await bot.send_photo(call.message.chat.id, photo=image_data, caption=caption)
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
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='IT Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)

    clear_brand = brand.replace(' ', '+')
    clear_size = size.replace(' ', '+')
    url = url_6.replace('brand', f'{clear_brand}')
    if size != 'All':
        replaced = url.replace(f'{clear_brand}', f'{clear_brand}&filter.v.option.taglia={clear_size}')
    else:
        replaced = url
    response = requests.get(replaced)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find_all('li', class_='grid__item')

    for el in div:
        if not user_id in stoplist:
            if brand in el.text:
                if brand in xz_brands:
                    sale_price = el.find_all('span', class_='price-item price-item--sale')
                    for price in sale_price:
                        clean_salepr = ' '.join(price.text.split())

                    orig_price = el.find_all('s', class_='price-item price-item--regular')
                    for price2 in orig_price:
                        clean_origpr = ' '.join(price2.text.split())

                    product_title = el.find_all('span', class_='visually-hidden')
                    for title in product_title:
                        title.text
                    
                    links = el.find_all('a', class_='full-unstyled-link')
                    for link in links:
                        link_txt = link['href'].replace('/collections', 'https://.../collections')
                    images = el.find_all('img', class_='motion-reduce')
                    caption = f'{title.text} \nSale price - {clean_salepr} \nOld price - {clean_origpr} \nLink - {link_txt}'
                    i = 0
                    for image in images:
                        i += 1
                        if i % 2 != 0:
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

async def xz_products(call, brand, size=None): # available to size filter
    stoplist.clear()
    from site_choose import callbacks
    user_id = call.message.chat.id;
    chosen_brand = brand
    await bot.send_message(user_id, f'brand - {chosen_brand}')

    stop_keyboard = InlineKeyboardBuilder()
    stop_btn = stop_keyboard.button(text='Stop', callback_data='IT Stop')
    # stop_keyboard.add(stop_btn)
    stop_keyboard.adjust(1)
    sent = await bot.send_message(user_id, 'Stop', reply_markup=stop_keyboard.as_markup())
    await bot.pin_chat_message(user_id, sent.message_id, disable_notification=True)
    flag = False

    clear_brand = brand.replace(' ', '+')
    clear_size = size.replace(' ', '+')
    url = url_7.replace('brand', f'{clear_brand}')
    if size != 'All':
        replaced = url.replace(f'{clear_brand}', f'{clear_brand}&filter.v.option.size={clear_size}')
    else:
        replaced = url

    for i in range(1, 6):
        rdyurl = replaced.format(i)
        response = requests.get(rdyurl)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find_all('li', class_='column')

        if not user_id in stoplist:
            for el in div:
                if brand in el.text and 'Save' in el.text:
                    if brand in xz_brands:
                        sale_price = el.find_all('span', class_='money')
                        i = 0
                        for price in sale_price:
                            i += 1
                            if i % 2 != 0:
                                origpr = price.text
                            else:
                                salepr = price.text

                        product_title = el.find_all('a', class_='product-card-title')
                        for title in product_title:
                            title.text
                        
                        links = el.find_all('a', class_='product-card-title')
                        for link in links:
                            link_txt = link['href'].replace('/collections', 'https://.../collections')
                        images = el.find_all('img', class_='product-primary-image')
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

def italy_pushstop(id, callback):
    stoplist[id] = callback

@dp.callback_query(lambda call: True)
async def italy_parse_callbacks_handler(call):
    if call.data == 'IT Stop':
        italy_pushstop(call.message.chat.id, 'Stop')
        print(stoplist)
        stopmsg = await bot.send_message(call.message.chat.id, 'Stop')
        time.sleep(2)
        await bot.delete_message(call.message.chat.id, stopmsg.message_id)

    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass


all_italy_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products,
    '...': xz_products
}

size_italy_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products, '...': xz_products
}

nonsize_italy_functions = {
    '...': xz_products, '...': xz_products,
    '...': xz_products
}