from telegram.ext import Updater, CommandHandler, ConversationHandler,MessageHandler,Filters,CallbackQueryHandler
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove, InlineKeyboardButton,InlineKeyboardMarkup

import numpy as np
import primer,threading, matn_convert
from dbworker import DBHelper
db=DBHelper("Malumotlar.db")


inline_keyboard = [[
                        InlineKeyboardButton("Su'niy Intelekt", url = 'https://t.me/suniy_intelekt')
                    ],
                    [
                        InlineKeyboardButton("Guinness rekordlar", url="https://t.me/Guinness_rekordlar")
                    ],
                    [
                        InlineKeyboardButton("Tasdiqlash", callback_data="Tasdiqlash")
                    ]
                    ]
button_inlinekeyboard=InlineKeyboardMarkup(inline_keyboard,resize_keyboard=True)

custom_keyboard = [["Lotin ➡ Kirill","Kirill ➡ Lotin"]]
button_replykeyboard = ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
Krill = False
Lotin = False
Azolik = False
tartib = 0
tartib_matn = 0

def start(update, context):
    try:
        global Azolik
        Azolik, _ , _ = primer.azolikni_tekshirish(update.message.chat_id)
        if Azolik:
            update.message.reply_html("😃Siz  botimizdan bemalol foydalanishingiz mumkin.",
                                     reply_markup=button_replykeyboard)
            db.set_state(update.message.chat_id, 2)
        else:
            update.message.reply_html("@uzlatin_bot ga hush kelibsiz.\n "
                                  "Bot xizmatidan foydalanish uchun biz tavsiya qilgan kanallarga  \n "
                                    "a'zo bo'lib, 'Tasdiqlash' tugmasini bosib qo'yasiz. Rahmat!\n"
                                  "Agar bizda xatolikni aniqlasangiz /xato buyrug'i orqali bizga jo'nating.",reply_markup=button_inlinekeyboard)
            db.set_state(update.message.chat_id, 1)

    except Exception as ex:
        print(ex)
def xato(update, context):
    try:
        update.message.reply_html("Bizga xatolikga ega so‘zni yoki so‘zlarni jo‘nating. Kiritilgan matn uzunligi 256 dan oshmasligi shart.")
        db.set_state(update.message.chat_id, 3)

    except Exception:
        pass
def text_xato(update, context):
    try:
        user=''
        first=''
        try:
            idchat = update.message.chat_id
            user = update.message.to_dict()['chat']['username']
        except Exception:
            pass
        try:
            first = update.message.to_dict()['chat']['first_name']
        except Exception:
            pass
        context.bot.send_message(chat_id=551490877, text=" Xatoliklar: " + str(idchat) + "\n" + user + " " + first + " \n " +
                                                         update.message.to_dict()['text'])
        update.message.reply_html("Bizga yordam berganingiz uchun katta rahmat. Tez orada kamchilikni to‘g‘irlaymiz.")
        db.set_state(update.message.chat_id, 2)

    except Exception as ex:
        print(ex)

def tekshirish(update, context):
    try:
        global Azolik,client
        query = update.callback_query
        if query['data'] == "Tasdiqlash":

            Azolik, prim, yangi = primer.azolikni_tekshirish(query.message.chat_id)
            if Azolik :
                query.message.delete()
                query.message.reply_html("😃Siz endi botimizdan bemalol foydalanishingiz mumkin.",
                                         reply_markup=button_replykeyboard)
                db.set_state(update.message.chat_id, 2)

            else:
                if prim != '' and yangi != '':
                    query.message.delete()
                    query.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>"+str(prim) + "</b> " + " <b>" + str(yangi)+ "</b> kanallariga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
                else:
                    query.message.delete()
                    query.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>"+str(prim) + "</b> " + " <b>" + str(yangi)+ "</b> kanaliga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
                db.set_state(update.message.chat_id, 1)

    except Exception as ex:
        pass


# Bu yerda foydalanuvchi uchun kerakli habarni botga chiqarib beriladi
def text(update, context):
    try:
        if update.message.to_dict()['text'] == "Lotin ✅ Kirill" or update.message.to_dict()['text'] == "Lotin ➡ Kirill":
            kril(update,context)
        elif update.message.to_dict()['text'] == "Kirill ➡ Lotin" or  update.message.to_dict()['text'] == "Kirill ✅ Lotin":
            lotin(update,context)
        else:
            state = db.get_state(update.message.chat_id)
            if int(state) == 3:
                text_xato(update,context)
                db.set_state(update.message.chat_id, 2)
            else:
                global Azolik,Krill,Lotin,tartib_matn
                Azolik, prim, yangi = primer.azolikni_tekshirish(update.message.chat_id)
                if Azolik:
                    if Lotin:
                        print(tartib_matn,"-lotin")
                        if tartib_matn  == 50:
                            tartib_matn = 0
                        if tartib_matn == 0:
                            tartib_matn += 1
                            ll1 = threading.Thread(target=matn_convert.l1, args=(update, context, 'lotin',))
                            ll1.start()
                        elif tartib_matn == 1:
                            tartib_matn += 1
                            ll2 = threading.Thread(target=matn_convert.l2, args=(update, context, 'lotin',))
                            ll2.start()
                        elif tartib_matn == 2:
                            tartib_matn += 1
                            ll3 = threading.Thread(target=matn_convert.l3, args=(update, context, 'lotin',))
                            ll3.start()
                        elif tartib_matn == 3:
                            tartib_matn += 1
                            ll4 = threading.Thread(target=matn_convert.l4, args=(update, context, 'lotin',))
                            ll4.start()
                        elif tartib_matn == 4:
                            tartib_matn += 1
                            ll5 = threading.Thread(target=matn_convert.l5, args=(update, context, 'lotin',))
                            ll5.start()
                        elif tartib_matn == 5:
                            tartib_matn += 1
                            ll6 = threading.Thread(target=matn_convert.l6, args=(update, context, 'lotin',))
                            ll6.start()
                        elif tartib_matn == 6:
                            tartib_matn += 1
                            ll7 = threading.Thread(target=matn_convert.l7, args=(update, context, 'lotin',))
                            ll7.start()
                        elif tartib_matn == 7:
                            tartib_matn += 1
                            ll8 = threading.Thread(target=matn_convert.l8, args=(update, context, 'lotin',))
                            ll8.start()
                        elif tartib_matn == 8:
                            tartib_matn += 1
                            ll9 = threading.Thread(target=matn_convert.l9, args=(update, context, 'lotin',))
                            ll9.start()
                        elif tartib_matn == 9:
                            tartib_matn += 1
                            ll10 = threading.Thread(target=matn_convert.l10, args=(update, context, 'lotin',))
                            ll10.start()
                        elif tartib_matn == 10:
                            tartib_matn += 1
                            ll11 = threading.Thread(target=matn_convert.l11, args=(update, context, 'lotin',))
                            ll11.start()
                        elif tartib_matn == 11:
                            tartib_matn += 1
                            ll12 = threading.Thread(target=matn_convert.l12, args=(update, context, 'lotin',))
                            ll12.start()
                        elif tartib_matn == 12:
                            tartib_matn += 1
                            ll13 = threading.Thread(target=matn_convert.l13, args=(update, context, 'lotin',))
                            ll13.start()
                        elif tartib_matn == 13:
                            tartib_matn += 1
                            ll14 = threading.Thread(target=matn_convert.l14, args=(update, context, 'lotin',))
                            ll14.start()
                        elif tartib_matn == 14:
                            tartib_matn += 1
                            ll15 = threading.Thread(target=matn_convert.l15, args=(update, context, 'lotin',))
                            ll15.start()
                        elif tartib_matn == 15:
                            tartib_matn += 1
                            ll16 = threading.Thread(target=matn_convert.l16, args=(update, context, 'lotin',))
                            ll16.start()
                        elif tartib_matn == 16:
                            tartib_matn += 1
                            ll17 = threading.Thread(target=matn_convert.l17, args=(update, context, 'lotin',))
                            ll17.start()
                        elif tartib_matn == 17:
                            tartib_matn += 1
                            ll18 = threading.Thread(target=matn_convert.l18, args=(update, context, 'lotin',))
                            ll18.start()
                        elif tartib_matn == 18:
                            tartib_matn += 1
                            ll19 = threading.Thread(target=matn_convert.l19, args=(update, context, 'lotin',))
                            ll19.start()
                        elif tartib_matn == 19:
                            tartib_matn += 1
                            ll20 = threading.Thread(target=matn_convert.l20, args=(update, context, 'lotin',))
                            ll20.start()
                        elif tartib_matn == 20:
                            tartib_matn += 1
                            ll21 = threading.Thread(target=matn_convert.l21, args=(update, context, 'lotin',))
                            ll21.start()
                        elif tartib_matn == 21:
                            tartib_matn += 1
                            ll22 = threading.Thread(target=matn_convert.l22, args=(update, context, 'lotin',))
                            ll22.start()
                        elif tartib_matn == 22:
                            tartib_matn += 1
                            ll23 = threading.Thread(target=matn_convert.l23, args=(update, context, 'lotin',))
                            ll23.start()
                        elif tartib_matn == 23:
                            tartib_matn += 1
                            ll24 = threading.Thread(target=matn_convert.l24, args=(update, context, 'lotin',))
                            ll24.start()
                        elif tartib_matn == 24:
                            tartib_matn += 1
                            ll25 = threading.Thread(target=matn_convert.l25, args=(update, context, 'lotin',))
                            ll25.start()
                        elif tartib_matn == 25:
                            tartib_matn += 1
                            ll26 = threading.Thread(target=matn_convert.l26, args=(update, context, 'lotin',))
                            ll26.start()
                        elif tartib_matn == 26:
                            tartib_matn += 1
                            ll27 = threading.Thread(target=matn_convert.l27, args=(update, context, 'lotin',))
                            ll27.start()
                        elif tartib_matn == 27:
                            tartib_matn += 1
                            ll28 = threading.Thread(target=matn_convert.l28, args=(update, context, 'lotin',))
                            ll28.start()
                        elif tartib_matn == 28:
                            tartib_matn += 1
                            ll29 = threading.Thread(target=matn_convert.l29, args=(update, context, 'lotin',))
                            ll29.start()
                        elif tartib_matn == 29:
                            tartib_matn += 1
                            ll30 = threading.Thread(target=matn_convert.l30, args=(update, context, 'lotin',))
                            ll30.start()
                        elif tartib_matn == 30:
                            tartib_matn += 1
                            ll31 = threading.Thread(target=matn_convert.l31, args=(update, context, 'lotin',))
                            ll31.start()
                        elif tartib_matn == 31:
                            tartib_matn += 1
                            ll32 = threading.Thread(target=matn_convert.l32, args=(update, context, 'lotin',))
                            ll32.start()
                        elif tartib_matn == 32:
                            tartib_matn += 1
                            ll33 = threading.Thread(target=matn_convert.l33, args=(update, context, 'lotin',))
                            ll33.start()
                        elif tartib_matn == 33:
                            tartib_matn += 1
                            ll34 = threading.Thread(target=matn_convert.l34, args=(update, context, 'lotin',))
                            ll34.start()
                        elif tartib_matn == 34:
                            tartib_matn += 1
                            ll35 = threading.Thread(target=matn_convert.l35, args=(update, context, 'lotin',))
                            ll35.start()
                        elif tartib_matn == 35:
                            tartib_matn += 1
                            ll36 = threading.Thread(target=matn_convert.l36, args=(update, context, 'lotin',))
                            ll36.start()
                        elif tartib_matn == 36:
                            tartib_matn += 1
                            ll37 = threading.Thread(target=matn_convert.l37, args=(update, context, 'lotin',))
                            ll37.start()
                        elif tartib_matn == 37:
                            tartib_matn += 1
                            ll38 = threading.Thread(target=matn_convert.l38, args=(update, context, 'lotin',))
                            ll38.start()
                        elif tartib_matn == 38:
                            tartib_matn += 1
                            ll39 = threading.Thread(target=matn_convert.l39, args=(update, context, 'lotin',))
                            ll39.start()
                        elif tartib_matn == 39:
                            tartib_matn += 1
                            ll40 = threading.Thread(target=matn_convert.l40, args=(update, context, 'lotin',))
                            ll40.start()
                        elif tartib_matn == 40:
                            tartib_matn += 1
                            ll41 = threading.Thread(target=matn_convert.l41, args=(update, context, 'lotin',))
                            ll41.start()
                        elif tartib_matn == 41:
                            tartib_matn += 1
                            ll42 = threading.Thread(target=matn_convert.l42, args=(update, context, 'lotin',))
                            ll42.start()
                        elif tartib_matn == 42:
                            tartib_matn += 1
                            ll43 = threading.Thread(target=matn_convert.l43, args=(update, context, 'lotin',))
                            ll43.start()
                        elif tartib_matn == 43:
                            tartib_matn += 1
                            ll44 = threading.Thread(target=matn_convert.l44, args=(update, context, 'lotin',))
                            ll44.start()
                        elif tartib_matn == 44:
                            tartib_matn += 1
                            ll45 = threading.Thread(target=matn_convert.l45, args=(update, context, 'lotin',))
                            ll45.start()
                        elif tartib_matn == 45:
                            tartib_matn += 1
                            ll46 = threading.Thread(target=matn_convert.l46, args=(update, context, 'lotin',))
                            ll46.start()
                        elif tartib_matn == 46:
                            tartib_matn += 1
                            ll47 = threading.Thread(target=matn_convert.l47, args=(update, context, 'lotin',))
                            ll47.start()
                        elif tartib_matn == 47:
                            tartib_matn += 1
                            ll48 = threading.Thread(target=matn_convert.l48, args=(update, context, 'lotin',))
                            ll48.start()
                        elif tartib_matn == 48:
                            tartib_matn += 1
                            ll49 = threading.Thread(target=matn_convert.l49, args=(update, context, 'lotin',))
                            ll49.start()
                        elif tartib_matn == 49:
                            tartib_matn += 1
                            ll50 = threading.Thread(target=matn_convert.l50, args=(update, context, 'lotin',))
                            ll50.start()

                    elif Krill:
                        print(tartib_matn,"-kril")

                        if tartib_matn == 50:
                            tartib_matn = 0
                        if tartib_matn == 0:
                            tartib_matn += 1
                            ll1 = threading.Thread(target=matn_convert.l1, args=(update, context, 'kril',))
                            ll1.start()
                        elif tartib_matn == 1:
                            tartib_matn += 1
                            ll2 = threading.Thread(target=matn_convert.l2, args=(update, context, 'kril',))
                            ll2.start()
                        elif tartib_matn == 2:
                            tartib_matn += 1
                            ll3 = threading.Thread(target=matn_convert.l3, args=(update, context, 'kril',))
                            ll3.start()
                        elif tartib_matn == 3:
                            tartib_matn += 1
                            ll4 = threading.Thread(target=matn_convert.l4, args=(update, context, 'kril',))
                            ll4.start()
                        elif tartib_matn == 4:
                            tartib_matn += 1
                            ll5 = threading.Thread(target=matn_convert.l5, args=(update, context, 'kril',))
                            ll5.start()
                        elif tartib_matn == 5:
                            tartib_matn += 1
                            ll6 = threading.Thread(target=matn_convert.l6, args=(update, context, 'kril',))
                            ll6.start()
                        elif tartib_matn == 6:
                            tartib_matn += 1
                            ll7 = threading.Thread(target=matn_convert.l7, args=(update, context, 'kril',))
                            ll7.start()
                        elif tartib_matn == 7:
                            tartib_matn += 1
                            ll8 = threading.Thread(target=matn_convert.l8, args=(update, context, 'kril',))
                            ll8.start()
                        elif tartib_matn == 8:
                            tartib_matn += 1
                            ll9 = threading.Thread(target=matn_convert.l9, args=(update, context, 'kril',))
                            ll9.start()
                        elif tartib_matn == 9:
                            tartib_matn += 1
                            ll10 = threading.Thread(target=matn_convert.l10, args=(update, context, 'kril',))
                            ll10.start()
                        elif tartib_matn == 10:
                            tartib_matn += 1
                            ll11 = threading.Thread(target=matn_convert.l11, args=(update, context, 'kril',))
                            ll11.start()
                        elif tartib_matn == 11:
                            tartib_matn += 1
                            ll12 = threading.Thread(target=matn_convert.l12, args=(update, context, 'kril',))
                            ll12.start()
                        elif tartib_matn == 12:
                            tartib_matn += 1
                            ll13 = threading.Thread(target=matn_convert.l13, args=(update, context, 'kril',))
                            ll13.start()
                        elif tartib_matn == 13:
                            tartib_matn += 1
                            ll14 = threading.Thread(target=matn_convert.l14, args=(update, context, 'kril',))
                            ll14.start()
                        elif tartib_matn == 14:
                            tartib_matn += 1
                            ll15 = threading.Thread(target=matn_convert.l15, args=(update, context, 'kril',))
                            ll15.start()
                        elif tartib_matn == 15:
                            tartib_matn += 1
                            ll16 = threading.Thread(target=matn_convert.l16, args=(update, context, 'kril',))
                            ll16.start()
                        elif tartib_matn == 16:
                            tartib_matn += 1
                            ll17 = threading.Thread(target=matn_convert.l17, args=(update, context, 'kril',))
                            ll17.start()
                        elif tartib_matn == 17:
                            tartib_matn += 1
                            ll18 = threading.Thread(target=matn_convert.l18, args=(update, context, 'kril',))
                            ll18.start()
                        elif tartib_matn == 18:
                            tartib_matn += 1
                            ll19 = threading.Thread(target=matn_convert.l19, args=(update, context, 'kril',))
                            ll19.start()
                        elif tartib_matn == 19:
                            tartib_matn += 1
                            ll20 = threading.Thread(target=matn_convert.l20, args=(update, context, 'kril',))
                            ll20.start()
                        elif tartib_matn == 20:
                            tartib_matn += 1
                            ll21 = threading.Thread(target=matn_convert.l21, args=(update, context, 'kril',))
                            ll21.start()
                        elif tartib_matn == 21:
                            tartib_matn += 1
                            ll22 = threading.Thread(target=matn_convert.l22, args=(update, context, 'kril',))
                            ll22.start()
                        elif tartib_matn == 22:
                            tartib_matn += 1
                            ll23 = threading.Thread(target=matn_convert.l23, args=(update, context, 'kril',))
                            ll23.start()
                        elif tartib_matn == 23:
                            tartib_matn += 1
                            ll24 = threading.Thread(target=matn_convert.l24, args=(update, context, 'kril',))
                            ll24.start()
                        elif tartib_matn == 24:
                            tartib_matn += 1
                            ll25 = threading.Thread(target=matn_convert.l25, args=(update, context, 'kril',))
                            ll25.start()
                        elif tartib_matn == 25:
                            tartib_matn += 1
                            ll26 = threading.Thread(target=matn_convert.l26, args=(update, context, 'kril',))
                            ll26.start()
                        elif tartib_matn == 26:
                            tartib_matn += 1
                            ll27 = threading.Thread(target=matn_convert.l27, args=(update, context, 'kril',))
                            ll27.start()
                        elif tartib_matn == 27:
                            tartib_matn += 1
                            ll28 = threading.Thread(target=matn_convert.l28, args=(update, context, 'kril',))
                            ll28.start()
                        elif tartib_matn == 28:
                            tartib_matn += 1
                            ll29 = threading.Thread(target=matn_convert.l29, args=(update, context, 'kril',))
                            ll29.start()
                        elif tartib_matn == 29:
                            tartib_matn += 1
                            ll30 = threading.Thread(target=matn_convert.l30, args=(update, context, 'kril',))
                            ll30.start()
                        elif tartib_matn == 30:
                            tartib_matn += 1
                            ll31 = threading.Thread(target=matn_convert.l31, args=(update, context, 'kril',))
                            ll31.start()
                        elif tartib_matn == 31:
                            tartib_matn += 1
                            ll32 = threading.Thread(target=matn_convert.l32, args=(update, context, 'kril',))
                            ll32.start()
                        elif tartib_matn == 32:
                            tartib_matn += 1
                            ll33 = threading.Thread(target=matn_convert.l33, args=(update, context, 'kril',))
                            ll33.start()
                        elif tartib_matn == 33:
                            tartib_matn += 1
                            ll34 = threading.Thread(target=matn_convert.l34, args=(update, context, 'kril',))
                            ll34.start()
                        elif tartib_matn == 34:
                            tartib_matn += 1
                            ll35 = threading.Thread(target=matn_convert.l35, args=(update, context, 'kril',))
                            ll35.start()
                        elif tartib_matn == 35:
                            tartib_matn += 1
                            ll36 = threading.Thread(target=matn_convert.l36, args=(update, context, 'kril',))
                            ll36.start()
                        elif tartib_matn == 36:
                            tartib_matn += 1
                            ll37 = threading.Thread(target=matn_convert.l37, args=(update, context, 'kril',))
                            ll37.start()
                        elif tartib_matn == 37:
                            tartib_matn += 1
                            ll38 = threading.Thread(target=matn_convert.l38, args=(update, context, 'kril',))
                            ll38.start()
                        elif tartib_matn == 38:
                            tartib_matn += 1
                            ll39 = threading.Thread(target=matn_convert.l39, args=(update, context, 'kril',))
                            ll39.start()
                        elif tartib_matn == 39:
                            tartib_matn += 1
                            ll40 = threading.Thread(target=matn_convert.l40, args=(update, context, 'kril',))
                            ll40.start()
                        elif tartib_matn == 40:
                            tartib_matn += 1
                            ll41 = threading.Thread(target=matn_convert.l41, args=(update, context, 'kril',))
                            ll41.start()
                        elif tartib_matn == 41:
                            tartib_matn += 1
                            ll42 = threading.Thread(target=matn_convert.l42, args=(update, context, 'kril',))
                            ll42.start()
                        elif tartib_matn == 42:
                            tartib_matn += 1
                            ll43 = threading.Thread(target=matn_convert.l43, args=(update, context, 'kril',))
                            ll43.start()
                        elif tartib_matn == 43:
                            tartib_matn += 1
                            ll44 = threading.Thread(target=matn_convert.l44, args=(update, context, 'kril',))
                            ll44.start()
                        elif tartib_matn == 44:
                            tartib_matn += 1
                            ll45 = threading.Thread(target=matn_convert.l45, args=(update, context, 'kril',))
                            ll45.start()
                        elif tartib_matn == 45:
                            tartib_matn += 1
                            ll46 = threading.Thread(target=matn_convert.l46, args=(update, context, 'kril',))
                            ll46.start()
                        elif tartib_matn == 46:
                            tartib_matn += 1
                            ll47 = threading.Thread(target=matn_convert.l47, args=(update, context, 'kril',))
                            ll47.start()
                        elif tartib_matn == 47:
                            tartib_matn += 1
                            ll48 = threading.Thread(target=matn_convert.l48, args=(update, context, 'kril',))
                            ll48.start()
                        elif tartib_matn == 48:
                            tartib_matn += 1
                            ll49 = threading.Thread(target=matn_convert.l49, args=(update, context, 'kril',))
                            ll49.start()
                        elif tartib_matn == 49:
                            tartib_matn += 1
                            ll50 = threading.Thread(target=matn_convert.l50, args=(update, context, 'kril',))
                            ll50.start()

                    else:
                        update.message.reply_html("<b>Lotindan</b> ➡️ <b>Kirillga</b> o'tkazish yoki <b>Kirilldan</b> ➡️ <b>Lotinga</b> o'tkazishni tanlang. ",
                            reply_markup=button_replykeyboard)
                else:
                    if prim != '' and yangi != '':
                        update.message.delete()
                        update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                            yangi) + "</b> kanallariga a'zo bo'lmadingiz.",
                                                 reply_markup=button_inlinekeyboard)
                    else:
                        update.message.delete()
                        update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                        yangi) + "</b> kanaliga a'zo bo'lmadingiz.",
                                             reply_markup=button_inlinekeyboard)
                db.set_state(update.message.chat_id, 1)

    except Exception:
        pass


def document(update, context):
    global tartib,Krill,Lotin,Azolik
    try:
        Azolik, prim, yangi = primer.azolikni_tekshirish(update.message.chat_id)
        if Azolik:
            if Lotin :
                if tartib == 100:
                    tartib = 0
                print(tartib)
                if tartib == 0:
                    tartib += 1
                    ll1 = threading.Thread(target=primer.l1, args=(update, context,'lotin',))
                    ll1.start()
                elif tartib == 1:
                    tartib += 1
                    ll2 = threading.Thread(target=primer.l2, args=(update, context,'lotin',))
                    ll2.start()
                elif tartib == 2:
                    tartib += 1
                    ll3 = threading.Thread(target=primer.l3, args=(update, context,'lotin',))
                    ll3.start()
                elif tartib == 3:
                    tartib += 1
                    ll4 = threading.Thread(target=primer.l4, args=(update, context,'lotin',))
                    ll4.start()
                elif tartib == 4:
                    tartib += 1
                    ll5 = threading.Thread(target=primer.l5, args=(update, context,'lotin',))
                    ll5.start()
                elif tartib == 5:
                    tartib += 1
                    ll6 = threading.Thread(target=primer.l6, args=(update, context,'lotin',))
                    ll6.start()
                elif tartib == 6:
                    tartib += 1
                    ll7 = threading.Thread(target=primer.l7, args=(update, context,'lotin',))
                    ll7.start()
                elif tartib == 7:
                    tartib += 1
                    ll8 = threading.Thread(target=primer.l8, args=(update, context,'lotin',))
                    ll8.start()
                elif tartib == 8:
                    tartib += 1
                    ll9 = threading.Thread(target=primer.l9, args=(update, context,'lotin',))
                    ll9.start()
                elif tartib == 9:
                    tartib += 1
                    ll10 = threading.Thread(target=primer.l10, args=(update, context,'lotin',))
                    ll10.start()
                elif tartib == 10:
                    tartib += 1
                    ll11 = threading.Thread(target=primer.l11, args=(update, context,'lotin',))
                    ll11.start()
                elif tartib == 11:
                    tartib += 1
                    ll12 = threading.Thread(target=primer.l12, args=(update, context,'lotin',))
                    ll12.start()
                elif tartib == 12:
                    tartib += 1
                    ll13 = threading.Thread(target=primer.l13, args=(update, context,'lotin',))
                    ll13.start()
                elif tartib == 13:
                    tartib += 1
                    ll14 = threading.Thread(target=primer.l14, args=(update, context,'lotin',))
                    ll14.start()
                elif tartib == 14:
                    tartib += 1
                    ll15 = threading.Thread(target=primer.l15, args=(update, context,'lotin',))
                    ll15.start()
                elif tartib == 15:
                    tartib += 1
                    ll16 = threading.Thread(target=primer.l16, args=(update, context,'lotin',))
                    ll16.start()
                elif tartib == 16:
                    tartib += 1
                    ll17 = threading.Thread(target=primer.l17, args=(update, context,'lotin',))
                    ll17.start()
                elif tartib == 17:
                    tartib += 1
                    ll18 = threading.Thread(target=primer.l18, args=(update, context,'lotin',))
                    ll18.start()
                elif tartib == 18:
                    tartib += 1
                    ll19 = threading.Thread(target=primer.l19, args=(update, context,'lotin',))
                    ll19.start()
                elif tartib == 19:
                    tartib += 1
                    ll20 = threading.Thread(target=primer.l20, args=(update, context,'lotin',))
                    ll20.start()
                elif tartib == 20:
                    tartib += 1
                    ll21 = threading.Thread(target=primer.l21, args=(update, context,'lotin',))
                    ll21.start()
                elif tartib == 21:
                    tartib += 1
                    ll22 = threading.Thread(target=primer.l22, args=(update, context,'lotin',))
                    ll22.start()
                elif tartib == 22:
                    tartib += 1
                    ll23 = threading.Thread(target=primer.l23, args=(update, context,'lotin',))
                    ll23.start()
                elif tartib == 23:
                    tartib += 1
                    ll24 = threading.Thread(target=primer.l24, args=(update, context,'lotin',))
                    ll24.start()
                elif tartib == 24:
                    tartib += 1
                    ll25 = threading.Thread(target=primer.l25, args=(update, context,'lotin',))
                    ll25.start()
                elif tartib == 25:
                    tartib += 1
                    ll26 = threading.Thread(target=primer.l26, args=(update, context,'lotin',))
                    ll26.start()
                elif tartib == 26:
                    tartib += 1
                    ll27 = threading.Thread(target=primer.l27, args=(update, context,'lotin',))
                    ll27.start()
                elif tartib == 27:
                    tartib += 1
                    ll28 = threading.Thread(target=primer.l28, args=(update, context,'lotin',))
                    ll28.start()
                elif tartib == 28:
                    tartib += 1
                    ll29 = threading.Thread(target=primer.l29, args=(update, context,'lotin',))
                    ll29.start()
                elif tartib == 29:
                    tartib += 1
                    ll30 = threading.Thread(target=primer.l30, args=(update, context,'lotin',))
                    ll30.start()
                elif tartib == 30:
                    tartib += 1
                    ll31 = threading.Thread(target=primer.l31, args=(update, context,'lotin',))
                    ll31.start()
                elif tartib == 31:
                    tartib += 1
                    ll32 = threading.Thread(target=primer.l32, args=(update, context,'lotin',))
                    ll32.start()
                elif tartib == 32:
                    tartib += 1
                    ll33 = threading.Thread(target=primer.l33, args=(update, context,'lotin',))
                    ll33.start()
                elif tartib == 33:
                    tartib += 1
                    ll34 = threading.Thread(target=primer.l34, args=(update, context,'lotin',))
                    ll34.start()
                elif tartib == 34:
                    tartib += 1
                    ll35 = threading.Thread(target=primer.l35, args=(update, context,'lotin',))
                    ll35.start()
                elif tartib == 35:
                    tartib += 1
                    ll36 = threading.Thread(target=primer.l36, args=(update, context,'lotin',))
                    ll36.start()
                elif tartib == 36:
                    tartib += 1
                    ll37 = threading.Thread(target=primer.l37, args=(update, context,'lotin',))
                    ll37.start()
                elif tartib == 37:
                    tartib += 1
                    ll38 = threading.Thread(target=primer.l38, args=(update, context,'lotin',))
                    ll38.start()
                elif tartib == 38:
                    tartib += 1
                    ll39 = threading.Thread(target=primer.l39, args=(update, context,'lotin',))
                    ll39.start()
                elif tartib == 39:
                    tartib += 1
                    ll40 = threading.Thread(target=primer.l40, args=(update, context,'lotin',))
                    ll40.start()
                elif tartib == 40:
                    tartib += 1
                    ll41 = threading.Thread(target=primer.l41, args=(update, context,'lotin',))
                    ll41.start()
                elif tartib == 41:
                    tartib += 1
                    ll42 = threading.Thread(target=primer.l42, args=(update, context,'lotin',))
                    ll42.start()
                elif tartib == 42:
                    tartib += 1
                    ll43 = threading.Thread(target=primer.l43, args=(update, context,'lotin',))
                    ll43.start()
                elif tartib == 43:
                    tartib += 1
                    ll44 = threading.Thread(target=primer.l44, args=(update, context,'lotin',))
                    ll44.start()
                elif tartib == 44:
                    tartib += 1
                    ll45 = threading.Thread(target=primer.l45, args=(update, context,'lotin',))
                    ll45.start()
                elif tartib == 45:
                    tartib += 1
                    ll46 = threading.Thread(target=primer.l46, args=(update, context,'lotin',))
                    ll46.start()
                elif tartib == 46:
                    tartib += 1
                    ll47 = threading.Thread(target=primer.l47, args=(update, context,'lotin',))
                    ll47.start()
                elif tartib == 47:
                    tartib += 1
                    ll48 = threading.Thread(target=primer.l48, args=(update, context,'lotin',))
                    ll48.start()
                elif tartib == 48:
                    tartib += 1
                    ll49 = threading.Thread(target=primer.l49, args=(update, context,'lotin',))
                    ll49.start()
                elif tartib == 49:
                    tartib += 1
                    ll50 = threading.Thread(target=primer.l50, args=(update, context,'lotin',))
                    ll50.start()
                elif tartib == 50:
                    tartib += 1
                    ll51 = threading.Thread(target=primer.l51, args=(update, context,'lotin',))
                    ll51.start()
                elif tartib == 51:
                    tartib += 1
                    ll52 = threading.Thread(target=primer.l52, args=(update, context,'lotin',))
                    ll52.start()
                elif tartib == 52:
                    tartib += 1
                    ll53 = threading.Thread(target=primer.l53, args=(update, context,'lotin',))
                    ll53.start()
                elif tartib == 53:
                    tartib += 1
                    ll54 = threading.Thread(target=primer.l54, args=(update, context,'lotin',))
                    ll54.start()
                elif tartib == 54:
                    tartib += 1
                    ll55 = threading.Thread(target=primer.l55, args=(update, context,'lotin',))
                    ll55.start()
                elif tartib == 55:
                    tartib += 1
                    ll56 = threading.Thread(target=primer.l56, args=(update, context,'lotin',))
                    ll56.start()
                elif tartib == 56:
                    tartib += 1
                    ll57 = threading.Thread(target=primer.l57, args=(update, context,'lotin',))
                    ll57.start()
                elif tartib == 57:
                    tartib += 1
                    ll58 = threading.Thread(target=primer.l58, args=(update, context,'lotin',))
                    ll58.start()
                elif tartib == 58:
                    tartib += 1
                    ll59 = threading.Thread(target=primer.l59, args=(update, context,'lotin',))
                    ll59.start()
                elif tartib == 59:
                    tartib += 1
                    ll60 = threading.Thread(target=primer.l60, args=(update, context,'lotin',))
                    ll60.start()
                elif tartib == 60:
                    tartib += 1
                    ll61 = threading.Thread(target=primer.l61, args=(update, context,'lotin',))
                    ll61.start()
                elif tartib == 61:
                    tartib += 1
                    ll62 = threading.Thread(target=primer.l62, args=(update, context,'lotin',))
                    ll62.start()
                elif tartib == 62:
                    tartib += 1
                    ll63 = threading.Thread(target=primer.l63, args=(update, context,'lotin',))
                    ll63.start()
                elif tartib == 63:
                    tartib += 1
                    ll64 = threading.Thread(target=primer.l64, args=(update, context,'lotin',))
                    ll64.start()
                elif tartib == 64:
                    tartib += 1
                    ll65 = threading.Thread(target=primer.l65, args=(update, context,'lotin',))
                    ll65.start()
                elif tartib == 65:
                    tartib += 1
                    ll66 = threading.Thread(target=primer.l66, args=(update, context,'lotin',))
                    ll66.start()
                elif tartib == 66:
                    tartib += 1
                    ll67 = threading.Thread(target=primer.l67, args=(update, context,'lotin',))
                    ll67.start()
                elif tartib == 67:
                    tartib += 1
                    ll68 = threading.Thread(target=primer.l68, args=(update, context,'lotin',))
                    ll68.start()
                elif tartib == 68:
                    tartib += 1
                    ll69 = threading.Thread(target=primer.l69, args=(update, context,'lotin',))
                    ll69.start()
                elif tartib == 69:
                    tartib += 1
                    ll70 = threading.Thread(target=primer.l70, args=(update, context,'lotin',))
                    ll70.start()
                elif tartib == 70:
                    tartib += 1
                    ll71 = threading.Thread(target=primer.l71, args=(update, context,'lotin',))
                    ll71.start()
                elif tartib == 71:
                    tartib += 1
                    ll72 = threading.Thread(target=primer.l72, args=(update, context,'lotin',))
                    ll72.start()
                elif tartib == 72:
                    tartib += 1
                    ll73 = threading.Thread(target=primer.l73, args=(update, context,'lotin',))
                    ll73.start()
                elif tartib == 73:
                    tartib += 1
                    ll74 = threading.Thread(target=primer.l74, args=(update, context,'lotin',))
                    ll74.start()
                elif tartib == 74:
                    tartib += 1
                    ll75 = threading.Thread(target=primer.l75, args=(update, context,'lotin',))
                    ll75.start()
                elif tartib == 75:
                    tartib += 1
                    ll76 = threading.Thread(target=primer.l76, args=(update, context,'lotin',))
                    ll76.start()
                elif tartib == 76:
                    tartib += 1
                    ll77 = threading.Thread(target=primer.l77, args=(update, context,'lotin',))
                    ll77.start()
                elif tartib == 77:
                    tartib += 1
                    ll78 = threading.Thread(target=primer.l78, args=(update, context,'lotin',))
                    ll78.start()
                elif tartib == 78:
                    tartib += 1
                    ll79 = threading.Thread(target=primer.l79, args=(update, context,'lotin',))
                    ll79.start()
                elif tartib == 79:
                    tartib += 1
                    ll80 = threading.Thread(target=primer.l80, args=(update, context,'lotin',))
                    ll80.start()
                elif tartib == 80:
                    tartib += 1
                    ll81 = threading.Thread(target=primer.l81, args=(update, context,'lotin',))
                    ll81.start()
                elif tartib == 81:
                    tartib += 1
                    ll82 = threading.Thread(target=primer.l82, args=(update, context,'lotin',))
                    ll82.start()
                elif tartib == 82:
                    tartib += 1
                    ll83 = threading.Thread(target=primer.l83, args=(update, context,'lotin',))
                    ll83.start()
                elif tartib == 83:
                    tartib += 1
                    ll84 = threading.Thread(target=primer.l84, args=(update, context,'lotin',))
                    ll84.start()
                elif tartib == 84:
                    tartib += 1
                    ll85 = threading.Thread(target=primer.l85, args=(update, context,'lotin',))
                    ll85.start()
                elif tartib == 85:
                    tartib += 1
                    ll86 = threading.Thread(target=primer.l86, args=(update, context,'lotin',))
                    ll86.start()
                elif tartib == 86:
                    tartib += 1
                    ll87 = threading.Thread(target=primer.l87, args=(update, context,'lotin',))
                    ll87.start()
                elif tartib == 87:
                    tartib += 1
                    ll88 = threading.Thread(target=primer.l88, args=(update, context,'lotin',))
                    ll88.start()
                elif tartib == 88:
                    tartib += 1
                    ll89 = threading.Thread(target=primer.l89, args=(update, context,'lotin',))
                    ll89.start()
                elif tartib == 89:
                    tartib += 1
                    ll90 = threading.Thread(target=primer.l90, args=(update, context,'lotin',))
                    ll90.start()
                elif tartib == 90:
                    tartib += 1
                    ll91 = threading.Thread(target=primer.l91, args=(update, context,'lotin',))
                    ll91.start()
                elif tartib == 91:
                    tartib += 1
                    ll92 = threading.Thread(target=primer.l92, args=(update, context,'lotin',))
                    ll92.start()
                elif tartib == 92:
                    tartib += 1
                    ll93 = threading.Thread(target=primer.l93, args=(update, context,'lotin',))
                    ll93.start()
                elif tartib == 93:
                    tartib += 1
                    ll94 = threading.Thread(target=primer.l94, args=(update, context,'lotin',))
                    ll94.start()
                elif tartib == 94:
                    tartib += 1
                    ll95 = threading.Thread(target=primer.l95, args=(update, context,'lotin',))
                    ll95.start()
                elif tartib == 95:
                    tartib += 1
                    ll96 = threading.Thread(target=primer.l96, args=(update, context,'lotin',))
                    ll96.start()
                elif tartib == 96:
                    tartib += 1
                    ll97 = threading.Thread(target=primer.l97, args=(update, context,'lotin',))
                    ll97.start()
                elif tartib == 97:
                    tartib += 1
                    ll98 = threading.Thread(target=primer.l98, args=(update, context,'lotin',))
                    ll98.start()
                elif tartib == 98:
                    tartib += 1
                    ll99 = threading.Thread(target=primer.l99, args=(update, context,'lotin',))
                    ll99.start()
                elif tartib == 99:
                    tartib += 1
                    ll100 = threading.Thread(target=primer.l100, args=(update, context,'lotin',))
                    ll100.start()
            elif Krill:
                if tartib == 100:
                    tartib = 0
                print(tartib)
                if tartib == 0:
                    tartib += 1
                    ll1 = threading.Thread(target=primer.l1, args=(update, context, 'kril',))
                    ll1.start()
                elif tartib == 1:
                    tartib += 1
                    ll2 = threading.Thread(target=primer.l2, args=(update, context,'kril',))
                    ll2.start()
                elif tartib == 2:
                    tartib += 1
                    ll3 = threading.Thread(target=primer.l3, args=(update, context,'kril',))
                    ll3.start()
                elif tartib == 3:
                    tartib += 1
                    ll4 = threading.Thread(target=primer.l4, args=(update, context,'kril',))
                    ll4.start()
                elif tartib == 4:
                    tartib += 1
                    ll5 = threading.Thread(target=primer.l5, args=(update, context,'kril',))
                    ll5.start()
                elif tartib == 5:
                    tartib += 1
                    ll6 = threading.Thread(target=primer.l6, args=(update, context,'kril',))
                    ll6.start()
                elif tartib == 6:
                    tartib += 1
                    ll7 = threading.Thread(target=primer.l7, args=(update, context,'kril',))
                    ll7.start()
                elif tartib == 7:
                    tartib += 1
                    ll8 = threading.Thread(target=primer.l8, args=(update, context,'kril',))
                    ll8.start()
                elif tartib == 8:
                    tartib += 1
                    ll9 = threading.Thread(target=primer.l9, args=(update, context,'kril',))
                    ll9.start()
                elif tartib == 9:
                    tartib += 1
                    ll10 = threading.Thread(target=primer.l10, args=(update, context,'kril',))
                    ll10.start()
                elif tartib == 10:
                    tartib += 1
                    ll11 = threading.Thread(target=primer.l11, args=(update, context,'kril',))
                    ll11.start()
                elif tartib == 11:
                    tartib += 1
                    ll12 = threading.Thread(target=primer.l12, args=(update, context,'kril',))
                    ll12.start()
                elif tartib == 12:
                    tartib += 1
                    ll13 = threading.Thread(target=primer.l13, args=(update, context,'kril',))
                    ll13.start()
                elif tartib == 13:
                    tartib += 1
                    ll14 = threading.Thread(target=primer.l14, args=(update, context,'kril',))
                    ll14.start()
                elif tartib == 14:
                    tartib += 1
                    ll15 = threading.Thread(target=primer.l15, args=(update, context,'kril',))
                    ll15.start()
                elif tartib == 15:
                    tartib += 1
                    ll16 = threading.Thread(target=primer.l16, args=(update, context,'kril',))
                    ll16.start()
                elif tartib == 16:
                    tartib += 1
                    ll17 = threading.Thread(target=primer.l17, args=(update, context,'kril',))
                    ll17.start()
                elif tartib == 17:
                    tartib += 1
                    ll18 = threading.Thread(target=primer.l18, args=(update, context,'kril',))
                    ll18.start()
                elif tartib == 18:
                    tartib += 1
                    ll19 = threading.Thread(target=primer.l19, args=(update, context,'kril',))
                    ll19.start()
                elif tartib == 19:
                    tartib += 1
                    ll20 = threading.Thread(target=primer.l20, args=(update, context,'kril',))
                    ll20.start()
                elif tartib == 20:
                    tartib += 1
                    ll21 = threading.Thread(target=primer.l21, args=(update, context,'kril',))
                    ll21.start()
                elif tartib == 21:
                    tartib += 1
                    ll22 = threading.Thread(target=primer.l22, args=(update, context,'kril',))
                    ll22.start()
                elif tartib == 22:
                    tartib += 1
                    ll23 = threading.Thread(target=primer.l23, args=(update, context,'kril',))
                    ll23.start()
                elif tartib == 23:
                    tartib += 1
                    ll24 = threading.Thread(target=primer.l24, args=(update, context,'kril',))
                    ll24.start()
                elif tartib == 24:
                    tartib += 1
                    ll25 = threading.Thread(target=primer.l25, args=(update, context,'kril',))
                    ll25.start()
                elif tartib == 25:
                    tartib += 1
                    ll26 = threading.Thread(target=primer.l26, args=(update, context,'kril',))
                    ll26.start()
                elif tartib == 26:
                    tartib += 1
                    ll27 = threading.Thread(target=primer.l27, args=(update, context,'kril',))
                    ll27.start()
                elif tartib == 27:
                    tartib += 1
                    ll28 = threading.Thread(target=primer.l28, args=(update, context,'kril',))
                    ll28.start()
                elif tartib == 28:
                    tartib += 1
                    ll29 = threading.Thread(target=primer.l29, args=(update, context,'kril',))
                    ll29.start()
                elif tartib == 29:
                    tartib += 1
                    ll30 = threading.Thread(target=primer.l30, args=(update, context,'kril',))
                    ll30.start()
                elif tartib == 30:
                    tartib += 1
                    ll31 = threading.Thread(target=primer.l31, args=(update, context,'kril',))
                    ll31.start()
                elif tartib == 31:
                    tartib += 1
                    ll32 = threading.Thread(target=primer.l32, args=(update, context,'kril',))
                    ll32.start()
                elif tartib == 32:
                    tartib += 1
                    ll33 = threading.Thread(target=primer.l33, args=(update, context,'kril',))
                    ll33.start()
                elif tartib == 33:
                    tartib += 1
                    ll34 = threading.Thread(target=primer.l34, args=(update, context,'kril',))
                    ll34.start()
                elif tartib == 34:
                    tartib += 1
                    ll35 = threading.Thread(target=primer.l35, args=(update, context,'kril',))
                    ll35.start()
                elif tartib == 35:
                    tartib += 1
                    ll36 = threading.Thread(target=primer.l36, args=(update, context,'kril',))
                    ll36.start()
                elif tartib == 36:
                    tartib += 1
                    ll37 = threading.Thread(target=primer.l37, args=(update, context,'kril',))
                    ll37.start()
                elif tartib == 37:
                    tartib += 1
                    ll38 = threading.Thread(target=primer.l38, args=(update, context,'kril',))
                    ll38.start()
                elif tartib == 38:
                    tartib += 1
                    ll39 = threading.Thread(target=primer.l39, args=(update, context,'kril',))
                    ll39.start()
                elif tartib == 39:
                    tartib += 1
                    ll40 = threading.Thread(target=primer.l40, args=(update, context,'kril',))
                    ll40.start()
                elif tartib == 40:
                    tartib += 1
                    ll41 = threading.Thread(target=primer.l41, args=(update, context,'kril',))
                    ll41.start()
                elif tartib == 41:
                    tartib += 1
                    ll42 = threading.Thread(target=primer.l42, args=(update, context,'kril',))
                    ll42.start()
                elif tartib == 42:
                    tartib += 1
                    ll43 = threading.Thread(target=primer.l43, args=(update, context,'kril',))
                    ll43.start()
                elif tartib == 43:
                    tartib += 1
                    ll44 = threading.Thread(target=primer.l44, args=(update, context,'kril',))
                    ll44.start()
                elif tartib == 44:
                    tartib += 1
                    ll45 = threading.Thread(target=primer.l45, args=(update, context,'kril',))
                    ll45.start()
                elif tartib == 45:
                    tartib += 1
                    ll46 = threading.Thread(target=primer.l46, args=(update, context,'kril',))
                    ll46.start()
                elif tartib == 46:
                    tartib += 1
                    ll47 = threading.Thread(target=primer.l47, args=(update, context,'kril',))
                    ll47.start()
                elif tartib == 47:
                    tartib += 1
                    ll48 = threading.Thread(target=primer.l48, args=(update, context,'kril',))
                    ll48.start()
                elif tartib == 48:
                    tartib += 1
                    ll49 = threading.Thread(target=primer.l49, args=(update, context,'kril',))
                    ll49.start()
                elif tartib == 49:
                    tartib += 1
                    ll50 = threading.Thread(target=primer.l50, args=(update, context,'kril',))
                    ll50.start()
                elif tartib == 50:
                    tartib += 1
                    ll51 = threading.Thread(target=primer.l51, args=(update, context,'kril',))
                    ll51.start()
                elif tartib == 51:
                    tartib += 1
                    ll52 = threading.Thread(target=primer.l52, args=(update, context,'kril',))
                    ll52.start()
                elif tartib == 52:
                    tartib += 1
                    ll53 = threading.Thread(target=primer.l53, args=(update, context,'kril',))
                    ll53.start()
                elif tartib == 53:
                    tartib += 1
                    ll54 = threading.Thread(target=primer.l54, args=(update, context,'kril',))
                    ll54.start()
                elif tartib == 54:
                    tartib += 1
                    ll55 = threading.Thread(target=primer.l55, args=(update, context,'kril',))
                    ll55.start()
                elif tartib == 55:
                    tartib += 1
                    ll56 = threading.Thread(target=primer.l56, args=(update, context,'kril',))
                    ll56.start()
                elif tartib == 56:
                    tartib += 1
                    ll57 = threading.Thread(target=primer.l57, args=(update, context,'kril',))
                    ll57.start()
                elif tartib == 57:
                    tartib += 1
                    ll58 = threading.Thread(target=primer.l58, args=(update, context,'kril',))
                    ll58.start()
                elif tartib == 58:
                    tartib += 1
                    ll59 = threading.Thread(target=primer.l59, args=(update, context,'kril',))
                    ll59.start()
                elif tartib == 59:
                    tartib += 1
                    ll60 = threading.Thread(target=primer.l60, args=(update, context,'kril',))
                    ll60.start()
                elif tartib == 60:
                    tartib += 1
                    ll61 = threading.Thread(target=primer.l61, args=(update, context,'kril',))
                    ll61.start()
                elif tartib == 61:
                    tartib += 1
                    ll62 = threading.Thread(target=primer.l62, args=(update, context,'kril',))
                    ll62.start()
                elif tartib == 62:
                    tartib += 1
                    ll63 = threading.Thread(target=primer.l63, args=(update, context,'kril',))
                    ll63.start()
                elif tartib == 63:
                    tartib += 1
                    ll64 = threading.Thread(target=primer.l64, args=(update, context,'kril',))
                    ll64.start()
                elif tartib == 64:
                    tartib += 1
                    ll65 = threading.Thread(target=primer.l65, args=(update, context,'kril',))
                    ll65.start()
                elif tartib == 65:
                    tartib += 1
                    ll66 = threading.Thread(target=primer.l66, args=(update, context,'kril',))
                    ll66.start()
                elif tartib == 66:
                    tartib += 1
                    ll67 = threading.Thread(target=primer.l67, args=(update, context,'kril',))
                    ll67.start()
                elif tartib == 67:
                    tartib += 1
                    ll68 = threading.Thread(target=primer.l68, args=(update, context,'kril',))
                    ll68.start()
                elif tartib == 68:
                    tartib += 1
                    ll69 = threading.Thread(target=primer.l69, args=(update, context,'kril',))
                    ll69.start()
                elif tartib == 69:
                    tartib += 1
                    ll70 = threading.Thread(target=primer.l70, args=(update, context,'kril',))
                    ll70.start()
                elif tartib == 70:
                    tartib += 1
                    ll71 = threading.Thread(target=primer.l71, args=(update, context,'kril',))
                    ll71.start()
                elif tartib == 71:
                    tartib += 1
                    ll72 = threading.Thread(target=primer.l72, args=(update, context,'kril',))
                    ll72.start()
                elif tartib == 72:
                    tartib += 1
                    ll73 = threading.Thread(target=primer.l73, args=(update, context,'kril',))
                    ll73.start()
                elif tartib == 73:
                    tartib += 1
                    ll74 = threading.Thread(target=primer.l74, args=(update, context,'kril',))
                    ll74.start()
                elif tartib == 74:
                    tartib += 1
                    ll75 = threading.Thread(target=primer.l75, args=(update, context,'kril',))
                    ll75.start()
                elif tartib == 75:
                    tartib += 1
                    ll76 = threading.Thread(target=primer.l76, args=(update, context,'kril',))
                    ll76.start()
                elif tartib == 76:
                    tartib += 1
                    ll77 = threading.Thread(target=primer.l77, args=(update, context,'kril',))
                    ll77.start()
                elif tartib == 77:
                    tartib += 1
                    ll78 = threading.Thread(target=primer.l78, args=(update, context,'kril',))
                    ll78.start()
                elif tartib == 78:
                    tartib += 1
                    ll79 = threading.Thread(target=primer.l79, args=(update, context,'kril',))
                    ll79.start()
                elif tartib == 79:
                    tartib += 1
                    ll80 = threading.Thread(target=primer.l80, args=(update, context,'kril',))
                    ll80.start()
                elif tartib == 80:
                    tartib += 1
                    ll81 = threading.Thread(target=primer.l81, args=(update, context,'kril',))
                    ll81.start()
                elif tartib == 81:
                    tartib += 1
                    ll82 = threading.Thread(target=primer.l82, args=(update, context,'kril',))
                    ll82.start()
                elif tartib == 82:
                    tartib += 1
                    ll83 = threading.Thread(target=primer.l83, args=(update, context,'kril',))
                    ll83.start()
                elif tartib == 83:
                    tartib += 1
                    ll84 = threading.Thread(target=primer.l84, args=(update, context,'kril',))
                    ll84.start()
                elif tartib == 84:
                    tartib += 1
                    ll85 = threading.Thread(target=primer.l85, args=(update, context,'kril',))
                    ll85.start()
                elif tartib == 85:
                    tartib += 1
                    ll86 = threading.Thread(target=primer.l86, args=(update, context,'kril',))
                    ll86.start()
                elif tartib == 86:
                    tartib += 1
                    ll87 = threading.Thread(target=primer.l87, args=(update, context,'kril',))
                    ll87.start()
                elif tartib == 87:
                    tartib += 1
                    ll88 = threading.Thread(target=primer.l88, args=(update, context,'kril',))
                    ll88.start()
                elif tartib == 88:
                    tartib += 1
                    ll89 = threading.Thread(target=primer.l89, args=(update, context,'kril',))
                    ll89.start()
                elif tartib == 89:
                    tartib += 1
                    ll90 = threading.Thread(target=primer.l90, args=(update, context,'kril',))
                    ll90.start()
                elif tartib == 90:
                    tartib += 1
                    ll91 = threading.Thread(target=primer.l91, args=(update, context,'kril',))
                    ll91.start()
                elif tartib == 91:
                    tartib += 1
                    ll92 = threading.Thread(target=primer.l92, args=(update, context,'kril',))
                    ll92.start()
                elif tartib == 92:
                    tartib += 1
                    ll93 = threading.Thread(target=primer.l93, args=(update, context,'kril',))
                    ll93.start()
                elif tartib == 93:
                    tartib += 1
                    ll94 = threading.Thread(target=primer.l94, args=(update, context,'kril',))
                    ll94.start()
                elif tartib == 94:
                    tartib += 1
                    ll95 = threading.Thread(target=primer.l95, args=(update, context,'kril',))
                    ll95.start()
                elif tartib == 95:
                    tartib += 1
                    ll96 = threading.Thread(target=primer.l96, args=(update, context,'kril',))
                    ll96.start()
                elif tartib == 96:
                    tartib += 1
                    ll97 = threading.Thread(target=primer.l97, args=(update, context,'kril',))
                    ll97.start()
                elif tartib == 97:
                    tartib += 1
                    ll98 = threading.Thread(target=primer.l98, args=(update, context,'kril',))
                    ll98.start()
                elif tartib == 98:
                    tartib += 1
                    ll99 = threading.Thread(target=primer.l99, args=(update, context,'kril',))
                    ll99.start()
                elif tartib == 99:
                    tartib += 1
                    ll100 = threading.Thread(target=primer.l100, args=(update, context,'kril',))
                    ll100.start()

            else:
                update.message.reply_html(
                    "<b>Lotindan</b> ➡️ <b>Kirillga</b> o'tkazish yoki <b>Kirilldan</b> ➡️ <b>Lotinga</b> o'tkazishni tanlang. ",
                    reply_markup=button_replykeyboard)
        else:
            if prim != '' and yangi != '':
                update.message.delete()
                update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                    yangi) + "</b> kanallariga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
            else:
                update.message.delete()
                update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                    yangi) + "</b> kanaliga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
            db.set_state(update.message.chat_id, 1)

    except Exception as ex:
        pass


def kril(update, context):
    try:
        global Krill,Lotin,Azolik
        Azolik, prim, yangi = primer.azolikni_tekshirish(update.message.chat_id)
        if Azolik:
            Lotin = True
            Krill=False
            custom_keyboard = [["Lotin ✅ Kirill", "Kirill ➡ Lotin"]]
            button_replykeyboard = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            update.message.reply_html("<b>Lotindan</b> ➡️ <b>Kirillga</b> o'tkaziladigan <b>Matn</b> yoki <b>.docx</b>, "
                                      " <b>.doc</b>, <b>.xlsx</b>, <b>.xls</b> fayllarini yuborishingiz mumkin. ",reply_markup = button_replykeyboard)
        else:
            if prim != '' and yangi != '':
                update.message.delete()
                update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                    yangi) + "</b> kanallariga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
            else:
                update.message.delete()
                update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                    yangi) + "</b> kanaliga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
            db.set_state(update.message.chat_id, 1)


    except Exception:
        pass
def lotin(update, context):
    try:
        global Krill,Lotin,Azolik
        Azolik, prim, yangi = primer.azolikni_tekshirish(update.message.chat_id)
        if Azolik:
            Krill=True
            Lotin=False
            custom_keyboard = [["Lotin ➡ Kirill", "Kirill ✅ Lotin"]]
            button_replykeyboard = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
            update.message.reply_html("<b>Kirilldan</b> ➡️ <b>Lotinga</b> o'tkaziladigan <b>Matn</b> yoki <b>.docx</b>, "
                                      " <b>.doc</b>, <b>.xlsx</b>, <b>.xls</b> fayllarini yuborishingiz mumkin. ", reply_markup = button_replykeyboard)
        else:
            if prim != '' and yangi != '':
                update.message.delete()
                update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                    yangi) + "</b> kanallariga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
            else:
                update.message.delete()
                update.message.reply_html("❗️❗️❗️Siz quydagi " + "<b>" + str(prim) + "</b> " + " <b>" + str(
                    yangi) + "</b> kanaliga a'zo bo'lmadingiz.",
                                         reply_markup=button_inlinekeyboard)
            db.set_state(update.message.chat_id, 1)


    except Exception:
        pass

def main():
    try:
        updater = Updater('')

        start_handler = CommandHandler('start', start)
        xato_handler = CommandHandler('xato', xato)
        doc_handler = MessageHandler(Filters.document, document)
        text_handler = MessageHandler(Filters.text, text)
        tekshir = CallbackQueryHandler(tekshirish)

        updater.dispatcher.add_handler(start_handler)
        updater.dispatcher.add_handler(xato_handler)
        updater.dispatcher.add_handler(doc_handler)
        updater.dispatcher.add_handler(text_handler)
        updater.dispatcher.add_handler(tekshir)

        updater.start_polling()
        updater.idle()
    except Exception:
        pass


if __name__ == '__main__':
    main()