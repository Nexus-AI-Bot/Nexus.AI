funfactapi = "https://useless-facts.sameerkumar.website/api"
import requests
math_operations = ["*", "/", "+", "-"]
sender = "helper.ai@fluffik.co.uk"
password = "nxukvmybdpgymmjq"
import json
import smtplib
import math as m
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

#subject = command.replace('email', '')
#e = 'email' + subject
#body = command.replace(e, '')
#a = subject + body
#recipients = command.replace(a, '')
#msg = MIMEText(body)
#msg['Subject'] = subject
#msg['From'] = sender
#msg['To'] = ', '.join(recipients)
#smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#smtp_server.login(sender, password)
#smtp_server.sendmail(sender, recipients, msg.as_string())
#smtp_server.quit()
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
  operation = math_operations[r.randint(1, 4)]
  x = r.randint(1, 100)
  y = r.randint(1, 100)
  answer = x, operation, y
  return answer
  #hey bro im working on a feature dont touch plz