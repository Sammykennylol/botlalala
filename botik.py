# Настройка webhook для чат-бота
# Научимс создавать локальный сервер для бота
# И посмотрим как можно загружать бота на удаленный хостинг

import logging   #  для вывода разных событий в консоль

from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage

# настройка переменных
API_TOKEN = '6103615654:AAE_8xFXR_Eq-YdK_3byIi10PqRLCoahdEA'


logging.basicConfig(level=logging.INFO) # настраиваем вывод сообщений в консоль
bot = Bot(token=API_TOKEN) # создаем бота
dp = Dispatcher(bot) # для обработки входящих сообщений боту


@dp.message_handler(commands=['start'])  # /start
async def start(message: types.Message):
    return SendMessage(message.chat.id, "Добро пожаловать в лучшего бота!")

@dp.message_handler(commands=['help'])  # /help
async def help(message: types.Message):
    return SendMessage(message.chat.id, "Наш бот ничего пока не умеет, поэтому мне тебе нечем помочь(((")

@dp.message_handler(content_types=['text'])  # текст
async def echo2(message: types.Message):
    if message.text == "Привет":
        return SendMessage(message.chat.id, "И тебе привет, друг!")
    elif message.text == "Пока":
        return SendMessage(message.chat.id, "До свидания, приходи еще!")
    else:
        return SendMessage(message.chat.id, message.text)

executor.start_polling(dp,skip_updates=True)


# 1) Поставьте плюсик в чат, если вставили токен и адрес, проверили, бот работает
# 2) Напишите простого чат-бота, который проверяет через ифы сообщения по типу "привет", "пока", "как дела" и тд и тп

