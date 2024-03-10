# aiocryptogram
Молниеносно быстрая библиотека для работы с [CryptoPay API](https://help.crypt.bot/crypto-pay-api).

## Установка и настройка
Следуйте инструкциям для использования библиотеки aiocryptogram

### Установка
Склонируйте репозиторий, создайте виртуальное окружение и установите зависимости

```bash
git clone https://github.com/alexeev-engineer/aiocryptogram.git
cd cryptobot-api
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Настройка
Перед началом работы вы должны отредактировать файл config.ini, вставив туда имя приложения и его API TOKEN.

### Запуск
Для запуска файла-примера:

```bash
python3 main.py
```

Для импорта откройте ваш код и отредактируйте его примерно так (если вы не используйте config.ini):

```python
from aiocryptogram.cryptopay import CryptoPayApp

NAME = "ИМЯ ПРИЛОЖЕНИЯ"
TOKEN = "ТОКЕН ПРИЛОЖЕНИЯ"

# Создаем бота в меиннете
bot = CryptoPayApp(name=NAME, api_token=TOKEN, testnet=False, debug=True) # параметр debug позволяет сразу выводить сообщения
info = bot.get_me() # проверяем работу приложения

... # ваш код
```

## Функции
В библиотеке уже реализованы методы:

 + getMe
 + createCheck
 + createInvoice

## Документация
Вы можете найти документацию по данному проекту по [этой ссылке](./docs/index.md)

## TODO

 + Добавить больше методов
 + Улучшить логгирование
 + Провести оптимизацию

