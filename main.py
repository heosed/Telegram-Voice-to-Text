# -*- coding: utf-8 -*-
import os

from telethon.tl import types
from telethon import TelegramClient, events
import speech_recognition as sr
import cryptg
import subprocess

import asyncio
import logging

#Логи
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')
#Данные клиента
entity = '' #имя сессии - все равно какое
API_ID =  #api-id приложения
API_HASH = ''#api-hash приложения

#Создание клиента
client = TelegramClient(entity, API_ID, API_HASH)
client.start()


#Переменная которая определяет расположение скрипта
root_dir = os.path.abspath(os.curdir)
#Вызов класса для распознавания речи
recognizer = sr.Recognizer()

#Хендлер ловли сообщений с клиента
#Что-бы поменять символ, на который будет реагировать бот, надо поменять '.v' в pattern=
@client.on(events.NewMessage(outgoing=True, pattern=r'\.v'))
async def handler(event):
    text = '⌛️Обработка голосового сообщения....'
    if event.is_reply:
        try:
            #Ловим сообщения на которые мы ответили, и записываем в переменные
            replied = await event.get_reply_message()
            msg = await event.edit(text)
            #Скачиваем файл
            await client.download_media(replied,f'{root_dir}\\audio.ogg')
            #Вызываем сопроцесс, который преобразует ogg в wav
            process = subprocess.call(['ffmpeg', '-i', f'{root_dir}\\audio.ogg', f'{root_dir}\\audio.wav'])
            #Удаляем лишний файл
            os.remove(f'{root_dir}\\audio.ogg',)
            #Конвертирум аудио в обьект класса
            audio_file = sr.AudioFile(f'{root_dir}\\audio.wav')
            #Преобразуем голосовое в текст
            with audio_file as source:
                audio_file = recognizer.record(source)
                """
                На самом деле, скрипт гугла не особо точный
                Лучше использовать recognize_wit(), но тогда надо будет надыбать API-KEY
                """
                result = recognizer.recognize_google(audio_data=audio_file, language = 'ru-RU').lower()
            await event.message.delete()
            #Отправляем результат
            await replied.reply(f'{result}')
            os.remove(f'{root_dir}\\audio.wav')
        except Exception:
            #На непредвиденные случаи
            await event.message.delete()
            await replied.reply(f'**Ничё не понятно**')
            os.remove(f'{root_dir}\\audio.wav')


with client:
    client.run_until_disconnected()