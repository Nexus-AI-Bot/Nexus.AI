funfactapi = "https://useless-facts.sameerkumar.website/api"
import requests
import json
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
def weather():
  city = msg.replace('weather', '')

  try:
    city = city.replace('[', '')
    city = city.replace(']', '')
    city = city.replace('in', '')
  except:
    pass
  try:
    observation = manager.weather_at_place(str(city))
  except:
    await message.channel.send('Город введен неверно.')
    weather = observation.weather
    temp = weather.temperature("celsius").get("temp")
    temp_max = weather.temperature("celsius").get("temp_max")
    temp_min = weather.temperature("celsius").get("temp_min")
            feels_like = weather.temperature("celsius").get("feels_like")
            rain = weather.rain
            if rain == {}:
                r = "Осадков нет"
            else:
                r = f"Идет дождь {rain.get('1h')} милиметров осадков"

            await message.channel.send(f"Сейчас на улице: {weather.detailed_status}\nОблачность: {weather.clouds}%\nТекущая температура: {temp}\nМаксимальная температура: {temp_max}\nМинимальная температура: {temp_min}\nОщущается как {feels_like}\n{r}\nСкорость ветра {weather.wind().get('speed')} м/с")