print("Hello world")
print("yep its runnin")
global pet
global user_id_sell
import discord
import os
import time
import cv2
#from IMGGEN import Generate as imggen
from datetime import datetime, timedelta
import datetime
#from replit import db
import urllib
import io as iio
from discord.ui import Select, View
import json
import ffmpeg
import discord.opus
from discord import ui
import random
from datetime import datetime
import pytz
from io import BytesIO
from pyowm import OWM
from googletrans import Translator
import smtplib
from pyrandmeme import *
import logger
from PIL import Image, ImageOps
from email.mime.text import MIMEText
import typing
from random import choice as ch
from pyowm.utils.config import get_default_config
import cool_functions as f
from class_economy import Economy
from discord.ext import commands
from discord import app_commands
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
from skimage import io
#import tensorflow as tf
import requests
import bcrypt
#from dotenv import load_dotenv
import os
import threading
from forex_python.converter import CurrencyRates
from class_friend import Friend


print('All libaries were sucsessfully imported.')

# Load environment variables from .env file
#load_dotenv(dotenv_path='.gitignore/.env')

# Get the values of the environment variables

#password = os.environ.get('PASSWORD222333')

password = input("Password: ")


response = requests.post(url='https://whale-app-yk39r.ondigitalocean.app/values', data={'password': password})

temp = response.json()
print(temp)

password_google = temp['google_pass']
token = temp['token']
import openai
openai.organization = "org-zuDrmFX8G3H6TsAwxsZZ8PLA"
openai.api_key = temp['api_key']
openai.Model.list()

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def get_results(query):
    url = 'https://api.duckduckgo.com'
    params = {
        'q': query,
        'format': 'json'
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data['RelatedTopics']


aiquestionstate = True
sender = "helper.ai@fluffik.co.uk"
password = temp['google_pass']
emoji = [':grinning:', ':smiling_imp:', ':wink:', ':heart_eyes:', ':kissing_heart:']
FFMPEG_PATH = '/home/runner/Helper.AI discord bot/node_modules/ffmpeg-static/ffmpeg'
#discord.opus.load_opus("./libopus.so.0.8.0")
translator = Translator()
global game
game = False

emoji = ["😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😎", "😍", "😘", "😜", "😝", "😛", "🤑", "🤗", "🤔", "🤐", "🤢", "🤕", "🤧", "😷", "👹", "👺", "💩", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", "❤️", "💔", "💕", "💖", "💗", "💘", "💙", "💚", "💛", "💜", "🖤", "💝", "💞", "💟", "💌", "💤", "💢", "💥", "💦", "💨", "🕳️", "💭", "👥", "👤", "👫", "👬", "👭", "👀", "👁️", "👅", "👄", "💋", "💯", "🔥", "💪", "👊", "👌", "👍", "👎", "👏", "🙌", "👐", "🤝", "🙏", "✌️", "🤞", "🖖", "🤘", "👋", "💅", "👂", "👃", "🤙", "👆", "👇", "👈", "👉", "🖕", "🤚", "🖐️", "✋", "💬", "🗨️", "🗯️", "🔊", "📢", "📣", "🔔", "🔕", "🎵", "🎶", "🎤", "🎧", "🎼", "🎹", "🥁", "🎷", "🎺", "🎸", "🎻", "🎬", "🎥", "🎦", "🏰", "🌋", "🌅", "🌄", "🌠", "🌌", "🌈", "☀️", "🌞", "⭐", "🌟"]


hi = [
  'привет',
  'hello',
  'hey',
  'hi',
]  #greetings
import requests
url = "https://discord.com/api/webhooks/1085941872515633182/YPQXCvEcqq18roRZI6UcxoplkY2O5X_7ZXfKyps1AF6LbP5sBBx4gdpS4FYw8ebxr4-T" 
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())







# Create an instance of the Economy class
economy = Economy(bot)
friend_obj = Friend()

# Print the balance

def buy(user_id, item):
  balance = economy.query(user_id)  # get the user's balance from the database
  if item.lower() == "cat":
    if balance < 150:
      return "You do not have enough coins to buy a cat!"
    economy.add_pet(user_id, "cat")  # add a cat pet to the user's account in the database
    economy.delete(user_id, 150)  # subtract 50 coins from the user's balance in the database
    return "You bought a cat!"
  elif item.lower() == "dog":
    if balance < 100:
      return "You do not have enough coins to buy a Dog!"
    economy.add_pet(user_id, "dog")  # add a cat pet to the user's account in the database
    economy.delete(user_id, 100)  # subtract 50 coins from the user's balance in the database
    return "You bought a Dog!"
  elif item.lower() == "parrot":
    if balance < 80:
      return "You do not have enough coins to buy a Parrot!"
    economy.add_pet(user_id, "parrot")  # add a cat pet to the user's account in the database
    economy.delete(user_id, 80)  # subtract 50 coins from the user's balance in the database
    return "You bought a Parrot!"
  elif item.lower() == "gold fish":
    if balance < 60:
      return "You do not have enough coins to buy a Gold Fish!"
    economy.add_pet(user_id, "gold fish")  # add a cat pet to the user's account in the database
    economy.delete(user_id, 60)  # subtract 50 coins from the user's balance in the database
    return "You bought a Gold Fish!"
  elif item.lower() == "rabbit":
    if balance < 50:
      return "You do not have enough coins to buy a Rabbit!"
    economy.add_pet(user_id, "rabbit")  # add a cat pet to the user's account in the database
    economy.delete(user_id, 50)  # subtract 50 coins from the user's balance in the database
    return "You bought a Rabbit!"
  elif item.lower() == "hamster":
    if balance < 20:
      return "You do not have enough coins to buy a Hamster!"
    economy.add_pet(user_id, "hamster")  # add a cat pet to the user's account in the database
    economy.delete(user_id, 20)  # subtract 50 coins from the user's balance in the database
    return "You bought a Hamster!"
  else:
    return f"{item} is not for sale in the shop."
  

class abot(discord.Client):
  def __init__(self):
    super().__init__(intents=discord.Intents.all())
    self.synced = False
  async def on_ready(self):
    await tree.sync()
    self.synced = True
    print("Bot is online!!!!")



bot = abot()
tree = app_commands.CommandTree(bot)

@bot.event
async def on_guild_join(guild):
  print(f"Joined a new guild: {guild.name}!")
  
  commands =["hi", "help", "weather", "askai", "randommath", "funfact", "calculate", "password", "email", "emoji", "imagine", "greyout", "balance", "gamble", "work", "shop", "dm", "meme", "search", "invite", "convert", "roast", "sell", "face", "recipe", "currency_convert", "friend"]
  
  print(guild.id)
  
  for i in commands:
    json = {"guild_id":str(guild.id),"command_name":str(i),"new_value":True,"signature":"nexusaisignature202020202020213456adminpass123456789"}
    requests.post('https://nexus-ai.xyz/bot/command/update', json=json)
  
  if guild.system_channel:
    await guild.system_channel.send("Thank you for adding Nexus.AI to this server! Make sure to check out the server dashboard at the [Nexus.AI](https://nexus-ai.xyz) website!")

#




class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pets = {}
#

class Pay(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(label='Monthly', style=discord.ButtonStyle.green)
  async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f"[Monthly](https://nexus-ai.xyz/create-checkout-session-monthly/{interaction.user.id})", ephemeral=True)
  
  @discord.ui.button(label='Yearly', style=discord.ButtonStyle.green)
  async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f"[Yearly](https://nexus-ai.xyz/create-checkout-session-yearly/{interaction.user.id})", ephemeral=True)


#

class ShopDropdown(discord.ui.Select):
  def __init__(self):
    options=[
      discord.SelectOption(label='Cat', description='150 nexus'),
      discord.SelectOption(label='Dog', description='100 nexus'),
      discord.SelectOption(label='Parrot', description='80 nexus'),
      discord.SelectOption(label='Gold Fish', description='60 nexus'),
      discord.SelectOption(label='Rabbit', description='50 nexus'),
      discord.SelectOption(label='Hamster', description='20 nexus')
    ]
    super().__init__(placeholder="Choose a pet you want to buy!", options=options, min_values=1, max_values=1)
  async def callback(self, interaction: discord.Interaction):
    global petpick
    petpick = self.values[0]
    user_id = str(interaction.user.id)
    await interaction.response.send_message(buy(user_id, petpick))

class ShopView(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.add_item(ShopDropdown())

#

class Friend_Questionnaire(ui.Modal, title='Some questions about you'):
  answer = ui.TextInput(label='Your interests, seperated by commas', style=discord.TextStyle.paragraph, required=True)
  async def on_submit(self, interaction: discord.Interaction):
      answer = str(self.answer)
      try:
        answer.split(' ')
        friend_obj.add(f"{interaction.user.name}#{interaction.user.discriminator}", answer)
        await interaction.response.send_message(f'You have been added. Now do /friend to find some friends!', ephemeral=True)
      except: 
        await interaction.response.send_message(f'A error happened.', ephemeral=True)

#

class HelpConfigDropdown(discord.ui.Select):
  def __init__(self):
    options=[
      discord.SelectOption(label='Fun', description='Fun commands!'),
      discord.SelectOption(label='Economy', description='Economy commands!')
    ]
    super().__init__(placeholder="Choose a category", options=options, min_values=1, max_values=1)
  async def callback(self, interaction: discord.Interaction):
    choice = self.values[0]
    if choice == 'Fun':
      embed1 = discord.Embed(title="Fun", description="You selected fun in the category", colour=discord.Colour.random())
      embed1.add_field(name="Random meme!", value="```/meme```", inline=False)
      embed1.add_field(name="Random funfact!", value="```/funfact```", inline=False)
      embed1.add_field(name="Get the weather!", value="```/weather```", inline=False)
      embed1.add_field(name="Ask AI something!", value="```/askai```", inline=False)
      embed1.add_field(name="Get AI art!", value="```/imagine```", inline=False)
      embed1.add_field(name="Get a random math question!", value="```/randommath```", inline=False)
      embed1.add_field(name="Calculator!", value="```/calculate```", inline=False)
      embed1.add_field(name="Get a random emoji!", value="```/emoji```", inline=False)
      embed1.add_field(name="Get a random password!", value="```/password```", inline=False)
      await interaction.response.edit_message(embed=embed1)
    if choice == 'Economy':
      embed2 = discord.Embed(title="Economy", description="You selected economy in the category", colour=discord.Colour.random())
      embed2.add_field(name="Balance command", value="```/balance```", inline=False)
      embed2.add_field(name="Work command", value="```/work```", inline=False)
      embed2.add_field(name="Gamble command", value="```/gamble```", inline=False)
      embed2.add_field(name="Shop command", value="```/shop```", inline=False)
      embed2.add_field(name="Buy command", value="```/buy```", inline=False)
      await interaction.response.edit_message(embed=embed2)
class HelpConfigView(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.add_item(HelpConfigDropdown())
    

#
@logger.log
@tree.command(name="hi", description="Intruduction to the bot")
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  
  if request.text == 'True':
    await interaction.response.send_message(f"Hello {interaction.user}! I'm an artificial intelligence called Nexus.AI. I'm not perfect yet, so I am always being updated by my wonderful developers! To find #out what I can do, do /help.")
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)!')
  
@logger.log
@tree.command(name="help", description="List all the availible commands")
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message('Help!', view=HelpConfigView())
  else:
    await interaction.response.send_message("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")

@logger.log
@tree.command(name="weather", description="Check the weather in a given city")
async def self(interaction: discord.Interaction, city: str):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    embed = discord.Embed(title="Weather", description=f"This is a weather in {city}", colour=discord.Colour.random())
    owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410')
    manager = owm.weather_manager()
    try:
      observation = manager.weather_at_place(city) 
      weather = observation.weather
      temp = weather.temperature("celsius").get("temp")
      temp_max = weather.temperature("celsius").get("temp_max")
      temp_min = weather.temperature("celsius").get("temp_min")
      feels_like = weather.temperature("celsius").get("feels_like")
      rain = weather.rain
      embed.add_field(name="It's outside now:",   value=weather.detailed_status)
      embed.add_field(name="Cloudy:", value=weather.clouds, inline=True)
      embed.add_field(name="Current temperature:", value=temp, inline=False)
      embed.add_field(name="Maximum temperature:", value=temp_max, inline=False)
      embed.add_field(name="Minimum temperature:", value=temp_min, inline=False)
      embed.add_field(name="Feels like", value=feels_like, inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=True)
    except:
      await interaction.response.send_message('Incorrect city!', ephemeral=True)
    else:
      await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="askai", description="Ask ChatGPT something")
async def self(interaction: discord.Interaction, question: str):
  await interaction.response.defer()
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    user_full_id = str(interaction.user.id)
    global f
    e = economy.query_pay(user_full_id)
    try:
      f = e.split(',')
    except AttributeError:
      view = Pay()
      embedpay = discord.Embed(title="You are accessing a paid feature", colour=discord.Colour.random(), description="Consider upgrading to the AI Plan")
      embedpay.add_field(name="Features of the AI plan:", value=" ", inline=False)
      embedpay.add_field(name="/askai", value="Generate __**unlimited**__ ChatGPT content!", inline=False)
      embedpay.add_field(name="/imagine", value="Generate __**unlimited**__ AI art for Dall-E!", inline=False)
      await interaction.followup.send(embed=embedpay, view=view)
      economy.add_pay(user_full_id, 'aiplan,notpaid')

    if 'aiplan' in f and 'paid' in f:
      if f.index('aiplan') + 1 == f.index('paid'):
        system_msg = f'You are Nexus.AI, a discord bot with an intent of helping people and integrating common apps into discord. Do not mention yourself as an AI  or Chatbot. Only refer to yourself as Nexus.AI. The users name is {str(interaction.user.display_name)}. That is the only infomation you know about the user.'
        user_msg = question 
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg}
        ]
        )

        response_from_gpt = response["choices"][0]["message"]["content"]
        await interaction.followup.send(response_from_gpt)
    else:
      view = Pay()
      embedpay = discord.Embed(title="You are accessing a paid feature", colour=discord.Colour.random(), description="Consider upgrading to the AI Plan")
      embedpay.add_field(name="Features of the AI plan:", value=" ", inline=False)
      embedpay.add_field(name="/askai", value="Generate __unlimited__ ChatGPT content!", inline=False)
      embedpay.add_field(name="/imagine", value="Generate unlimited AI art for Dall-E!", inline=False)
      await interaction.followup.send(embed=embedpay, view=view)
      economy.add_pay(user_full_id, 'aiplan,notpaid')
  else:
    await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="randommath", description="Get a random math question")
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message(f.math_ran())
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')
@logger.log
@tree.command(name="funfact", description="Get a random funfact")
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message(f.funfact())
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')
  
@logger.log
@tree.command(name="calculate", description="Calculate a math problem")
async def self(interaction: discord.Interaction, num1: int, num2: int, operator: str):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message(f.math(num1, num2, operator))
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')
  
@logger.log
@tree.command(name="password", description="Get a random password")
async def self(interaction: discord.Interaction, symbols_quantity: str):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message(f.password(symbols_quantity), ephemeral=True)
  else:
    await interaction.response.send_message("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")

@logger.log
@tree.command(name="email", description="Send an email")
async def self(interaction: discord.Interaction, subject: str, body: str, recipient: str):
  await interaction.response.defer()
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    recipients = recipient
    print(recipient)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password_google)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
    await interaction.followup.send(f"Sent email with subject {subject} to {recipients}", ephemeral=True)
  else:
    await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="emoji", description="Get a random emoji")
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message(ch(emoji))
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="imagine", description="Generate an AI image")
async def self(interaction: discord.Interaction, prompt: str):
  await interaction.response.defer()
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    user_full_id = interaction.user.id
    global f
    e = economy.query_pay(user_full_id)
    try:
      f = e.split(',')
    except AttributeError:
      view = Pay()
      embedpay = discord.Embed(title="You are accessing a paid feature", colour=discord.Colour.random(), description="Consider upgrading to the AI Plan")
      embedpay.add_field(name="Features of the AI plan:", value=" ", inline=False)
      embedpay.add_field(name="/askai", value="Generate __unlimited__ ChatGPT content!", inline=False)
      embedpay.add_field(name="/imagine", value="Generate unlimited AI art for Dall-E!", inline=False)
      await interaction.followup.send(embed=embedpay, view=view)
      economy.add_pay(user_full_id, 'aiplan,notpaid')

    if 'aiplan' in f and 'paid' in f:
      if f.index('aiplan') + 1 == f.index('paid'):
        num_image=1
        SIZES = ('1024x1024', '512x512', '256x256')
        size='512x512'
        output_format='url'
        """
        params: 
            prompt (str):
            num_image (int):
            size (str):
            output_format (str):
        """
        try:
          images = []
          response = openai.Image.create(
            prompt=prompt,
            n=num_image,
            size=size,
            response_format=output_format
          )
          print(response)
          if output_format == 'url':
            for image in response['data']:
              images.append(image.url)
          elif output_format == 'b64_json':
            for image in response['data']:
              images.append(image.b64_json)
        except:
          print('didnt work lol')
        openai.api_key = temp['api_key']
        e = {'images': images}
        images = e['images']
        images[0]
        for image in images:
            print('Image Generated')
        urllib.request.urlretrieve(image, "dalle.png")
        await interaction.followup.send(file=discord.File('dalle.png'))
        await os.remove('dalle.png')
    else:
      view = Pay()
      embedpay = discord.Embed(title="You are accessing a paid feature", colour=discord.Colour.random(), description="Consider upgrading to the AI Plan")
      embedpay.add_field(name="Features of the AI plan:", value=" ", inline=False)
      embedpay.add_field(name="/askai", value="Generate __unlimited__ ChatGPT content!", inline=False)
      embedpay.add_field(name="/imagine", value="Generate unlimited AI art for Dall-E!", inline=False)
      await interaction.followup.send(embed=embedpay, view=view)
      economy.add_pay(user_full_id, 'aiplan,notpaid')
  else:
    await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="greyout", description="Greyout an image")
async def self(interaction: discord.Interaction,image: discord.Attachment):
  await interaction.response.defer()
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    img = await image.read()
    img2 = iio.BytesIO(img)
    image_content = io.imread(img2) 
    image_grey = color.rgb2gray(image_content)
    io.imsave('grey.png', image_grey)
    await interaction.followup.send(file=discord.File('grey.png'))
  else:
    await interaction.followup.send("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")

#@logger.log
#@tree.command(name="rockpaperscissors", description="Rock, paper, scissors")
#async def self(interaction: discord.Interaction):
  #name = interaction.user
  #pfp = "https://cdn.discordapp.com/attachments/1085937814211936267/1088763806425043059/IMG_1951.PNG"
  #embed = discord.Embed(title="Rock Paper Scissors", description="Choose your attack.", colour=discord.Colour.random())
  #embed.set_author(name=f"{name}")
  #embed.set_thumbnail(url=f"{pfp}")
  #embed.set_footer(text=f"{name} started the game")
  #view = Game()
  #await interaction.response.send_message(view=view, ephemeral=True, embed=embed)

@logger.log
@tree.command(name="balance", description="Check your balance in the economy system")
async def self(interaction: discord.Interaction):
  await interaction.response.defer()
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    user_id = str(interaction.user.id)
    balance = economy.query(user_id)  # get the user's balance from the database
    pets = economy.check_user_pet(user_id)  # get a list of the user's pets from the database
    if len(pets) > 0:
      pet_message = "Your pets are: " + ", ".join(pets)
    else:
      pet_message = "You don't have any pets yet."

    await interaction.followup.send(f"Your balance is {balance} coins. {pet_message}")
  else:
    await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="gamble", description="Gamble for money in the economy system")
async def self(interaction: discord.Interaction, amount: int):
    await interaction.response.defer()  # defer the response before processing
    
    id = interaction.guild.id
    json = {
      'guild_id':id,
      'command_name': interaction.command.name
    }
    request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
    if request.text == 'True': 
      user_id = str(interaction.user.id)
      balance = economy.query(user_id)  # get the user's balance from the database

      if amount > balance:
        await interaction.followup.send('You do not have enough coins to gamble that much!')
      else:
        outcomes = ['win', 'lose']
        outcome = random.choice(outcomes)

        if outcome == 'win':
            economy.add(user_id, amount)  # add the winnings to the user's balance in the database
            await interaction.followup.send(f"You won {amount} coins!")
        else:
            economy.delete(user_id, amount)  # subtract the loss from the user's balance in the database
            await interaction.followup.send(f"You lost {amount} coins!")
    else:
      await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="work", description="Work for money in the economy system")
async def self(interaction: discord.Interaction):
  await interaction.response.defer()
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    user_id = str(interaction.user.id)
    earnings = random.randint(1, 10)
    economy.add(user_id, earnings)
    await interaction.followup.send(f'You earned {earnings} coins for your hard work!')
  else:
    await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="shop", description="Shop for pets in the economy system")
async def self(interaction: discord.Interaction):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    embed = discord.Embed(title='Shop', color=0x00ff00)
    embed.add_field(name='Cat', value='Cost: 150 nexus')
    embed.add_field(name='Dog', value='Cost: 100 nexus')
    embed.add_field(name='Parrot', value='Cost: 80 nexus')
    embed.add_field(name='Gold Fish', value='Cost: 60 nexus')
    embed.add_field(name='Rabbit', value='Cost: 50 nexus')
    embed.add_field(name='Hamster', value='Cost: 20 nexus')
    await interaction.response.send_message(embed=embed, view=ShopView())
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

#@logger.log
#@tree.command(name="test", description="Tic tac toe game!")
#async def self(interaction: discord.Interaction, place: str):
  #global game
  #global board
  #await interaction.response.defer()
  #user = interaction.user
  #pfp = user.display_avatar
  #embed = discord.Embed(title="test embed!", description="this is a test description", colour=discord.Colour.random())
  #avatar = embed.set_thumbnail(url=f"{pfp}")
  #url = f"{pfp}"
  #response = requests.get(url)
  #img = Image.open(BytesIO(response.content))
  #if game == False:
    #board = [[None, None, None],
    #[None, None, None],
    #[None, None, None]]
    #image = Image.open('tic tac toe.png')
    #img.save("avatar.png")
    #avatar = Image.open('avatar.png')
    #print(image.size)
    #avatar = avatar.convert('RGB')
    #avatar = avatar.resize((150,150))

  #if game:
    #image = Image.open('result.png')
    #img.save("avatar.png")
    #avatar = Image.open('avatar.png')
    #print(image.size)
    #avatar = avatar.convert('RGB')
    #avatar = avatar.resize((150,150))
  #x1 = 100
  #y1 = 100
  #x2 = 100
  #y2 = 350
  #x3 = 100
  #y3 = 600
  #x4 = 350
  #y4 = 100
  #x5 = 350
  #y5 = 350
  #x6 = 350
  #y6 = 600
  #x7 = 600
  #y7 = 100
  #x8 = 600
  #y8 = 350
  #x9 = 600
  #y9 = 600
  
  #players = [avatar, None]
  #current_player = 0

  
  #if place == 'a1':      
      #image.paste(avatar, (x1,y1))
      #board[0][0] = current_player
      #image.save('result.png')
  
  #if place == 'a2':      
      #image.paste(avatar, (x2,y2))
      #board[0][1] = current_player
      #image.save('result.png')
  #if place == 'a3':      
      #image.paste(avatar, (x3,y3))
      #board[0][2] = current_player
      #image.save('result.png')
  #if place == 'b1':      
      #image.paste(avatar, (x4,y4))
      #board[1][0] = current_player
      #image.save('result.png')
  #if place == 'b2':      
      #image.paste(avatar, (x5,y5))
      #board[1][1] = current_player
      #image.save('result.png')
  #if place == 'b3':      
      #image.paste(avatar, (x6,y6))
      #board[1][2] = current_player
      #image.save('result.png')
  #if place == 'c1':      
      #image.paste(avatar, (x7,y7))
      #board[2][0] = current_player
      #image.save('result.png')
  #if place == 'c2':      
      #image.paste(avatar, (x8,y8))
      #board[2][1] = current_player
      #image.save('result.png')
  #if place == 'c3':      
      #image.paste(avatar, (x9,y9))
      #board[2][2] = current_player
      #image.save('result.png')
  
  # add the other image placement blocks for the other squares
  
  #victory = False
  #print(board)
  
  # check rows
  #for i in range(3):
      #if board[i][0] == board[i][1] == board[i][2] == current_player:
          #victory = True
  
  # check columns
  #for i in range(3):
      #if board[0][i] == board[1][i] == board[2][i] == current_player:
         # victory = True
  
  # check diagonals
  #if board[0][0] == board[1][1] == board[2][2] == current_player:
      #victory = True
  #if board[0][2] == board[1][1] == board[2][0] == current_player:
      #victory = True
  
  #if victory:
      #await interaction.followup.send("win!")
      #game = False
  #else:
      #current_player = 1 - current_player
      #game = True
    
    # add code to switch to the next player here
    
  #await interaction.followup.send(file=discord.File('result.png'))

@logger.log
@tree.command(name='dm', description='DM someone in this server')
async def self(interaction: discord.Interaction, user: discord.User, message: str):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    embed = discord.Embed(title=message, description='Sent using [Nexus.AI](https://nexus-ai.xyz) discord bot')
    await user.send(embed=embed)
    await interaction.response.send_message(f"Sent message {message} to user {user.display_name}", ephemeral=True)
  else:
    await interaction.response.send_message("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")

@logger.log
@tree.command(name='meme', description='Get a random meme')
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message(embed=await pyrandmeme())
  else:
    await interaction.response.send_message("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")

@logger.log
@tree.command(name="search", description="Google something")
async def self(interaction: discord.Interaction, query: str):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    embed = discord.Embed(title="Your search results", description="First 5 shown", colour=discord.Colour.random())
    results = get_results(query)
    if len(results) == 0:
      for i, result in enumerate(results[:5]):
        if 'Text' in result and 'FirstURL' in result:
            embed.add_field(name=f"Result {i+1}", value=f"{i+1}. {result['Text']} - {result['FirstURL']}", inline=False)
      await interaction.response.send_message(embed=embed)
    else:
      await interaction.response.send_message(f"We scraped the internet far and wide but couldn't find anything for {query}. :(")
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="invite", description="Invite the bot")
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    await interaction.response.send_message("Server invite link: https://discord.gg/RwWaA3QxVw \nBot invite link: https://nexus-ai.xyz")
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="convert", description="Convert units")
async def self(interaction: discord.Interaction, number: int, from_unit: str, to_unit: str):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    answer = f.convert_SI(number, from_unit, to_unit)
    if answer == "among":
      await interaction.response.send_message("Valid conversions are mm, cm, m,")
    else:
      await interaction.response.send_message(f"Converted {number} from {from_unit} to {to_unit}. Answer is {answer}")
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name='roast', description='Roast someone')
async def self(interaction: discord.Interaction, member: discord.Member):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    with open("data/roast.json") as r:
      roasts = json.load(r)
    name = member.name
    random_roast = random.choice(roasts["roasts"])
    roast = f"{name}, {random_roast['roast']}"
    await interaction.response.send_message(roast)
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

async def drink_autocompletion(interaction: discord.Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
  data = []
  for pet in ['cat', 'dog', 'parrot', 'gold fish', 'rabbit', 'hamster']:
    if current.lower() in pet.lower():
      data.append(app_commands.Choice(name=pet, value=pet))
  return data 

@logger.log
@tree.command(name="sell", description="Sell your pet")
@app_commands.autocomplete(pet=drink_autocompletion)
async def self(interaction: discord.Interaction, pet: str):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    user_id_sell = interaction.user.id
    user_pets = economy.check_user_pet(user_id_sell)
    if user_pets.count(pet) == 1:
      if pet == 'cat':
        economy.add(user_id_sell, 150)
        economy.delete_pet(user_id_sell, pet)
        await interaction.response.send_message(f'Your Cat has been sold', ephemeral=True)
      elif pet == 'dog':
        economy.add(user_id_sell, 100)
        economy.delete_pet(user_id_sell, pet)
        await interaction.response.send_message(f'Your Dog has been sold', ephemeral=True)
      elif pet == 'parrot':
        economy.add(user_id_sell, 80)
        economy.delete_pet(user_id_sell, pet)
        await interaction.response.send_message(f'Your Parrot has been sold', ephemeral=True)
      elif pet == 'gold fish':
        economy.add(user_id_sell, 60)
        economy.delete_pet(user_id_sell, pet)
        await interaction.response.send_message(f'Your Gold Fish has been sold', ephemeral=True)
      elif pet == 'rabbit':
        economy.add(user_id_sell, 50)
        economy.delete_pet(user_id_sell, pet)
        await interaction.response.send_message(f'Your Rabbit has been sold', ephemeral=True)
      elif pet == 'hamster':
        economy.add(user_id_sell, 50)
        economy.delete_pet(user_id_sell, pet)
        await interaction.response.send_message(f'Your Hamster has been sold', ephemeral=True)
      else:
        await interaction.response.send_message(content='Either you do not have that type of pet or this pet does not exist')
        return
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')



@logger.log
@tree.command(name="face", description="Face recognition")
async def self(interaction: discord.Interaction,image: discord.Attachment):
  await interaction.response.defer()
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True': 
    attachment = image
    await attachment.save('face.png')
    image2 = cv2.imread('face.png')
    faces = face_cascade_db.detectMultiScale(image2,1.1,19)
    for(x,y,w,h) in faces:
      cv2.rectangle(image2,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imwrite('face_rec_result.png', image2)
    await interaction.followup.send(file=discord.File('face_rec_result.png'))
    os.remove('face_rec_result.png')
  else:
    await interaction.followup.send('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')

@logger.log
@tree.command(name="recipe", description="Recipe finder")
async def self(interaction: discord.Interaction,meal:str):
  
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    app_id = "160652b9"
    app_key = "2b2e37458836cfe80cf3389f82991655"

    url = f"https://api.edamam.com/search?q={meal}&app_id={app_id}&app_key={app_key}"

    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      try:
        first_recipe = data['hits'][0]['recipe']
      except:
        await interaction.response.send_message("An error occurred while requesting the recipe. Please try again later.")
      recipe_label = first_recipe['label']
      recipe_url = first_recipe['url']

      await interaction.response.send_message(f"Recipe found for '{meal}': {recipe_label}\n{recipe_url}")
  else:
    await interaction.response.send_message("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")

@logger.log
@tree.command(name="currency_convert", description="Convert currency")
async def self(interaction: discord.Interaction, number: int, from_currency: str, to_currency: str):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True':
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, number)
    await interaction.response.send_message(f'Result: {round(converted_amount,2)} {to_currency}')
  else:
    await interaction.response.send_message('This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)')


class Friend_Questionnaire(ui.Modal, title='Some questions about you'):
  answer = ui.TextInput(label='Your interests, seperated by commas', style=discord.TextStyle.paragraph, required=True)
  async def on_submit(self, interaction: discord.Interaction):
      answer = str(self.answer)
      try:
        answer.split(' ')
        friend_obj.add(f"{interaction.user.name}#{interaction.user.discriminator}", answer)
        await interaction.response.send_message(f'You have been added. Now do /friend to find some friends!', ephemeral=True)
      except: 
        await interaction.response.send_message(f'A error happened.', ephemeral=True)


@logger.log
@tree.command(name='friend', description='Find a friend on discord')
async def self(interaction: discord.Interaction):
  id = interaction.guild.id
  json = {
    'guild_id':id,
    'command_name': interaction.command.name
  }
  request = requests.post('https://nexus-ai.xyz/bot/command/query', json=json)
  if request.text == 'True': 
    find = friend_obj.query_username(f"{interaction.user.name}#{interaction.user.discriminator}")
    if find == None:
      await interaction.response.send_modal(Friend_Questionnaire())
    else:
      user_likes = friend_obj.query_likes(f"{interaction.user.name}#{interaction.user.discriminator}")
      same_likes = friend_obj.query_same_likes(user_likes)
      samelikes2 = ""
      userlikes2 = ""
      for i in same_likes:
        samelikes2 = samelikes2 + f"{i},"
      for i in user_likes:
        userlikes2 = userlikes2 + f"{i},"

      await interaction.response.send_message(f"{samelikes2} has the same likes as you (Reminder, your likes are {userlikes2})")
  else:
    await interaction.response.send_message("This command has been disabled on the dashboard, ask a moderator or server owner to enable it by going to the [Nexus.AI Website](https://nexus-ai.xyz)")


bot.run(token)

