#!/usr/bin/python3
import requests
from datetime import datetime
from aiocryptogram.color import FG, BG

__version__ = '0.1.1'


def send_request(request_type: str, api_method: str, headers: dict, data: dict=None, testnet: bool=False) -> str:
	"""Посылаем запрос на CryptoBot API

	Аргументы:
	 request_type: str - тип запроса (get или post)
	 api_method: str - метод API
	 headers: dict - заголовок запроса
	 testnet: bool - используется тестнет или меиннет
	 data: dict=None - данные (при post запросах)"""

	if testnet:
		url = 'https://testnet-pay.crypt.bot/api'
	else:
		url = 'https://pay.crypt.bot/api/'

	if request_type.upper() == 'GET':
		data = requests.get(f'{url}{api_method}', headers=headers).json()
	elif request_type.upper() == 'POST':
		data = requests.post(f'{url}{api_method}', headers=headers, json=data).json()
	else:
		data = {'ok': False, 'error': {'code': 400, 'name': 'Неизвестный тип запроса'}}

	return data


class CryptoPayBot:
	"""Класс криптобота"""
	def __init__(self, name: str, api_token: str, testnet: bool=False, debug: bool=True) -> None:
		self.name = name
		self.API_TOKEN = api_token
		self.debug = debug
		self.testnet = testnet
		self.headers = {'Content-Type': 'application/json', 'Crypto-Pay-API-Token': self.API_TOKEN} 

		self.log(f'CryptoBotAPI Python library {__version__} (BETA)', 8)

	def log(self, text: str, log_type: int) -> str:
		"""Логирование собщений"""
		if log_type == 0:
			dbg_message = f"{FG.GREEN}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 1:
			dbg_message = f"{FG.YELLOW}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 2:
			dbg_message = f"{FG.RED}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 4:
			dbg_message = f"{FG.BLUE}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 5:
			dbg_message = f"{BG.GREEN}{FG.BLACK}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 6:
			dbg_message = f"{BG.YELLOW}{FG.BLACK}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 7:
			dbg_message = f"{BG.RED}{FG.BLACK}[{datetime.now()}]{FG.END} {text}"
		elif log_type == 8:
			dbg_message = f"{BG.BLUE}{FG.BLACK}[{datetime.now()}]{FG.END} {text}"

		if self.debug: print(dbg_message)

		return dbg_message

	def get_me(self) -> list:
		"""Получение информации об приложении. Используется для проверки работы приложения

		Возвращает список: логическое значение (правильно ли работает приложение) и сообщение"""
		try:
			data = send_request('get', 'getMe', self.headers, self.testnet)
		except requests.exceptions.ConnectionError as ex:
			msg = f'Проверьте подключения к серверу ({ex})'
			self.log(msg, 2)
			data = {'ok': False, "error": {'code': 400, "name": "Ошибка подключения к серверу"}}
		else:
			if data['ok']:
				msg = f'Аутенфикация прошла успешно. ID приложения: {data["result"]["app_id"]}'
				self.log(msg, 0)
			else:
				msg = f'Произошла ошибка {data["error"]["code"]}: {data["error"]["name"]}'
				self.log(msg, 2)

		return [data['ok'], msg]

	def create_invoice(self, currency_type: str, amount: float, description: str=None, hidden_message: str=None, 
					accepted_assets: list=["USDT", "TON", "BTC", "ETH", "LTC", "BNB", "TRX", "USDC"], asset: str=None, 
					fiat: str=None, paid_btn_name: str=None, paid_btn_url: str=None, allow_comments: bool=None, 
					allow_anonymous: bool=False, expires_in: int=None) -> list:
		"""Создание инвойса. Инвойс - это чек об оплате, то есть приложение принимает оплату.

		Аргументы:
		 + currency_type: str - тип валюты (crypto или fiat)
		 + amount: float - сумма
		 + description: str=None - описание
		 + hidden_message: str=None - скрытое сообщение
		 + accepted_assets: list=["USDT", "TON", "BTC", "ETH", "LTC", "BNB", "TRX", "USDC"] - принимаемые значения криптовалюты (при currency_type == crypto)
		 + asset: str=None - криптовалюта (при currency_type == crypto)
		 + fiat: str=None - валюта (при currency_type == fiat)
		 + paid_btn_name: str=None - название кнопки оплаты ('viewItem', 'openChannel', 'openBot', 'callback')
		 + paid_btn_url: str=None - ссылка (paid_btn_name)
		 + allow_comments: bool=None - разрешить комментарии (True, False)
		 + allow_anonymous: bool=False - анонимная оплата (True, False)
		 + expires_in: int=None - через сколько секунд инвойс станет недействительным

		Возвращает: список; логическая переменная и сообщение

		Подробнее об методе: https://help.crypt.bot/crypto-pay-api#createInvoice
		"""
		if currency_type == "crypto":
			if asset in accepted_assets:
				invoice_headers = {
					'currency_type': currency_type,
					'asset': asset,
					'amount': str(amount)
				}
		elif currency_type == "fiat":
			if fiat in ["USD", "EUR", "RUB", "BYN", "UAH", "GBP", "CNY", "KZT", "UZS", "GEL", "TRY", "AMD", "THB", "INR", "BRL", "IDR", "AZN", "AED", "PLN", "ILS"]:
				invoice_headers = {
					'currency_type': currency_type,
					'fiat': fiat,
					'amount': str(amount)
				}
		else:
			return False

		if description:
			invoice_headers['description'] = description
		if hidden_message and len(hidden_message) < 2048:
			invoice_headers['hidden_message'] = hidden_message
		if paid_btn_name in ['viewItem', 'openChannel', 'openBot', 'callback']:
			if paid_btn_url and paid_btn_url.startswith('http'):
				invoice_headers['paid_btn_name'] = paid_btn_name
				invoice_headers['paid_btn_url'] = paid_btn_url
		if allow_comments:
			invoice_headers['allow_comments'] = allow_comments
		if allow_anonymous:
			invoice_headers['allow_anonymous'] = allow_anonymous
		if expires_in:
			invoice_headers['expires_in'] = expires_in

		data = send_request('post', 'createInvoice', self.headers, invoice_headers, self.testnet)

		if data['ok']:
			msg = f'Инвойс {data["result"]["invoice_id"]} успешно создан. Ссылка на оплату: {data["result"]["pay_url"]}'
			self.log(msg, 0)
		else:
			msg = f'Ошибка создания чека {data["error"]["code"]}: {data["error"]["name"]}'
			self.log(msg, 1)

		return [data['ok'], msg]

	def create_check(self, cryptocurrency: str, amount: float) -> list:
		"""Создание чека.

		Аргументы:
		 + cryptocurrency: str - криптовалюта. Поддерживаемые: USDT, TON, BTC, ETH, LTC, BNB, TRX, USDC (и JET в TestNet)
		 + amount: float - сумма чека
		Возвращает:
		+ str - данные"""
		cryptocurrency = cryptocurrency.upper()

		if cryptocurrency in ["USDT", "TON", "BTC", "ETH", "LTC", "BNB", "TRX", "USDC"] or \
				(cryptocurrency in ["USDT", "TON", "BTC", "ETH", "LTC", "BNB", "TRX", "USDC", "JET"] and self.testnet):
			check_headers = {
				'asset': cryptocurrency.upper(),
				'amount': str(amount)
			}

			data = send_request('post', 'createCheck', self.headers, check_headers, self.testnet)

			if data['ok']:
				msg = f'Успешно создан чек: {data["check"]["check_id"]}'
				self.log(msg, 0)
			else:
				msg = f'Ошибка создания чека {data["error"]["code"]}: {data["error"]["name"]}'
				self.log(msg, 2)
		else:
			data = 'Неверная криптовалюта. Поддерживаемые: USDT, TON, BTC, ETH, LTC, BNB, TRX, USDC (и JET в TestNet)'

		return [data['ok'], msg]
