from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,filters,MessageHandler


ls=["A masala\nMenda 3 ta olma bor edi shunda menda nechta olma bor"]

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(f'login: <code>Login yoq</code>\nparol: <code>parol yoq</code>')
    for i in ls:
        await update.message.reply_html(f"<code>{i}</code>")

    await update.message.reply_text(f"masalalar soni hozrida: {len(ls)}")

    await update.message.reply_html("Nima yossalaringham menga keladi. Agar men yana masalarni yozsam uni bilish uchun /start ni bosilar shunda men qoshgan masalarni hammasi keladi.")

async def text(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    text=update.message.text
    print(update.effective_user.full_name,"|",text)
    r=input("-> ")
    await update.message.reply_html(f"<code>{r}</code>")


app = ApplicationBuilder().token("6647247101:AAEEjUX3QFqmFBJU7okbqz49oXlUpe0M-Zk").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(MessageHandler(filters.TEXT,text))

app.run_polling()