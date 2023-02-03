import discord
import os
import random
from pyowm import OWM
from pyowm.utils.config import get_default_config
import webbrowser as wb
import cool_functions as f

language = get_default_config()
language["language"] = 'ru'
owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410',language)
manager = owm.weather_manager()

hi = ['привет','hello','hey','hi', ]   #greetings



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        global msg
        msg = message.content.lower()
      
        if msg == 'help':
            await message.channel.send(
                'Мои команды:\nПогода: weather[место]\nРешение примеров: math[пример]\n\Прикольный факт: funfact\nПоиск в интернете:search[запрос]\nИ генерация паролей: Password[кол-во символов]')
        if 'funfact' in msg:
            await message.channel.send(f.funfact())
        find_hi_words = False
        for item in hi:  # hello check
            if msg.find(item) >= 0:
                find_hi_words = True
        if 'math' in msg:
            await message.channel.send(f.math(msg))

        if find_hi_words:  # hello
            await message.channel.send(
                f'Привет {message.author.mention}! Я искуственный интелект. Я еще не совершенный поэтому вы не сможете писать мне что хотите. Чтобы узнать что я могу пропишите команду help.')

        if 'search' in msg:
            q = msg.replace('search','')
            wb.open('https://www.google.com/search?q='+q,new=2)
        if 'weather' in msg:
            
            
        if 'password' in msg:
          await message.channel.send(f.password(msg))



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA2NDg0MDEzMTI3NTY2NTQwOA.GULdOd.eGKNtXjCAWtkQ_IdjtqdcZ8uyjlZU7bX_-G9Is')