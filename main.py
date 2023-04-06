import discord
import os
import time
from datetime import datetime, timedelta
import datetime
#from replit import db
import urllib
import io as iio
import pytesseract
from discord.ui import Select, View
import ffmpeg
import discord.opus
import random
import youtube_dl
import openai
from io import BytesIO
from pyowm import OWM
from googletrans import Translator
import smtplib
from pyrandmeme import *
from PIL import Image, ImageOps
from email.mime.text import MIMEText
from random import choice as ch
from pyowm.utils.config import get_default_config
import cool_functions as f
from discord.ext import commands
from discord import app_commands
# from skimage import io
# import the image
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
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path='.gitignore/.env')

# Get the values of the environment variables
password_google = os.environ.get('PASSWORD')
token = os.environ.get('TOKEN')



aiquestionstate = True
sender = "helper.ai@fluffik.co.uk"
password = os.environ['PASSWORD']
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


#

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pets = {}
#


class Menu(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(label='Add', style=discord.ButtonStyle.grey)
  async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
    f.create_key(user, job)
    await interaction.response.send_message("Done")

  @discord.ui.button(label='Remove', style=discord.ButtonStyle.grey)
  async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
    f.delete_value(user)
    await interaction.response.send_message("Done")

  @discord.ui.button(label='List', style=discord.ButtonStyle.grey)
  async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f.list_keys())

#

class ShopDropdown(discord.ui.Select):
  def __init__(self):
    options=[
      discord.SelectOption(label='Cat', description='50 helpers')
    ]
    super().__init__(placeholder="Choose a pet you want to buy!", options=options, min_values=1, max_values=1)
  async def callback(self, interaction: discord.Interaction):
    global petpick
    petpick = self.values[0]
    user_id = str(interaction.user.id)
    await interaction.response.send_message(f.buy(user_id, petpick))

class ShopView(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.add_item(ShopDropdown())

  
class Game(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(label='Rock', style=discord.ButtonStyle.grey)
  async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f.rock_scissors_paper('rock'))

  @discord.ui.button(label='Scissors', style=discord.ButtonStyle.grey)
  async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f.rock_scissors_paper('scissors'))

  @discord.ui.button(label='Paper', style=discord.ButtonStyle.grey)
  async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f.rock_scissors_paper('paper'))


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
      embed1.add_field(name="Start a todo list! (in development)", value="```/todo```", inline=False)
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
@tree.command(name="ping", description="Pings the user")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"Pong")

@tree.command(name="hi", description="introduction")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hello {interaction.user}! I'm an artificial intelligence. I'm not perfect yet, so I don't want to write me anything. To find #out what you can write the help command.")

@tree.command(name="help", description="bot commands list")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message("Help!", view=HelpConfigView())

@tree.command(name="weather", description="Send where is the weather")
async def self(interaction: discord.Interaction, city: str):
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

@tree.command(name="askai", description="Ask AI something!")
async def self(interaction: discord.Interaction, question: str):
  await interaction.response.send_message(f.chatgpt(question, interaction.user))

@tree.command(name="randommath", description="Get a random math question!")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f.math_ran())

@tree.command(name="funfact", description="Random funfacts!")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f.funfact())

@tree.command(name="calculate", description="Calculator in discord!")
async def self(interaction: discord.Interaction, math_problem: str):
  await interaction.response.send_message(f.math(math_problem))

@tree.command(name="password", description="Get a random password!")
async def self(interaction: discord.Interaction, symbols_quantity: str):
  await interaction.response.send_message(f.password(symbols_quantity))

@tree.command(name="email", description="Send an email")
async def self(interaction: discord.Interaction, subject: str, body: str, recipient: str):
  await interaction.response.defer()
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
  await interaction.followup.send("Sent!", ephemeral=True)

@tree.command(name="emoji", description="Random emoji!")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(ch(emoji))

@tree.command(name="imagine", description="ai")
async def self(interaction: discord.Interaction, prompt: str):
  await interaction.response.defer()
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
  openai.api_key = os.environ.get('API_KEY')
  e = {'created': datetime.datetime.fromtimestamp(response['created']), 'images': images}
  e['created']
  images = e['images']
  images[0]
  for image in images:
      print('Image Generated')
  urllib.request.urlretrieve(image, "dalle.png")
  await interaction.followup.send(file=discord.File('dalle.png'))


@tree.command(name="todo", description="Todo list")
async def self(interaction: discord.Interaction, task: str):
  global job
  global user
  job = task
  user = interaction.user
  str(user)
  view = Menu()
  await interaction.response.send_message(view=view, ephemeral=True)

@tree.command(name="translate", description="Translation")
async def self(interaction: discord.Interaction, text: str,dest_language: str):
  translation = translator.translate(text, dest=dest_language)
  await interaction.response.send_message(translation.text)

@tree.command(name="embed", description="Test embed")
async def self(interaction: discord.Interaction, member: discord.User):
  name = member.display_name
  pfp = member.display_avatar
  embed = discord.Embed(title="test embed!", description="this is a test description", colour=discord.Colour.random())
  embed.set_author(name=f"{name}", url="https://cdn.discordapp.com/emojis/1084268640649609336.webp?size=48&quality=lossless")
  embed.set_thumbnail(url=f"{pfp}")
  embed.add_field(name="This is a field 1", value="This is a value")
  embed.add_field(name="This is a field 2", value="This is a value", inline=True)
  embed.add_field(name="This is a field 3", value="This is a value", inline=False)
  embed.set_footer(text=f"{name} made this!")
  await interaction.response.send_message(embed=embed)

@tree.command(name="grey", description="grey image")
async def self(interaction: discord.Interaction,image: discord.Attachment):
  img = await image.read()
  img2 = iio.BytesIO(img)
  await interaction.response.defer()
  image_content = io.imread(img2) 
  image_grey = color.rgb2gray(image_content)
  io.imsave('grey.png', image_grey)
  await interaction.followup.send(file=discord.File('grey.png'))

@tree.command(name="rockpaperscissors", description="Rock, paper, scissors")
async def self(interaction: discord.Interaction):
  name = interaction.user
  pfp = "https://cdn.discordapp.com/attachments/1085937814211936267/1088763806425043059/IMG_1951.PNG"
  embed = discord.Embed(title="Rock Paper Scissors", description="Choose your attack.", colour=discord.Colour.random())
  embed.set_author(name=f"{name}")
  embed.set_thumbnail(url=f"{pfp}")
  embed.set_footer(text=f"{name} started the game")
  view = Game()
  await interaction.response.send_message(view=view, ephemeral=True, embed=embed)

@tree.command(name="balance", description="Check your balance")
async def self(interaction: discord.Interaction):
  user_id = str(interaction.user.id)
  if f"{user_id}-balance" not in db.keys():
    db[f"{user_id}-balance"] = 0
  if f"{user_id}-pet" not in db.keys():
    db[f"{user_id}-pet"] = None
  balance = db[f"{user_id}-balance"]
  pet = db[f"{user_id}-pet"]
  await interaction.response.send_message(f'Your balance is {balance} coins. Your pet is {pet}.')

@tree.command(name="gamble", description="Gamble for money!")
async def self(interaction: discord.Interaction, amount: int):
  user_id = str(interaction.user.id)
  if user_id not in db:
    db[f"{user_id}-balance"] = 0
  if amount > db[f"{user_id}-balance"]:
    return await interaction.response.send_message('You do not have enough coins to gamble that much!')
  list = ['win','lose']
  outcome = random.choice(list)
  print(outcome)
  if outcome == 'win':
    db[f"{user_id}-balance"] += amount
    await interaction.response.send_message(f'You won {amount} coins!')
  if outcome=='lose':
    db[f"{user_id}-balance"] -= amount
    await interaction.response.send_message(f'You lost {amount} coins!')


@tree.command(name="work", description="Work for money!")
async def self(interaction: discord.Interaction):
  user_id = str(interaction.user.id)
  if user_id not in db:
    db[f"{user_id}-balance"]
  earnings = random.randint(1, 10)
  db[f"{user_id}-balance"] += earnings
  await interaction.response.send_message(f'You earned {earnings} coins for your hard work!')

@tree.command(name="shop", description="Check out the shop!")
async def self(interaction: discord.Interaction):
  embed = discord.Embed(title='Shop', color=0x00ff00)
  embed.add_field(name='Cat', value='Cost: 50 helpers')
  await interaction.response.send_message(embed=embed)

@tree.command(name="buy", description="Buy a pet!")
async def self(interaction: discord.Interaction):
  await interaction.response.send_message("Choose your pet!", view=ShopView())


@tree.command(name="test", description="Tic tac toe game!")
async def self(interaction: discord.Interaction, place: str):
  global game
  global board
  await interaction.response.defer()
  user = interaction.user
  pfp = user.display_avatar
  embed = discord.Embed(title="test embed!", description="this is a test description", colour=discord.Colour.random())
  avatar = embed.set_thumbnail(url=f"{pfp}")
  url = f"{pfp}"
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  if game == False:
    board = [[None, None, None],
    [None, None, None],
    [None, None, None]]
    image = Image.open('tic tac toe.png')
    img.save("avatar.png")
    avatar = Image.open('avatar.png')
    print(image.size)
    avatar = avatar.convert('RGB')
    avatar = avatar.resize((150,150))

  if game:
    image = Image.open('result.png')
    img.save("avatar.png")
    avatar = Image.open('avatar.png')
    print(image.size)
    avatar = avatar.convert('RGB')
    avatar = avatar.resize((150,150))
  x1 = 100
  y1 = 100
  x2 = 100
  y2 = 350
  x3 = 100
  y3 = 600
  x4 = 350
  y4 = 100
  x5 = 350
  y5 = 350
  x6 = 350
  y6 = 600
  x7 = 600
  y7 = 100
  x8 = 600
  y8 = 350
  x9 = 600
  y9 = 600
  
  players = [avatar, None]
  current_player = 0

  
  if place == 'a1':      
      image.paste(avatar, (x1,y1))
      board[0][0] = current_player
      image.save('result.png')
  
  if place == 'a2':      
      image.paste(avatar, (x2,y2))
      board[0][1] = current_player
      image.save('result.png')
  if place == 'a3':      
      image.paste(avatar, (x3,y3))
      board[0][2] = current_player
      image.save('result.png')
  if place == 'b1':      
      image.paste(avatar, (x4,y4))
      board[1][0] = current_player
      image.save('result.png')
  if place == 'b2':      
      image.paste(avatar, (x5,y5))
      board[1][1] = current_player
      image.save('result.png')
  if place == 'b3':      
      image.paste(avatar, (x6,y6))
      board[1][2] = current_player
      image.save('result.png')
  if place == 'c1':      
      image.paste(avatar, (x7,y7))
      board[2][0] = current_player
      image.save('result.png')
  if place == 'c2':      
      image.paste(avatar, (x8,y8))
      board[2][1] = current_player
      image.save('result.png')
  if place == 'c3':      
      image.paste(avatar, (x9,y9))
      board[2][2] = current_player
      image.save('result.png')
  
  # add the other image placement blocks for the other squares
  
  victory = False
  print(board)
  
  # check rows
  for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] == current_player:
          victory = True
  
  # check columns
  for i in range(3):
      if board[0][i] == board[1][i] == board[2][i] == current_player:
          victory = True
  
  # check diagonals
  if board[0][0] == board[1][1] == board[2][2] == current_player:
      victory = True
  if board[0][2] == board[1][1] == board[2][0] == current_player:
      victory = True
  
  if victory:
      await interaction.followup.send("win!")
      game = False
  else:
      current_player = 1 - current_player
      game = True
    
    # add code to switch to the next player here
    
  await interaction.followup.send(file=discord.File('result.png'))

@tree.command(name='dm', description='Dm someone')
async def self(interaction: discord.Interaction, user: discord.User, message: str):
  embed = discord.Embed(title=message, description='Sent using Helper.AI discord bot')
  await user.send(embed=embed)
  await interaction.response.send_message("Sent!", ephemeral=True)

@tree.command(name='meme', description='Get a random meme!')
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(embed=await pyrandmeme())

@tree.command(name="cat", description="Check if the given image is a cat")
async def self(interaction: discord.Interaction, image: discord.Attachment):
  send_image = await image.read()
  await interaction.response.send_message(f.discord_cat_finder(iio.BytesIO(send_image)))

  
bot.run(token)
