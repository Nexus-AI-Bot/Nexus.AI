
import discord
import os
import random
from pyowm import OWM
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
    await message.channel.send('Email sent!')