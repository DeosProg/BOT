import os
import time
import datetime

lessons = [34200, 40800, 47400, 55500, 68580]


def check_settings():
    H = datetime.today().strftime("%H")
    M = datetime.today().strftime("%M")
    S = datetime.today().strftime("%S")
    now_time = int(H) * 60 * 60 + int(M) * 60 + int(S)
    path = os.getcwd() + '/ID'
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            n = (os.path.join(file))
            filelist.append(n)
    for i in filelist:
        with open(path + '/' + str(i), 'r+', encoding='utf-8') as f:
            try:
                line = f.readlines()
                id = line[2]
                s_time = line[3]
                for j in lessons:
                    print(j - now_time)
                    if j - now_time == int(s_time):
                        return id
            except:
                pass



