import asyncio
#import cool_functions as f
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from email.mime.text import MIMEText
import smtplib
from pywebio.session import defer_call, info as session_info, run_async, run_js
import cool_functions as f
from pyowm import OWM
from pyowm.utils.config import get_default_config

chat_msgs = []
online_users = set()

sender = "helper.ai@fluffik.co.uk"
password = "nxukvmybdpgymmjq"

owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410')
manager = owm.weather_manager()

hi = ['привет','hello','hey','hi', ]  #greetings

MAX_MESSAGES_COUNT = 100

async def main():
    global chat_msgs
    
    put_markdown("## 🧊 Welcome to the chat!")

    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)

    nickname = await input("Enter the chat", required=True, placeholder="Your name", validate=lambda n: "This name is already taken!" if n in online_users or n == '📢' else None)
    online_users.add(nickname)

    chat_msgs.append(('📢', f'`{nickname}` Joined the chat'))
    msg_box.append(put_markdown(f'📢 `{nickname}` Joined the chat!'))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:
        data = await input_group("💭 New message", [
            input(placeholder="Message text ...", name="msg"),
            actions(name="cmd", buttons=["Send", {'label': "Leave the chat", 'type': 'cancel'}])
        ], validate = lambda m: ('msg', "Enter some text!") if m["cmd"] == "Send" and not m['msg'] else None)

        if data is None:
            break

        msg = data['msg'].lower()
        msg_box.append(put_markdown(f"`{nickname}`: {msg}"))
      
        chat_msgs.append((nickname, data['msg']))
        if msg in hi:
          msg_box.append(put_markdown(f"`Helper AI`: Hello {nickname}! I'm an artificial intelligence. I'm not perfect yet, so I don't want to write me anything. To find out what you can write the help command."))
          
        if msg == '/help':
          msg_box.append(put_markdown(f'`Helper AI`: My commands:\nWeather: /weather[location]\nMath problems: /calculate[example]\nFun fact: /funfact\nGenerating passwords: /password[number of symbols]\nSend email: /email, subject, msg, your email.\nImage Generation: /imagegen [prompt]\nAnd Chat GPT: /aiquestion [prompt]import cool_functions as f'))
          
        if msg == '/funfact':
          msg_box.append(put_markdown(f'`Helper AI`: {f.funfact()}'))
          
        if '/calculate' in msg:
          msg_box.append(put_markdown(f'`Helper AI`: {f.math(msg)}'))
          
        if '/weather' in msg:
          try:
            city = msg.replace('/weather','')                                
            city = city.replace('[','')
            city = city.replace(']','')
            city = city.replace('in','')
            observation = manager.weather_at_place(str(city))
        
            weather = observation.weather
            temp = weather.temperature("celsius").get("temp")
            temp_max = weather.temperature("celsius").get("temp_max")
            temp_min = weather.temperature("celsius").get("temp_min")
            feels_like = weather.temperature("celsius").get("feels_like")
            rain = weather.rain
              
            msg_box.append(put_markdown(f"`Helper AI`: It's outside now: {weather.detailed_status}\nCloudy: {weather.clouds}%\nCurrent temperature: {temp}\nMaximum temperature: {temp_max}\nMinimum temperature: {temp_min}\nFeels like {feels_like}"))
                
            if rain == {}:
              msg_box.append(put_markdown("`Helper AI`: No precipitation"))
            else:
              msg_box.append(put_markdown(f"`Helper AI`: It's raining {rain.get('1h')} millimeters of rain"))
                
            msg_box.append(put_markdown(f"`Helper AI`: Wind speed {weather.wind().get('speed')} m/s"))
          except:
            msg_box.append(put_markdown('`Helper AI`: Uncorrect city!'))
        if '/password' in msg:
          msg_box.append(put_markdown(f'`Helper AI`: {f.password(msg)}'))
          
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
          msg_box.append(put_markdown('`Helper AI`: Email send!'))
        if "/imagegen" in msg:
          msg_box.append(put_markdown(f'`Helper AI`: {f.image_gen(msg, nickname)}'))
          
        if "/aiquestion" in msg:
          msg_box.append(put_markdown(f'`Helper AI`: {f.chatgpt(msg, nickname)}'))
    
    refresh_task.close()

    online_users.remove(nickname)
    toast("You left the chat!")
    msg_box.append(put_markdown(f'📢 User `{nickname}` Left the chat!'))
    chat_msgs.append(('📢', f'User `{nickname}` left the chat!'))

    put_buttons(['Re-join'], onclick=lambda btn:run_js('window.location.reload()'))

async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)
        
        for m in chat_msgs[last_idx:]:
            if m[0] != nickname: # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))
        
        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]
        
        last_idx = len(chat_msgs)

if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)