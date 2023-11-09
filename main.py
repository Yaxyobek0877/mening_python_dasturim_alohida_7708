from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes,filters,MessageHandler

async def text(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    text=update.message.text
    print(update.effective_user.full_name,update.effective_user.id,"|",text)
    r=input("-> ")
    if r.split()[0] == "file":
        await update.message.reply_document(document=open("main.txt"),caption=r)

    elif r.split()[0].isnumeric():
        t=""
        for i in r.split()[1:]:
            t+=i
        await context.bot.send_message(chat_id=int(r.split()[0]),text=t)
    else:
        await update.message.reply_html(f"<code>{r}</code>")

    r=input("->")
    if r == "file":
        await update.message.reply_html(f"{open('main.txt', 'r').read()}")

    elif r == ".":
        pass

    elif r.split()[0].isnumeric():
        t=""
        for i in r.split()[1:]:
            t+=i
        await context.bot.send_message(chat_id=int(r.split()[0]),text=t)
    else:
        await update.message.reply_html(f"<code>{r}</code>")


app = ApplicationBuilder().token("6647247101:AAEEjUX3QFqmFBJU7okbqz49oXlUpe0M-Zk").build()

app.add_handler(MessageHandler(filters.ALL,text))

app.run_polling()
