import discord
import os
import random
from pyowm import OWM
from googletrans import Translator
import smtplib
from email.mime.text import MIMEText
from pyowm.utils.config import get_default_config
import cool_functions as f

aiquestionstate = True

sender = "helper.ai@fluffik.co.uk"
password = os.environ['PASSWORD']

hi = [
  'привет',
  'hello',
  'hey',
  'hi',
]  #greetings


class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    # don't respond to ourselves
    author = message.author
    if message.author == self.user:
      return
    global msg
    global aiquestionstate
    msg = message.content.lower()
    global ru
    global eng
    global manager
    global owm
    if '/setlanguage ru' in msg:
      global language
      language = get_default_config()
      language["language"] = 'ru'
      owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410', language)
      manager = owm.weather_manager()
      ru = True
      eng = False

    async def send(message):
      await message.channel.send(message)

    if '/setlanguage eng' in msg:
      owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410')
      manager = owm.weather_manager()
      eng = True
      ru = False
      if ru and msg in hi:
        await message.channel.send(
          f'Привет {message.author.mention}! Я искуственный интелект. Я еще не совершенный поэтому вы не сможете писать мне что хотите. Чтобы узнать что я могу пропишите команду help.'
        )
      if eng and msg in hi:
        await message.channel.send(
          f"Hello {message.author.mention}! I'm an artificial intelligence. I'm not perfect yet, so I don't want to write me anything. To find out what you can write the help command."
        )
    if msg == '/help':
      try:
        if ru:
          await message.channel.send(
            'Мои команды:\nПогода: /weather[место]\nРешение примеров: /calculate[пример]\n\Прикольный факт: /funfact\nГенерация паролей: /password[кол-во символов]\nИ отправка email: /email, subject, msg, your email.'
          )
        if eng:
          await message.channel.send(
            'My commands:\nWeather: /weather[location]\nMath problems: /calculate[example]\nFun fact: /funfact\nGenerating passwords: /password[number of symbols]\nAnd send email: /email, subject, msg, your email.\nImage Generation: /imagegen [prompt]\nChat GPT: /aiquestion [prompt]'
          )
      except:
        await message.channel.send('Choose tour language - ru or eng')

    if '/funfact' in msg:
      await message.channel.send(f.funfact())

    if '/calculate' in msg:
      await message.channel.send(f.math(msg))

    if '/weather' in msg:
      try:
        city = msg.replace('/weather', '')

        try:
          city = city.replace('[', '')
          city = city.replace(']', '')
          city = city.replace('in', '')
        except:
          pass
        try:
          observation = manager.weather_at_place(str(city))
        except:
          await message.channel.send('Uncorrect city')
            
          weather = observation.weather
          temp = weather.temperature("celsius").get("temp")
          temp_max = weather.temperature("celsius").get("temp_max")
          temp_min = weather.temperature("celsius").get("temp_min")
          feels_like = weather.temperature("celsius").get("feels_like")
          rain = weather.rain

          await message.channel.send(
            f"It's outside now: {weather.detailed_status}\nCloudy: {weather.clouds}%\nCurrent temperature: {temp}\nMaximum temperature: {temp_max}\nMinimum temperature: {temp_min}\nFeels like {feels_like}"
          )

          if rain == {}:
            await message.channel.send("no precipitation")
          else:
            await message.channel.send(
              f"it's raining {rain.get('1h')} millimeters of rain")
          await message.channel.send(
            f"Wind speed {weather.wind().get('speed')} m/s")

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
      try:
        if eng:
          await message.channel.send('Email sent!')
        if ru:
          await message.channel.send('Письмо отправленно!')
      except:
        await message.channel.send('Choose tour language - ru or eng')

    if "/mathproblem" in msg:
      await message.channel.send(f.math_ran())

    if "/todo" in msg:
      await message.channel.send(f.todo(msg, author))
    if "/imagegen" in msg:
      await message.channel.send(f.image_gen(msg, author))
    if "/aiquestion" in msg:
      if aiquestionstate == True:
        await message.channel.send(f.chatgpt(msg, author))
      elif aiquestionstate == False:
        await message.channel.send("Feature is disabled!")
    if "/translate" in msg:
      await message.channel.send(f"Translate: {f.translate(msg)}")
    if "/settings" in msg:
      await message.channel.send(f.settings(msg))


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])
