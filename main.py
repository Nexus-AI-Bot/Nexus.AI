import discord
import os
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

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class abot(discord.Client):
  def __init__(self):
    super().__init__(intents=discord.Intents.all())
    self.synced = False
  async def on_ready(self):
    await tree.sync(guild=discord.Object(id=1064833489368780810))
    self.synced = True
    print("Bot is online!!!!")


bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="ping", description="Pings the user", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"Pong")

@tree.command(name="hi", description="introduction", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hello {interaction.user}! I'm an artificial intelligence. I'm not perfect yet, so I don't want to write me anything. To find #out what you can write the help command.")

@tree.command(name="help", description="bot commands list", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f"My commands:\nWeather: /weather[location]\nMath problems: /calculate[example]\nFun fact: /funfact\nGenerating passwords: /password[number of symbols]\nAnd send email: /email, subject, msg, your email.\nImage Generation: /imagegen [prompt]\nChat GPT: /aiquestion [prompt]")

@tree.command(name="imagine", description="Create a image using AI", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction, question: str):
  await interaction.response.send_message(f.image_gen(question))

@tree.command(name="weather", description="Send where is the weather", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction, city: str):
  
  owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410')
  manager = owm.weather_manager()
  try:
    observation = manager.weather_at_place(str(city))    
    weather = observation.weather
    temp = weather.temperature("celsius").get("temp")
    temp_max = weather.temperature("celsius").get("temp_max")
    temp_min = weather.temperature("celsius").get("temp_min")
    feels_like = weather.temperature("celsius").get("feels_like")
    rain = weather.rain

    await interaction.response.send_message(
            f"It's outside now: {weather.detailed_status}\nCloudy: {weather.clouds}%\nCurrent temperature: {temp}\nMaximum temperature: {temp_max}\nMinimum temperature: {temp_min}\nFeels like {feels_like}"
          )

    if rain == {}:
      await interaction.response.send_message("no precipitation")
    else:
      await interaction.response.send_message(
          f"it's raining {rain.get('1h')} millimeters of rain")
    await interaction.response.send_message(
        f"Wind speed {weather.wind().get('speed')} m/s")
        
  except:
    await interaction.response.send_message('Incorrect city')
@tree.command(name="askai", description="Ask AI something!", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction, question: str):
  await interaction.response.send_message(f.chatgpt(question, interaction.user))

@tree.command(name="randommath", description="Get a random math question!", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f.math_ran())

@tree.command(name="funfact", description="Random funfacts!", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction):
  await interaction.response.send_message(f.funfact())

@tree.command(name="calculate", description="Calculator in discord!", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction, math_problem: str):
  await interaction.response.send_message(f.math(math_problem))

@tree.command(name="password", description="Get a random password!", guild=discord.Object(id=1064833489368780810))
async def self(interaction: discord.Interaction, symbols_quantity: str):
  await interaction.response.send_message(f.password(symbols_quantity))

@tree.command(name="email", description="Send an email", guild=discord.Object(id=1064833489368780810))
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



bot.run(os.environ['TOKEN'])
