import telebot
from bs4 import BeautifulSoup
import requests
import time
from telebot import types
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest
import re
import os

from request_choose import country_request
from all_data import (
    all_stores, all_sizes, ready_to_sizefilter_all,
    xzxz_brands_ids, xzxz_brands_ids,
    xzxz_brands_ids, xzxz_brands_ids,
    xzxz_brands_ids
)

tok = os.getenv('tok')
bot = Bot(token=tok)
dp = Dispatcher()

async def size_choosing(call, country, site, brand):
    user_id = call.message.chat.id
    msg = call.message.message_id
    keyboard = InlineKeyboardBuilder()
    buttons = []
    back_to_brands = types.InlineKeyboardButton(text='Back to brands', callback_data='Back to brands')
    all_btn = types.InlineKeyboardButton(text='All', callback_data='All')

    if site == '...':
        if brand == "Levi's":
            clear_brand = 'Levi%27s'
        else:
            clear_brand = brand.replace(' ', '+')
        site_to_response = ready_to_sizefilter_all[site]
        replaced = site_to_response.replace('sale/?', f'sale/?brand={clear_brand}&')
        
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('li', class_='option___fA7Hp button___bmFnB', attrs={'title': 'Sizes'})
        for el in sizes:
            keyboard.button(text=f'{el.text}', callback_data=el.text)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(back_to_brands)
        # back_to_brands = keyboard.button(text='Back to brands', callback_data='Back to brands')
        # all_btn = keyboard.button(text='All', callback_data='All')
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(f'brand - {brand}', user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('sale?', f'sale?filter.p.vendor={clear_brand}&')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('ul', class_='facets__list list-unstyled')
        sizelist = list(sizes[1])
        for el in sizelist:
            clear_txt = ' '.join(el.text.split())
            button = types.InlineKeyboardButton(text=clear_txt, callback_data=clear_txt)
            buttons.append(button)
        filtered_buttons = [button for button in buttons if button.text.strip()]
        keyboard.add(*filtered_buttons)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        if brand != 'asics':
            clear_brand = brand.replace(' ', '%20').upper()
        replaced = site_to_response.format(clear_brand)
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find('ul', class_='sizes2')
        item = sizes.find_all('li')
        for el in item:
            clear_txt = ' '.join(el.text.split())
            button = keyboard.button(text=clear_txt, callback_data=clear_txt)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '_').lower()
        replaced = site_to_response.replace('sale', f'sale/{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('div', class_='swatch-option text')
        if sizes:
            for el in sizes:
                clear_txt = ' '.join(el.text.split())
                button = keyboard.button(text=clear_txt, callback_data=clear_txt)
                # buttons.append(button)
            # keyboard.add(*buttons)
            # keyboard.add(all_btn)
            # keyboard.add(back_to_brands)
            keyboard.adjust(2)
            keyboard.row(all_btn)
            keyboard.row(back_to_brands)
            await bot.edit_message_text(brand, user_id, msg)
            await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.upper()
        replaced = site_to_response.replace('sale?', f'sale?filter.p.vendor={clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('div', class_='filter-group')
        to_remove = soup.find_all('span', class_='filter-group__item__count')
        if to_remove:
            for tag in to_remove:
                tag.extract()

        btn = sizes[5].find_all('span', class_='filter-group__item__text')
        for el in btn:
            clear_txt = ' '.join(el.text.split())
            button = keyboard.button(text=clear_txt, callback_data=clear_txt)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '-')
        replaced = site_to_response.replace('/wy', f'/{clear_brand}/wy')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('div', class_='filters-fieldset-wrapper')
        checkbox = sizes[2].find_all('input', attrs={'type': 'checkbox'})
        for el in checkbox:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        brandid = xzxz_brands_ids[brand]
        replaced = site_to_response.replace('promoted', f'promoted/{brandid}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        body = soup.find('select', attrs={'id': 'fl_rozmiar'})
        sizes = body.find_all('option', attrs={'data-url': True})
        for el in sizes:
            button = keyboard.button(text=el.text, callback_data=el.text)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = ''
        if brand == 'C.P. Company':
            clear_brand = 'cp-company'
        elif brand == 'Stüssy':
            clear_brand = 'stussy'
        else:
            clear_brand = brand.replace(' ', '-')
        replaced = site_to_response.replace('meska', f'meska/{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('div', class_='c-dropdown__content')
        item = sizes[3].find_all('a', class_='c-dropdown__list-item')
        for el in item:
            clear_txt = ' '.join(el.text.split())
            button = keyboard.button(text=clear_txt, callback_data=clear_txt)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+').upper()
        replaced = site_to_response.replace('sales?', f'sales?filter.p.vendor={clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('ul', class_='mobile-facets__list list-unstyled')
        items = sizes[2].find_all('label', class_='mobile-facets__label')
        for el in items:
            if len(el['class']) == 1:
                values = el.find_all('input', class_='mobile-facets__checkbox')
                for value in values:
                    size = value.get('value')
                    button = keyboard.button(text=size, callback_data=size)
                    # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        if brand == "Levi's":
            clear_brand = 'LEVI%27S®'
        elif brand == 'Lyle & Scott':
            clear_brand = 'LYLE+%26+SCOTT'
        else:
            upper_brand = brand.upper()
            clear_brand = upper_brand.replace(' ', '+')

        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'disabled': False, 'name': 'filter.v.option.taglia'})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
            # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('outlet?', f'outlet?filter.p.vendor={clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.taglia', 'disabled': False})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'disabled': False, 'name': 'filter.v.option.size'})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+').lower()
        replaced = site_to_response.replace('rebajas', f'rebajas/b/{clear_brand}/')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'size'})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '-').upper()
        replaced = site_to_response.replace('sneakers', f'sneakers/es_vender_{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('div', class_='consuela-filter')
        for el in sizes:
            script = el.find_all('script')
            for scr in script:
                if scr is not None:
                    string = scr.string.strip().split('\n')[0]
                    json_match = re.search(r'JSON\.parse\(.*?\)', string)
                    if json_match:
                        json_array = json_match.group(0)[11:-1]
                        allsizes = re.findall(r'"(.*?)"', json_array)
                        for el in allsizes:
                            button = keyboard.button(text=el, callback_data=el)
        #                     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('a', class_='feds_link')
        for el in sizes:
            href = el.get('href')
            if 'Tallas' in href:
                span = el.find_all('span')
                for sp in span:
                    sp.extract()
                    button = keyboard.button(text=el.text, callback_data=el.text)
        #             buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...': # ?????????
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '_').lower()
        brandid = xzxz_brands_ids[brand]
        replaced = site_to_response.replace('rebajados', f'rebajados/marca_2-{clear_brand}')
        replaced = replaced.replace('brid', f'{brandid}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find('select', attrs={'data-placeholder': 'Elige'})
        option = sizes.find_all('option')
        for el in option:
            button = keyboard.button(text=el.text, callback_data=el.text)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        if brand == "Levi's":
            clear_brand = 'Levi%27s'
        else:
            clear_brand = brand.replace(' ', '+')

        replaced = site_to_response.replace('sale?', f'sale?filter.p.vendor={clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('label', class_='facet-checkbox')
        seen_values = set()
        for el in sizes:
            inputs = el.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
            for item in inputs:
                value = item.get('value')
                if value not in seen_values:
                    seen_values.add(value)
                    button = keyboard.button(text=value, callback_data=value)
        #             buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
        seen_values = set()
        for el in sizes:
            value = el.get('value')
            if value not in seen_values:
                seen_values.add(value)
                button = keyboard.button(text=value, callback_data=value)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '-').lower()
        replaced = site_to_response.replace('sale', f'sale/{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('a', attrs={'title': True})
        for el in sizes:
            title = el.get('title')
            if 'size' in title:
                clear_txt = ' '.join(el.text.split())
                button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        if brand == "Levi's":
            clear_brand = 'levis'
        else:
            clear_brand = brand.replace(' ', '-').lower()

        replaced = site_to_response.replace('name', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('li', attrs={'data-value': True})
        for el in sizes:
            value = el.get('data-value')
            if 'size' in value:
                button = keyboard.button(text=el.text, callback_data=el.text)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
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

        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('a', attrs={'title': True})
        for el in sizes[:-1]:
            href = el.get('href')
            if 'size' in href:
                clear_txt = ' '.join(el.text.split())
                button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        brandid = xzxz_brands_ids[brand]
        replaced = site_to_response.replace('brid', f'{brandid}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('a', attrs={'href': True})
        for el in sizes:
            href = el.get('href')
            if 'size' in href:
                span = el.find('span')
                if span:
                    span.extract()
                    clear_txt = ' '.join(el.text.split())
                    button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #             buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        replaced = site_to_response.replace('brand', f'{brand.lower()}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('a', attrs={'title': True})
        seen_values = set()
        for el in sizes:
            href = el.get('href')
            if 'size' in href:
                clear_txt = ' '.join(el.text.split())
                if clear_txt not in seen_values:
                    seen_values.add(clear_txt)
                    button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #             buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        replaced = site_to_response.replace('brand', f'{brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        brandid = xzxz_brands_ids[brand]
        replaced = site_to_response.replace('brandid', f'{brandid}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('a')
        for el in sizes:
            href = el.get('href')
            if 'size' in href:
                clear_txt = ' '.join(el.text.split())
                button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
        seen_values = set()
        for el in sizes:
            value = el.get('value')
            if value not in seen_values:
                seen_values.add(value)
                button = keyboard.button(text=value, callback_data=value)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        brandid = xzxz_brands_ids[brand]
        replaced = site_to_response.replace('brandid', f'{brandid}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('ul', class_='filter__properties filter__properties--size')
        for elm in sizes:
            li = elm.find_all('li')
            for el in li:
                clear_txt = ' '.join(el.text.split())
                button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
        seen_values = set()
        for el in sizes:
            value = el.get('value')
            if value not in seen_values:
                seen_values.add(value)
                button = keyboard.button(text=value, callback_data=value)
        #         buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '+')
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('input', attrs={'name': 'filter.v.option.size', 'disabled': False})
        for el in sizes:
            value = el.get('value')
            button = keyboard.button(text=value, callback_data=value)
        #     buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '-').lower()
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('ul', class_='filter-group_options filter-boxes sizeFilters')
        for el in sizes:
            a = el.find_all('a')
            for link in a:
                href = link.get('href')
                if 'Size' in href:
                    clear_txt = ' '.join(link.text.split())
                    button = keyboard.button(text=clear_txt, callback_data=clear_txt)
        #             buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

    if site == '...':
        site_to_response = ready_to_sizefilter_all[site]
        clear_brand = brand.replace(' ', '_').lower()
        replaced = site_to_response.replace('brand', f'{clear_brand}')
        response = requests.get(replaced)
        soup = BeautifulSoup(response.text, 'lxml')
        sizes = soup.find_all('div', class_='PM_ASCriterionsOutput')
        for el in sizes:
            if 'Pointure' in el.text:
                link = el.find_all('a', class_='PM_ASLabelLink')
                for item in link:
                    div = item.find('div')
                    div.extract()
                    clear_txt = ' '.join(item.text.split())
                    button = keyboard.button(text=clear_txt, callback_data=clear_txt)
                    # buttons.append(button)
            if 'Taille' in el.text:
                link = el.find_all('a', class_='PM_ASLabelLink')
                for item in link:
                    div = item.find('div')
                    div.extract()
                    clear_txt = ' '.join(item.text.split())
                    button = keyboard.button(text=clear_txt, callback_data=clear_txt)
                    # buttons.append(button)
        # keyboard.add(*buttons)
        # keyboard.add(all_btn)
        # keyboard.add(back_to_brands)
        keyboard.adjust(2)
        keyboard.row(all_btn)
        keyboard.row(back_to_brands)
        await bot.edit_message_text(brand, user_id, msg)
        await bot.edit_message_reply_markup(user_id, msg, reply_markup=keyboard.as_markup())

### need to add array with all sizes  04.08 - added
### BUG with one-letter sizes (M, L, S etc.)  04.08 16:02 - fixed

@dp.callback_query(lambda call: True)
async def size_callbacks_handler(call):
    msg = call.message.chat.id
    from brand_choose import chosen_brand
    from country_choose import countrytest
    from site_choose import callbacks, callbacks2
    if chosen_brand and callbacks:
        if call.data in all_sizes:
            if callbacks:
                await bot.edit_message_reply_markup(msg, call.message.message_id, reply_markup=None)
                time.sleep(0.5)
                await country_request(call, countrytest[msg], callbacks[msg], chosen_brand[msg], call.data)
                chosen_brand.clear()
                callbacks.clear()
                # countrytest.clear()
    if call.data == 'Back to brands':
        from brand_choose import brands_choose
        brand_markup = await brands_choose(call, callbacks2[msg])
        try:
            await bot.send_message(msg, text='', reply_markup=brand_markup)
        except TelegramBadRequest:
            pass
    try:
        await bot.answer_callback_query(call.id)
    except TelegramBadRequest:
        pass