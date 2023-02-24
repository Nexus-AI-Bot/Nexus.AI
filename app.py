import asyncio
#import cool_functions as f
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
import cool_functions as f

chat_msgs = []
online_users = set()

sender = "helper.ai@fluffik.co.uk"
password = "nxukvmybdpgymmjq"

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
          msg_box.append(put_markdown(f'`Helper AI`: My commands:\nWeather: /weather[location]\nMath problems: /calculate[example]\nFun fact: /funfact\nGenerating passwords: /password[number of symbols]\nAnd send email: /email, subject, msg, your email.\nImage Generation: /imagegen [prompt]\nChat GPT: /aiquestion [prompt]import cool_functions as f'))
          
        if msg == '/funfact':
          msg_box.append(put_markdown(f'`Helper AI`: {f.funfact()}'))
          
        if msg =='/calculate':
          msg_box.append(put_markdown(f'`Helper AI`: {f.math(msg)}'))

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