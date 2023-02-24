funfactapi = "https://useless-facts.sameerkumar.website/api"
import requests
import openai
import os
openai.organization = "org-zuDrmFX8G3H6TsAwxsZZ8PLA"
openai.api_key = os.environ['APIKEY']
openai.Model.list()
from replit import db
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
import random
password_simbols = ['@','#','$','&','*']
password_alpha = ['a','b','c','d','e','f','g','q','w','r','t','y','u','i','o','p','s','h','j','k','l','z','x','v','b','n','m']
def funfact():
  api = requests.get(funfactapi)
  funfactgetdict = json.loads(api.content)
  return(funfactgetdict["data"])
  
def password(msg):
  symbols = msg.replace('password','')
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
      return send
  except:
    return 'Неверно введено количество символов!'
    
def math(msg):
  math = msg.replace('math','')
  try:
    solution = eval(math)
    return solution
  except:
    return "Пример написан неправильно!"
def send_email(subject, body, recipients):
  msg = MIMEText(body)
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = recipients
  smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp_server.login(sender, password)
  smtp_server.sendmail(sender, recipients, msg.as_string())
  smtp_server.quit()
  
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
  
def todo(msg, discord_user):
  message = msg.replace('/todo ', '')
  print(message)
  if "add" in message:
    task = message.replace('add', '')
    print(task)
    db[task] = discord_user
    return "Added task!"
  if "list" in message:
    return db[discord_user]
def image_gen(msg, user):
  request = msg.replace('/imagegen ', '')
  response = openai.Image.create(
  prompt=request,
  n=1,
  size="1024x1024"
  )
  image_url = response['data'][0]['url']
  return image_url
def chatgpt(msg, user):
  model_engine = "text-davinci-003"
  prompt = msg.replace("/aiquestion ", "")
  completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  ) 
  response = completion.choices[0].text
  return response