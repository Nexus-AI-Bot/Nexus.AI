import discord
import os
import time
import io
import random
from pyowm import OWM
from googletrans import Translator
import smtplib
from email.mime.text import MIMEText
from pyowm.utils.config import get_default_config
import cool_functions as f
from discord.ext import commands
from discord import app_commands
aiquestionstate = True
sender = "helper.ai@fluffik.co.uk"
password = os.environ['PASSWORD']
hi = [
  'привет',
  'hello',
  'hey',
  'hi',
]  #greetings
import requests
url = "https://discord.com/api/webhooks/1085941872515633182/YPQXCvEcqq18roRZI6UcxoplkY2O5X_7ZXfKyps1AF6LbP5sBBx4gdpS4FYw8ebxr4-T" 
#import discord.opus
#if not discord.opus.is_loaded():
  #discord.opus.load_opus('libopus.so')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class abot(discord.Client):
  def __init__(self):
    super().__init__(intents=discord.Intents.all())
    self.synced = False
  async def on_ready(self):
    await tree.sync(guild=discord.Object(id=1085922093205573763))
    self.synced = True
    print("Bot is online!!!!")


bot = abot()
tree = app_commands.CommandTree(bot)

class Menu(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(label='Send message', style=discord.ButtonStyle.grey)
  async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message("You clicked me...")

@tree.command(name="ping", description="Pings the user", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"Pong")

@tree.command(name="hi", description="introduction", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hello {interaction.user}! I'm an artificial intelligence. I'm not perfect yet, so I don't want to write me anything. To find #out what you can write the help command.")

@tree.command(name="help", description="bot commands list", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"My commands:\nWeather: /weather[location]\nMath problems: /calculate[example]\nFun fact: /funfact\nGenerating passwords: /password[number of symbols]\nAnd send email: /email, subject, msg, your email.\nImage Generation: /imagegen [prompt]\nChat GPT: /aiquestion [prompt]")

@tree.command(name="weather", description="Send where is the weather", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, city: str):
  await interaction.response.send_message(f.weather_finder(city))

@tree.command(name="askai", description="Ask AI something!", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, question: str):
  await interaction.response.send_message(f.chatgpt(question, interaction.user))

@tree.command(name="randommath", description="Get a random math question!", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f.math_ran())

@tree.command(name="funfact", description="Random funfacts!", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f.funfact())

@tree.command(name="calculate", description="Calculator in discord!", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, math_problem: str):
  await interaction.response.send_message(f.math(math_problem))

@tree.command(name="password", description="Get a random password!", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, symbols_quantity: str):
  await interaction.response.send_message(f.password(symbols_quantity))

@tree.command(name="email", description="Send an email", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, subject: str, body: str, recipient: str):
  recipients = recipient
  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = recipients
  smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp_server.login(sender, password)
  smtp_server.sendmail(sender, recipients, msg.as_string())
  smtp_server.quit()
  await interaction.response.send_message("Sent!")

#@tree.command(name="imagine", description="ai", guild=discord.Object(id=1085922093205573763))
#async def self(interaction: discord.Interaction, question: str):
  #answer = f.image_gen(question)
  #await interaction.response.send_message("Generating...")
  #time.sleep(3)
  #await interaction.response.edit_message(answer)

@tree.command(name="button", description="A random test button", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction):
  view = Menu()
  await interaction.response.send_message(view=view)


@tree.command(name="webhook", description="Webhook update", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, update: str):
  data = {
      "content" : update,
      "username" : "updates"
  }
  result = requests.post(url, json = data)
  try:
    result.raise_for_status()
  except requests.exceptions.HTTPError as err:
    print(err)
  else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
    await interaction.response.send_message("Update sent")

@tree.command(name="cat", description="Check if the given image is a cat", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, image: discord.Attachment):
  send_image = await image.read()
  await interaction.response.send_message(f.discord_cat_finder(io.BytesIO(send_image)))

@tree.command(name="join", description="join", guild=discord.Object(id=1085922093205573763))
async def self(interaction: discord.Interaction, channel: discord.VoiceChannel, mode: str):
  if mode == "join":
    if discord.voice_client is not None:
      await channel.connect()
      await interaction.response.send_message("connected")
      voice_client = interaction.guild.voice_client
      source = MP3AudioSource("android-bass-133563.mp3")
      voice_client.play(source)
  elif mode == "leave":
    await channel.guild.voice_client.disconnect()
    await interaction.response.send_message("disconnected")

bot.run(os.environ['TOKEN'])
