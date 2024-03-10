#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""aiocryptogram - асинхронная библиотека для работы с Crypto Pay API
Разработчик: Alexeev Bronislav
Лицензия: GNU GPL v3"""
from rich import print
from aiocryptogram.cryptopay import CryptoPayBot
from configparser import ConfigParser
import asyncio

__version__ = '0.1.0'


async def main():
    print(f'aiocryptogram v {__version__}')
    print(f'Copyright (C) Alexeev Bronislav 2024 @ All rights reversed')
    
    # Читаем config.ini и парсим из него токен и имя
    config = ConfigParser()
    config.read('config.ini')
    NAME = config.get('CryptoBot', 'name')
    TOKEN = config.get('CryptoBot', 'token')
    
    # Создаем бота
    bot = CryptoPayBot(NAME, TOKEN, False)
    info = bot.get_me() # проверяем работу приложения
    
    if info[0]:
    	# Если приложение работает
    
    	# Создание инвойса
    	invoice = bot.create_invoice(currency_type='crypto', asset='USDT', amount=1.0)
    	# Создание чека
    	# check = bot.create_check("USDT", 100.0)
    else:
    	# Иначе выходим
    	exit()


if __name__ == "__main__":
    asyncio.run(main())
