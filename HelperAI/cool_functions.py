funfactapi = "https://useless-facts.sameerkumar.website/api"
import requests
import openai
import os
import uuid
from replit import db
import tensorflow as tf
model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=True)
import numpy as np
from PIL import Image
openai.organization = "org-zuDrmFX8G3H6TsAwxsZZ8PLA"
openai.api_key = os.environ['APIKEY']
openai.Model.list()
math_operations = ["*", "/", "+", "-"]
sender = "helper.ai@fluffik.co.uk"
password = os.environ['PASSWORD']
import json
func = ["add", "remove", "list"]
import smtplib
from pyowm import OWM
from pyowm.utils.config import get_default_config
import random as r
from email.mime.text import MIMEText
password_simbols = ['@','#','$','&','*']
password_alpha = ['a','b','c','d','e','f','g','q','w','r','t','y','u','i','o','p','s','h','j','k','l','z','x','v','b','n','m']
list = ['Rock','Scissors','Paper']


def funfact():
  api = requests.get(funfactapi)
  funfactgetdict = json.loads(api.content)
  return(funfactgetdict["data"])
  
def password(msg):
  symbols = msg
  try:
    if int(symbols)>10:
      return 'В пароле должно быть до 10 символов!'
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
      return f"||{send}||"
  except:
    return 'Неверно введено количество символов!'
    
def math(msg):
  math = msg
  try:
    solution = eval(math)
    return solution
  except:
    return "Пример написан неправильно!"
def math_ran():
  random_number = r.randint(1, 4)
  x = r.randint(1, 100)
  y = r.randint(1, 100)
  if random_number == 1:
    answer = f"{x} + {y} = {x + y}"
  elif random_number == 2:
    answer = f"{x} - {y} = {x - y}"
  elif random_number == 3:
    answer = f"{x} * {y} = {x * y}"
  elif random_number == 4:
    answer = f"{x} / {y} = {x / y}"
  else:
    return "An unknown error occured! Check lines 76 - 89"
  return answer
  
def get_value(key):
  response = requests.get("https://Replit-Database-proxy.fluffik.repl.co/get_value", params={"key": key})
  if response.status_code == 200:
    return response.json()["value"]
  else:
    return None

def delete_value(key):
  response = requests.delete("https://Replit-Database-proxy.fluffik.repl.co/delete_value", params={"key": key})
  if response.status_code == 200:
    return True
  else:
    return False

def list_keys():
  response = requests.get("https://Replit-Database-proxy.fluffik.repl.co/list_keys")
  if response.status_code == 200:
    return response.json()["keys"]
  else:
    return None

def create_key(discord_user, value):
  response = requests.post("https://Replit-Database-proxy.fluffik.repl.co/create_key", json={"discord_user": discord_user, "value": value})
  if response.status_code == 200:
    return True
  else:
    return False

def image_gen(msg):
  request = msg
  response = openai.Image.create(
  prompt=request,
  n=1,
  size="1024x1024"
  )
  image_url = response['data'][0]['url']
  print(image_url)
  return image_url
def chatgpt(msg, user):
  openai.api_key = os.environ['APIKEY']
  model_engine = "davinci"
  prompt = msg
  completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    chat_log=None,
  )
  response = completion.choices[0].text
  return response
def settings(msg):
  mylist1 = msg.split(' ')
  mylist1.remove(mylist1[0])
  category = mylist1[0]
  value = mylist1[1]
  passw = mylist1[2]
  if passw == "admin||adminpass||":
    if input("Password requested through discord. Enter it here.") == os.environ['ADMINPASS']:
      if category == 'aiquestion':
        if value == 'true':
          aiquestionstate = True
          return "Changed to True"
        elif value == 'false':
          aiquestionstate = False
          return "Changed to False"
      else:
        return "Not a valid answer!"
    else:
      print('Wrong password!')
      return 'Error when completing request'

def weather_finder(city):
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

    return (
            f"It's outside now: {weather.detailed_status}\nCloudy: {weather.clouds}%\nCurrent temperature: {temp}\nMaximum temperature: {temp_max}\nMinimum temperature: {temp_min}\nFeels like {feels_like}"
          )

    if rain == {}:
      return ("no precipitation")
    else:
      return (f"it's raining {rain.get('1h')} millimeters of rain")
    return f"Wind speed {weather.wind().get('speed')} m/s"
  except:
    return ('Incorrect city')

def rock_scissors_paper(choice):
  global bot_choose
  bot_choose = r.choice(list)
  global bot_win
  print(bot_choose)
  bot_win = 'Winner: 👉' + ' I'
  if choice == bot_choose.lower():
    return 'Draw'
    
  if choice == 'rock':
    if bot_choose == 'Scissors':
      return 'Scissors. You Win ¯\_(ツ)_/¯'
    else:
      return 'Paper. ' + bot_win
  elif choice == 'Scissors':
    if bot_choose == 'Paper':
      return 'Paper. You Win ¯\_(ツ)_/¯'
    else:
      return 'Rock. ' + bot_win
  elif choice == 'paper':
    if bot_choose == 'Rock':
      return 'Rock. You Win ¯\_(ツ)_/¯'
    else:
      return 'Scissors. ' + bot_win

def buy(user_id, item):   
  if user_id not in db:
    db[user_id] = 0
  if item.lower() == 'cat':
    if db[f"{user_id}-balance"] < 50:
      return ('You do not have enough coins to buy a cat!')
    db[f"{user_id}-balance"] -= 50
    db[f"{user_id}-pet"] = 'cat'
    return ('You bought a cat!')
  else:
    return (f'{item} is not for sale in the shop.')

def preprocess_image(image_path, target_size=(224, 224)):
  image = Image.open(image_path)
  image = image.resize(target_size)
  image_array = np.array(image)
  image_array = np.expand_dims(image_array, axis=0)
  image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
  return image_array
def is_cat(image_path, model):
  image_array = preprocess_image(image_path)
  predictions = model.predict(image_array)
  decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)
  for _, label, confidence in decoded_predictions[0]:
    if label.lower() == 'egyptian_cat' or label.lower() == 'tiger_cat':
      return True, confidence
  return False, 0
def discord_cat_finder(image):
  image_path = image
  is_it_cat, confidence = is_cat(image_path, model)
  return f"Is it a cat? {is_it_cat}. Confidence {confidence}."
