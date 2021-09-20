import pandas as pd
def l1(update,context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ', header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])

            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l2(update,context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l3(update,context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l4(update,context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l5(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l6(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l7(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l8(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l9(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l10(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l11(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l12(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l13(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l14(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l15(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l16(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l17(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l18(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l19(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l20(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l21(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l22(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l23(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l24(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l25(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l26(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l27(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l28(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l29(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l30(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l31(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l32(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l33(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l34(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l35(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l36(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l37(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l38(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l39(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l40(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l41(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l42(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l43(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l44(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l45(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l46(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l47(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l48(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l49(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

def l50(update, context,tur):
    try:
        get_text = update.message.to_dict()['text']
        chat_id = update.message.chat_id
        if tur =='lotin':
            dictionary=pd.read_csv('Lugat/lotin_kril.txt',sep=' ',header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i,0],dictionary.iloc[i,1])
            context.bot.send_message(chat_id=chat_id, text=get_text)

        else:
            dictionary = pd.read_csv('Lugat/kril_lotin.txt', sep=' ',
                                     header=None)
            for i in range(dictionary.shape[0]):
                get_text = get_text.replace(dictionary.iloc[i, 0], dictionary.iloc[i, 1])
            context.bot.send_message(chat_id=chat_id, text=get_text)
    except Exception as ex:
        print(ex)

