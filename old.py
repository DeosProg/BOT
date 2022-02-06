if 'Домашнее задание на эту неделю' in message.text:
        try:
            with open('DZ', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                pn = lines[0]
                sr = lines[2]
                ch = lines[3]
                pt = lines[4]
                sb = lines[5]
                bot.send_message(message.chat.id, texts.homework.format(pn=pn, sr=sr, ch=ch, pt=pt, sb=sb),
                                 reply_markup=keyboard)
        except Exception as exc:
            print(exc)
            traceback.print_exc()


    if 'Домашнее задание на след. неделю' in message.text:
        try:
            with open('DZ2', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                pn = lines[0]
                sr = lines[2]
                ch = lines[3]
                pt = lines[4]
                sb = lines[5]
                bot.send_message(message.chat.id, texts.homework2.format(pn=pn, sr=sr, ch=ch, pt=pt, sb=sb),
                                 reply_markup=keyboard)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
if 'Расписание на завтра' in message.text:
        try:
            c_date = date.today()
            day = str(int(c_date.day) + 1) + ' '
            month = months[int(c_date.month)]
            pairs = timetable_processing.get_timetable_tomorrow()
            try:
                if pairs[5] == 'Авиамоторная':
                    place = 'на Авиамоторной'
                else:
                    place = 'на Октябрьском поле'
            except:
                place = 'нигде'
            bot.send_message(message.chat.id,
                             texts.timetables_text.format(
                                 day=day + month,
                                 place=place,
                                 pair1=pairs[0],
                                 pair2=pairs[1],
                                 pair3=pairs[2],
                                 pair4=pairs[3],
                                 pair5=pairs[4],
                                 parse_mode="Markdown"))
            bot.send_message(message.chat.id, texts.main, reply_markup=keyboard)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
    if 'Расписание на сегодня' in message.text:
        try:
            c_date = date.today()
            day = str(c_date.day) + ' '
            month = months[int(c_date.month)]
            pairs = timetable_processing.get_timetable_today()
            try:
                if pairs[5] == 'Авиамоторная':
                    place = 'на Авиамоторной'
                else:
                    place = 'на Октябрьском поле'
            except:
                place = 'нигде'
            bot.send_message(message.chat.id,
                             texts.timetables_text.format(
                                 day=day + month,
                                 place=place,
                                 pair1=pairs[0],
                                 pair2=pairs[1],
                                 pair3=pairs[2],
                                 pair4=pairs[3],
                                 pair5=pairs[4],
                                 parse_mode="Markdown"))
            bot.send_message(message.chat.id, texts.main, reply_markup=keyboard)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
#ДОМАШНЕЕ ЗАДАНИЕ-------------------------------------------------------
        if call.data == '0':
            try:
                with open('DZ', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    pn = lines[0]
                    sr = lines[2]
                    ch = lines[3]
                    pt = lines[4]
                    sb = lines[5]
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=texts.homework.format(pn=pn, sr=sr, ch=ch, pt=pt, sb=sb) )
            except Exception as exc:
                print(exc)
                traceback.print_exc()
        elif call.data == '1':
            try:
                with open('DZ2', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    pn = lines[0]
                    sr = lines[2]
                    ch = lines[3]
                    pt = lines[4]
                    sb = lines[5]
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=texts.homework2.format(pn=pn, sr=sr, ch=ch, pt=pt, sb=sb) )
            except Exception as exc:
                print(exc)
                traceback.print_exc()

#day1 = str(c_date.day)
#day2 = str(int(c_date.day) + 1) + ' '
#button_1 = types.KeyboardButton(text="Расписание на завтра " + cal(day2))
#button_2 = types.KeyboardButton(text="Расписание на сегодня " + cal(day1))
#button_3 = types.KeyboardButton(text="Домашнее задание на эту неделю📖")
#button_4 = types.KeyboardButton(text="Домашнее задание на след. неделю📘")