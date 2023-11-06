from telethon.sync import TelegramClient
from config import *
from time import monotonic
api_id = api_id
api_hash = api_hash
username = 'my_accaount'
client = TelegramClient(username, api_id, api_hash)
client.start()
while True:
    m=monotonic()
    with client:
        chats = client.get_dialogs()
        k=0
        for chat in chats:
            # u_n=chat.entity.username
            try:
                id=chat.entity.id
                ls=0
                def read_messages(u_n):
                    global ls
                    for message in client.iter_messages(u_n):
                        ls+=1
                        if ls==3:
                            break
                read_messages(id)
                if ls <= 2:
                    client.send_message(id,"Assalomu alaykum")
                    client.send_message(id, "Sizga qanday yordam ber olaman")
            except Exception:
                pass

            if k ==5:
                break
            k+=1

    print("Ko'rib chiqdim")
    print(f"Ketgan vaqt: {monotonic()-m}")

