import urllib.request
from datetime import datetime
import time
import json
import configparser

#мои библиотеки
import funcs
import myClasses
import bot_notification


print("Main.py")


error_count = 0 # подсчёт подтряд неудачных попыток достучаться до сервера
connect_status = True

# Вычитывание из config.ini
config = configparser.ConfigParser()
config.read('config.ini')
time_for_check_connect = config.get("Timing", "time_for_check_connect")
time_for_reconnect = config.get("Timing", "time_for_reconnect")

#импорт классов из objects.json

with open("objects.json", "r") as read_file:
    data = json.load(read_file)

points = []
for key, value in data.items():
    points.append(myClasses.Point(value["addr"],
                                  value["available"],
                                  value["information"]))



while True:
    for i in points:
        print("ОТЛАДОЧНЫЙ ПРИНТ СОСТОЯНИЕ СЕРВЕРОВ", i.addr, i.available)
        error_count = 0

        try:
            # Первый запрос коннекта
            response = urllib.request.urlopen(i.addr, timeout=30)
            print(f"All ok! for {i.addr} Код: {response.getcode()}")
            connect_status = True
        except Exception as e:
            # Любая ошибка прилетает сюда
            print(f"Ошибка при запросе: {e} url: {i.addr} Попытка реконнекта.")
            connect_status = False
            while error_count <= 5 and not connect_status:
                try:
                    response = urllib.request.urlopen(i.addr, timeout=30)
                    print(f"All ok! for {i.addr} Код: {response.getcode()}  При повторной проверке")
                    connect_status = True
                except:
                    print(f"Неудавшаяся попытка реконнекта: {i.addr}")
                    error_count += 1
                    time.sleep(int(time_for_reconnect))

        funcs.statusChange(i.available, connect_status, i.addr, i.information )
        i.available = connect_status



    time.sleep(int(time_for_check_connect))
