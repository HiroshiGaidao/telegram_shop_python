import db, telebot, config, threading, time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(config.token)


def mess_from_user(id):
    try:
        state = str(db.user.check(id)[0])
        db.user.change_state(id, state+'|'+'Null')
    except Exception as _ex:
        print("mess_from_user", _ex)
        pass


def mess_editor(id, m_id):
    try:
        state = str(db.user.check(id)[0])
        db.user.change_state(id, state+'|'+str(m_id))
    except Exception as _ex:
        print('mess_editor', _ex)
        pass


def mess_state(id):
    try:
        state = str(db.user.check(id)[1])
        print(state)
        return state
    except IndexError as _ex:
        print(_ex)
        mess_from_user(id)
        return mess_state(id)
    except Exception as _ex:
        print('[MeSS STATE]', _ex)


def user_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Вернуться к покупкам", callback_data="market"))
    markup.add(InlineKeyboardButton("Изменить телефон", callback_data="phone"),InlineKeyboardButton("Изменить ФИО", callback_data="full_name"),InlineKeyboardButton("Изменить адрес", callback_data="address"))
    markup.add(InlineKeyboardButton("Заполнить данные заного", callback_data="registration"))
    return markup


def category_markup():
    cat, _ = db.len_upd()
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for i in cat:
        markup.add(InlineKeyboardButton(str(db.parse(0, int(i))), callback_data=(int(i))))
    if cat == []:
        return "None"
    else:
        return markup


def sub_category_markup(category_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    ids = db.parse(2, category_id)
    for i in ids:
        markup.add(InlineKeyboardButton(db.parse(1, int(i)), callback_data=('prod' + str(i))))
    markup.add(InlineKeyboardButton('Назад', callback_data=f"back|0"))
    return markup

def product_markup(sub_category_id, page = 0):
    ids = db.parse(3, sub_category_id)
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    print(db.parse(5, sub_category_id))
    for i in range(len(ids[page])):
        markup.add(InlineKeyboardButton(f"{i+1}. " + db.parse(4, int(ids[page][i])), callback_data=(f'product_card{ids[page][i]}')))
    markup.add(InlineKeyboardButton('<', callback_data=f'{page}|<|{sub_category_id}'), InlineKeyboardButton(f'{page + 1}/{len(ids)}', callback_data='qqqqq'), InlineKeyboardButton('>', callback_data=f'{page}|>|{sub_category_id}|{len(ids)}'))
    markup.add(InlineKeyboardButton('Назад', callback_data=f"back|{sub_category_id}"))
    markup.add(InlineKeyboardButton('К категориям', callback_data=f"back|0"))
    return markup


#                Карточка товара
# Принимает в себя ID товара и ID пользователя и генерирует сообщение на выходе
# Содержание сообщения: Фотография, название, описание, количество на складе, цена
# Кнопки: < 0/количество > добавить в корзину, назад, к категориям
def product_card(from_id, prod_id):
    pass


if __name__ == '__main__':
    print("System started, init DB")
    db.create_db()
    print("DB ready")


    @bot.message_handler(commands=['user'])
    def message_handler(message):
        mess_from_user(message.chat.id)
        try:
            phone, name, addr = db.user.info(message.chat.id)
            bot.send_message(message.chat.id,
                             f"Ваш идентификатор: {message.chat.id}\nВаше ФИО: {name}\nВаш номер телефона: {phone}\nВаш адрес: {addr}",
                             reply_markup=user_markup())

        except TypeError:
            db.user.add(message.chat.id, None, None, 11)
            db.user.change_state(message.chat.id, 11)
            bot.send_message(message.chat.id,
                             "Для исползования бота, пожалуйста зарегистрируйтесь, в дальнейшем эти данные будут использованы для отправки покупок и обратной связи. \n\nВведите ваш номер телефона:")


    @bot.message_handler(commands=['start'])
    def message_handler(message):
        try:
            db.user.check(message.chat.id)[0]
        except:
            db.user.add(message.chat.id, None, None, 11)
#        print(db.user.check(message.chat.id))
        if db.user.check(message.chat.id)[0] == '21':
            try:
                back = bot.send_message(message.chat.id, "Для просмотра товаров выберите одну из категорий: ",
                             reply_markup=category_markup())
                mess_editor(message.chat.id, back.message_id)
            except TypeError as _ex:
                print(_ex)
        else:
            db.user.change_state(message.chat.id, 11)
            bot.send_message(message.chat.id,
                             "Для исползования бота, пожалуйста зарегистрируйтесь, в дальнейшем эти данные будут использованы для отправки покупок и обратной связи. \n\nВведите ваш номер телефона:")




    @bot.message_handler(func=lambda message: True)
    def massage_loop(message):
        # Работа с сообщениями от пользователя создана для изменения персональных данных
        mess_from_user(message.chat.id)
        if db.user.check(message.chat.id)[0] == '11':
            db.user.change_state(message.chat.id, 12)
            db.user.update.phone(message.chat.id, message.text)
            bot.send_message(message.chat.id, "Введите ваше ФИО")
        elif db.user.check(message.chat.id)[0] == '12':
            db.user.change_state(message.chat.id, 13)
            db.user.update.FIO(message.chat.id, message.text)
            bot.send_message(message.chat.id, "Введите адресс для получения покупок\n\nПример: 123456 Самарская область, г.Сызрань, ул. Пушкина, д.1, кв. 1")
        elif db.user.check(message.chat.id)[0] == '13':
            db.user.change_state(message.chat.id, 21)
            db.user.update.addr(message.chat.id, message.text)
            bot.send_message(message.chat.id, "Данные сохранены")
            back = bot.send_message(message.chat.id, "Для просмотра товаров выберите одну из категорий: ",
                             reply_markup=category_markup())
            mess_editor(message.chat.id, back.message_id)
        elif db.user.check(message.chat.id)[0] == '41':
            db.user.change_state(message.chat.id, 21)
            db.user.update.phone(message.chat.id, message.text)
            bot.send_message(message.chat.id, "Номер телефона изменен")
            back = bot.send_message(message.chat.id, "Для просмотра товаров выберите одну из категорий: ",
                             reply_markup=category_markup())
            mess_editor(message.chat.id, back.message_id)
        elif db.user.check(message.chat.id)[0] == '42':
            db.user.change_state(message.chat.id, 21)
            db.user.update.FIO(message.chat.id, message.text)
            bot.send_message(message.chat.id, "ФИО изменено")
            back = bot.send_message(message.chat.id, "Для просмотра товаров выберите одну из категорий: ",
                             reply_markup=category_markup())
            mess_editor(message.chat.id, back.message_id)
        elif db.user.check(message.chat.id)[0] == '43':
            db.user.change_state(message.chat.id, 21)
            db.user.update.addr(message.chat.id, message.text)
            bot.send_message(message.chat.id, "Адрес изменен")
            back = bot.send_message(message.chat.id, "Для просмотра товаров выберите одну из категорий: ",
                             reply_markup=category_markup())
            mess_editor(message.chat.id, back.message_id)

    @bot.callback_query_handler(func=lambda call: True)
    def category_query(call):
        cat, sub_cat = db.len_upd()
        try:
            # Вывод подкатегорий
            if call.data in cat:
                try:
                    bot.edit_message_text(f"Для категории \"{db.parse(0, int(call.data))}\" найдены следующие подкатегории:", call.from_user.id, mess_state(call.from_user.id), reply_markup=sub_category_markup(
                        call.data))
                except Exception as _ex:
                    print("[Category edit] ", _ex)
                    back = bot.send_message(call.from_user.id,
                                     f"Для категории \"{db.parse(0, int(call.data))}\" найдены следующие подкатегории:",
                                            reply_markup=sub_category_markup(call.data))
                    print(call.data)
                    mess_editor(call.from_user.id, back.message_id)
            elif call.data.split('prod')[0] == '':
                #Страница продуктов для определенной категории
                if mess_state(call.from_user.id) != 'Null':
                    bot.edit_message_text(f"Товары в категории {str(db.parse(1, int(call.data.split('prod')[1])))}: ", call.from_user.id, mess_state(call.from_user.id), reply_markup=product_markup(int(call.data.split('prod')[1])))
                else:
                    back = bot.send_message(call.from_user.id, f"Товары в категории {str(db.parse(1, int(call.data.split('prod')[1])))}: ",
                                            reply_markup=product_markup(int(call.data.split('prod')[1])))
                    mess_editor(call.from_user.id, back.message_id)
            elif call.data == "market":
                if mess_state(call.from_user.id) != 'Null':
                    bot.edit_message_text("Для просмотра товаров выберите одну из категорий: ",
                                          call.from_user.id, mess_state(call.from_user.id),
                                          reply_markup=category_markup())
                else:
                    back = bot.send_message(call.from_user.id, "Для просмотра товаров выберите одну из категорий: ",
                                     reply_markup=category_markup())
                    mess_editor(call.from_user.id, back.message_id)
            elif call.data == 'phone':
                # Замена телефона существующего пользователя
                db.user.change_state(call.from_user.id, 41)
                bot.send_message(call.from_user.id, "Введите новый номер телефона: ")
            elif call.data == 'full_name':
                # Замена ФИО существующего пользователя
                db.user.change_state(call.from_user.id, 42)
                bot.send_message(call.from_user.id, "Введите новое ФИО: ")
            elif call.data == 'address':
                # Замена адреса существующего пользователя
                db.user.change_state(call.from_user.id, 41)
                bot.send_message(call.from_user.id, "Введите новый адрес: ")
            elif call.data.split('|')[1] == '<' and int(call.data.split('|')[0]) != 0:
                # Страница товаров назад
                page = int(call.data.split('|')[0]) - 1
                id = int(call.data.split('|')[2])
                back = bot.send_message(call.from_user.id, 'text', reply_markup=product_markup(id, page))
                mess_editor(call.from_user.id, back.message_id)
            elif call.data.split('|')[1] == '>' and int(call.data.split('|')[3]) > (int(call.data.split('|')[0]) + 1):
                #Страница товаров вперед
                page = int(call.data.split('|')[0]) + 1
                id = int(call.data.split('|')[2])
                back = bot.send_message(call.from_user.id, 'text', reply_markup=product_markup(id, page))
                mess_editor(call.from_user.id, back.message_id)
            elif call.data.split('|')[0] == 'back':
                #Кнопка возврата в меню
                print("back btn")
                print(call.data)
                if call.data.split('|')[1] == '0':
                    if mess_state(call.from_user.id) != 'Null':

                        bot.edit_message_text("Для просмотра товаров выберите одну из категорий: ", call.from_user.id, mess_state(call.from_user.id), reply_markup=category_markup())
                    else:

                        back = bot.send_message(call.from_user.id, "Для просмотра товаров выберите одну из категорий: ",
                                         reply_markup=category_markup())
                        mess_editor(call.from_user.id, back.message_id)
                else:
                    if mess_state(call.from_user.id) != 'Null':

                        print("in db            ", int(call.data.split('|')[1]))
                        bot.edit_message_text(f"Для категории \"{db.parse(0, db.parse(5, int(call.data.split('|')[1])))}\" найдены следующие подкатегории:", call.from_user.id, mess_state(call.from_user.id), reply_markup=sub_category_markup(db.parse(5, int(call.data.split('|')[1]))))
                    else:
                        bot.send_message(call.from_user.id, f"Для категории \"{db.parse(0, db.parse(5, int(call.data.split('|')[1])))}\" найдены следующие подкатегории:",
                                         reply_markup=sub_category_markup(db.parse(5, int(call.data.split('|')[1]))))
        except Exception as _ex:
            print("[CallBack]", _ex)
            pass


    bot.infinity_polling()
