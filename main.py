from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes,filters,MessageHandler

async def text(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    text=update.message.text
    print(update.effective_user.full_name,"|",text)
    r=input("-> ")
    await update.message.reply_html(f"<code>{r}</code>")


app = ApplicationBuilder().token("6647247101:AAEEjUX3QFqmFBJU7okbqz49oXlUpe0M-Zk").build()

app.add_handler(MessageHandler(filters.ALL,text))

app.run_polling()
