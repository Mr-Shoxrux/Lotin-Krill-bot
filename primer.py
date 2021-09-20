import os
def l1(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l2(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l3(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l4(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l5(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l6(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l7(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l8(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l9(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l10(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l11(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l12(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l13(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l14(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l15(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l16(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l17(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l18(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l19(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l20(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l21(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l22(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l23(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l24(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l25(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l26(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l27(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l28(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l29(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l30(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l31(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l32(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l33(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l34(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l35(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l36(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l37(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l38(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l39(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l40(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l41(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l42(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l43(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l44(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l45(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l46(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l47(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l48(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l49(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l50(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l51(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l52(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l53(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l54(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l55(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l56(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l57(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l58(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l59(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l60(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l61(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l62(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l63(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l64(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l65(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l66(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l67(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l68(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l69(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l70(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l71(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l72(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l73(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l74(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l75(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l76(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l77(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l78(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l79(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l80(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l81(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l82(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l83(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l84(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l85(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l86(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l87(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l88(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l89(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l90(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l91(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l92(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l93(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l94(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l95(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l96(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l97(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l98(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l99(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

def l100(update,context,tur):
    try:
        chat_id = update.message.chat_id
        dirName = 'Input/' + str(chat_id)
        dirName1 = 'Output/' + str(chat_id)
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        try:
            os.mkdir(dirName1)
        except FileExistsError:
            pass
        file_name = str(update.message.document['file_name'])
        if file_name.endswith('.docx') or file_name.endswith('.doc') or file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            update.message.reply_html('Biroz kuting. Jarayon davom etmoqda...')
            lis = file_name.split()
            satr = ''
            for i in lis:
                satr += i
            path = dirName + '/' + satr
            with open(path, 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
            dastur = "Convertor_cril_lotin.exe"
            index = ''
            for i in range(len(file_name)):
                if file_name[i] == ' ':
                    index += str(i) + '_'
            path = path+'/'+index+'/'+tur
            os.system(dastur + " " + path)

            document_path = dirName1 + '/' + file_name
            if tur =='lotin':
                context.bot.sendDocument(chat_id=chat_id,
                                     caption="Lotindan  ➡️ Kirillga o'tkazilgan faylingiz. ",
                                     document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
            else:
                context.bot.sendDocument(chat_id=chat_id,
                                         caption="Kirilldan  ➡️ Lotinga o'tkazilgan faylingiz. ",
                                         document=open(document_path, 'rb'))
                try:
                    os.remove(dirName + '/' + satr)
                    os.remove(dirName1 + '/' + file_name)
                except OSError as e:
                    pass
        else:
            context.bot.send_message(chat_id=chat_id, text="Bizga faqat .doc, .docx, .xls, .xlsx formatidagi fayl jo'nating.")
    except Exception:
        pass

