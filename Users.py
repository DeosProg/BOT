import os


def create_new_id(telegram_id='none', time=None, id=0):  # создание нового id
    files = os.listdir('C:\\Users\\peter\\PycharmProjects\\2107BOT\\ID')
    for i in files:
        if i != '.DS_Store':
            if int(i) > id:
                id = int(i)
    id = id + 1
    with open('ID/' + str(id), 'w') as f:
        f.writelines(
            str(telegram_id) + '\n' + str(time) + '\n' + '0' + '\n' + '0' + '\n' + '0')
        f.close()
    print(id)
