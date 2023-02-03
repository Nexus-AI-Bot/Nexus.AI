import discord
import os
import random
from pyowm import OWM
from pyowm.utils.config import get_default_config
import requests
import json
import webbrowser as wb


# variables:
funfactapi = "https://useless-facts.sameerkumar.website/api"

# __main__:

def funfact():
  api = requests.get(funfactapi)
  funfactgetdict = json.loads(api.content)
  return(funfactgetdict["data"])
#

language = get_default_config()
language["language"] = 'ru'
owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410',language)
manager = owm.weather_manager()

hi = ['привет','hello','hey','hi', ]   #greetings
password_simbols = ['@','#','$','&','*']
password_alpha = ['a','b','c','d','e','f','g','q','w','r','t','y','u','i','o','p','s','h','j','k','l','z','x','v','b','n','m']


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
            await message.channel.send(funfact())
        find_hi_words = False
        for item in hi:  # hello check
            if msg.find(item) >= 0:
                find_hi_words = True
        if 'math' in msg:
            math = msg.replace('math','')
            try:
                solution = eval(math)
                await message.channel.send(solution)
            except:
                await message.channel.send("Пример написан неправильно!")

        if find_hi_words:  # hello
            await message.channel.send(
                f'Привет {message.author.mention}! Я искуственный интелект. Я еще не совершенный поэтому вы не сможете писать мне что хотите. Чтобы узнать что я могу пропишите команду help.')

        if 'search' in msg:
            q = msg.replace('search','')
            wb.open('https://www.google.com/search?q='+q,new=2)
        if 'weather' in msg:
            city = msg.replace('weather', '')

            try:
                city = city.replace('[', '')
                city = city.replace(']', '')
                city = city.replace('in', '')
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
            if rain == {}:
                r = "Осадков нет"
            else:
                r = f"Идет дождь {rain.get('1h')} милиметров осадков"

            await message.channel.send(f"Сейчас на улице: {weather.detailed_status}\nОблачность: {weather.clouds}%\nТекущая температура: {temp}\nМаксимальная температура: {temp_max}\nМинимальная температура: {temp_min}\nОщущается как {feels_like}\n{r}\nСкорость ветра {weather.wind().get('speed')} м/с")
            
        if 'password' in msg:
            symbols = msg.replace('password','')
            try:
                if int(symbols)>10:
                    await message.channel.send('В пароле должно быть до 10 символов!')
                else:
                    password = []
                    for symbol in range(int(symbols)):
                        a = random.randint(1,3)
                        if a == 1:
                            password.append(random.choice(password_simbols))
                        elif a == 2:
                            b = random.randint(1,2)
                            alpha = random.choice(password_alpha)
                            if b == 1:
                                password.append(alpha)
                            else:
                                password.append(alpha.upper())
    
                        else:
                            password.append(random.randint(0,9))
                send = str(password).replace('[','')
                send = send.replace(']','')
                send = send.replace(',','')
                send = send.replace("'",'')
                send = send.replace(' ','')
                await message.channel.send( send)
            except:
               await message.channel.send('Неверно введено количество символов!')



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA2NDg0MDEzMTI3NTY2NTQwOA.GULdOd.eGKNtXjCAWtkQ_IdjtqdcZ8uyjlZU7bX_-G9Is')