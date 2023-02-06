funfactapi = "https://useless-facts.sameerkumar.website/api"
import requests
import json
import smtplib
from email.message import EmailMessage
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
def send_email(command): 
  you = command.replace('email', '')
  e = you + 'email '
  info = command.replace(e, '')
  msg = EmailMessage()
  msg.set_content(info)
  me = 'info@fluffik.co.uk'
    
  
  msg['Subject'] = 'this is a email'
  msg['From'] = me
  msg['To'] = you

  s = smtplib.SMTP('localhost')
  s.send_message(msg)
  s.quit()
