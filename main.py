import discord
import os
import random
from pyowm import OWM
import smtplib
from email.mime.text import MIMEText
from pyowm.utils.config import get_default_config
import webbrowser as wb
import cool_functions as f

sender = "helper.ai@fluffik.co.uk"
password = "nxukvmybdpgymmjq"
language = get_default_config()
language["language"] = 'ru'
owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410',language)
manager = owm.weather_manager()

hi = ['привет','hello','hey','hi', ]  #greetings



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        author = message.author
        if message.author == self.user:
            return
        global msg
        msg = message.content.lower()
      
        if msg == '/help':
            await message.channel.send(
                'Мои команды:\nПогода: /weather[место]\nРешение примеров: /calculate[пример]\n\Прикольный факт: /funfact\nПоиск в интернете: /search[запрос]\nИ генерация паролей: /password[кол-во символов]')
        if '/funfact' in msg:
            await message.channel.send(f.funfact())
        find_hi_words = False
        for item in hi:  # hello check
            if msg.find(item) >= 0:
                find_hi_words = True
        if '/calculate' in msg:
            await message.channel.send(f.math(msg))

        if find_hi_words:  # hello
          await message.channel.send(f'Привет {message.author.mention}! Я искуственный интелект. Я еще не совершенный поэтому вы не сможете писать мне что хотите. Чтобы узнать что я могу пропишите команду help.')

        if '/search' in msg:
          q = msg.replace('search','')
          wb.open('https://www.google.com/search?q='+q,new=2)
        if '/weather' in msg:
          city = msg.replace('weather','')
                              
          try:
            city = city.replace('[','')
            city = city.replace(']','')
            city = city.replace('in','')
          except:
            pass
          try:
            observation = manager.weather_at_place(str(city))
          except:
            await message.channel.send('Город введен неверно.')
          weather = observation.weather
          temp = weather.temperature("celsius").get("temp")
          temp_max = weather.temperature("celsius").get("temp_max")
          temp_min = weather.temperature("celsius").get("temp_min")
          feels_like = weather.temperature("celsius").get("feels_like")
          rain = weather.rain
                    
          await message.channel.send(f"Сейчас на улице: {weather.detailed_status}")
          await message.channel.send(f"Облачность: {weather.clouds}%")
          await message.channel.send(f"Текущая температура: {temp}")
          await message.channel.send(f"Максимальная температура: {temp_max}")
          await message.channel.send(f"Минимальная температура: {temp_min}")
          await message.channel.send(f"Ощущается как {feels_like}")
          if rain == {}:
            await message.channel.send("осадков нет")
          else:
            await message.channel.send(f"идет дождь {rain.get('1h')} милиметров осадков")
          await message.channel.send(f"Скорость ветра {weather.wind().get('speed')} м/с")
              
        if '/password' in msg:
          await message.channel.send(f.password(msg))
        if '/email' in msg:
          mylist = msg.split(',')
          mylist.remove(mylist[0])
          subject = mylist[0]
          body = mylist[1]
          recipients = mylist[2]
          msg = MIMEText(body)
          msg['Subject'] = subject
          msg['From'] = sender
          msg['To'] = recipients
          smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
          smtp_server.login(sender, password)
          smtp_server.sendmail(sender, recipients, msg.as_string())
          smtp_server.quit()
          await message.channel.send('Email sent!')
        if "/mathproblem" in msg:
          await message.channel.send(f.math_ran())
        if "/todo" in msg:
          await message.channel.send(f.todo(msg, author))

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA2NDg0MDEzMTI3NTY2NTQwOA.G69t_3.bQ5Auegi6GTWu8s9S3mpcN5h0SX450jpSqREfs')



