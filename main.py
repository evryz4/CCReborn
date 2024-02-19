# CookieClicker Reborn 1.0
# https://github.com/watermelon46/CCReborn

import time
import os
import json
from platform import uname

clickerActive = False
clickerActiveTime = 0
clickerLastClick = 0

config = {
    "mobile": False, # Платформа. False - ПК, True - телефон. Оптимизирует арты под мелкие экраны.
    "autoLoadGame": False, # Автоматическая загрузка сохранения.
    "cfgDir": "ToBeFilled", # Папка для хранения сохранений. Обычно, заполняется автоматически используя SysCompat. Уберите ToBeFilled, чтобы не заполнять автоматически
    "clearCmd": "ToBeFilled", # Команда, используемая функцией clear()
    "system": uname()[0], # Тип системы. Влияет на принцип работы clear()
    "ccVerInfo": "1.0",
    "ccVerType": "beta"
}

def SysCompat(): # Функция, которая обеспечивает совместимость CC Reborn с Windows, Linux и MacOS
    if config['system'] == 'Windows':
        if config['clearCmd'] == "ToBeFilled":
            config['clearCmd'] = 'cls'
        if config['cfgDir'] == "ToBeFilled":
            config['cfgDir'] = 'C://CookieClicker//'
    else:
        if config['clearCmd'] == "ToBeFilled":
            config['clearCmd'] = 'clear'
        if config['cfgDir'] == "ToBeFilled":
            config['cfgDir'] = '//home//CookieClicker//'

SysCompat()

player = {
    "cookies" : 0,
    "coins" : 0,
    "boosters" : 0,
    "clickers" : 0,
    "watermelons" : 0
}

def clear():
    os.system(config['clearCmd'])

def save(showSuccessSave = True):
    prepared_data = json.dumps(player)
    dir = config['cfgDir']
    try:
        save_file = open(f'{dir}ccsave.json', 'w')
    except FileNotFoundError:
        try:
            cache = open(f'{dir}ccsave.json', 'w+')
            cache.close()
        except:
            os.mkdir(dir)
            cache = open(f'{dir}ccsave.json', 'w+')
            cache.close()
        save_file = open(f'{dir}ccsave.json', 'w')
    save_file.truncate(0)
    save_file.write(prepared_data)
    save_file.close()
    if showSuccessSave == True:
        print(f'{Style.RESET_ALL + Fore.GREEN}Игра сохранена!{Style.RESET_ALL}')

def load():
    clickerActive = False
    dir = config['cfgDir']
    try:
        save_file = open(f'{dir}ccsave.json')
    except FileNotFoundError:
        print(f'{Style.RESET_ALL}{Fore.RED}Файл сохранения не найден, создаем при помощи save...{Style.RESET_ALL}')
        save(False)
        save_file = open(f'{dir}ccsave.json')
    global player
    save_data = save_file.read()
    player = json.loads(save_data)
    save_file.close()
    print(f'{Style.RESET_ALL + Fore.GREEN}Игра загружена!{Style.RESET_ALL}')

if config['autoLoadGame'] == True:
    load()

def reInput():
    return input(f'{Style.RESET_ALL + Style.BRIGHT}\n> {Style.RESET_ALL}')

try:
    from colorama import Fore, Back, Style, init
except ModuleNotFoundError:
    print('Одной из обязательных библиотек нет. Попытка установки...')
    os.system('python3 -m pip install colorama')

cache = None # Переменная для хранения всякой фигни

init()
clear()
print(f'{Fore.YELLOW + Style.BRIGHT}CookieClicker {Style.RESET_ALL + Fore.YELLOW}Reborn {Fore.RESET}v{config["ccVerInfo"]} {config["ccVerType"]}\n{Style.RESET_ALL}Пропиши help для просмотра списка команд\n{Style.BRIGHT}Нажми Enter, чтобы начать{Style.RESET_ALL}')

# /\ /\ Последняя версия CookieClicker Classic вышла в мае 2023 года, и была полным говнокодом.
#       Именно поэтому CookieClicker Classic больше не быть, и хлнм принял решение переписать CookieClicker с нуля.
# \___/ February 20, 2024 \\// 

while True: # Ну чтож, погнали!
    try:
        command = input(f'{Style.RESET_ALL + Style.BRIGHT}\n> {Style.RESET_ALL}')
    except KeyboardInterrupt:
        print('Тебе трудно прописать exit?')
        os.system('pause')
    clear()
    if command == '':
        summaryClick = player['boosters'] + 1
        player['cookies'] += summaryClick
        if clickerActive == True:
            
            clickerActiveAgo = int(time.time() - clickerActiveTime)
            clickSecondsNeed = int(time.time() - clickerLastClick)
            if clickerActiveAgo > 300:
                player['cookies'] += summaryClick * 300
                clickerActive = False
            else:
                player['cookies'] += summaryClick * clickSecondsNeed
            clickerLastClick = time.time()
            toClickerEnd = 300 - clickerActiveAgo
        print(f'{Fore.GREEN + Style.BRIGHT}🍪 Клик!\n\nВаш баланс:\n {Style.RESET_ALL + Fore.YELLOW}Печеньки: {Style.RESET_ALL}{player["cookies"]}\n {Fore.YELLOW}Монетки: {Style.RESET_ALL}{player["coins"]}\n {Fore.YELLOW}Арбузы: {Style.RESET_ALL}{player["watermelons"]}\n {Fore.YELLOW}Бустеры: {Style.RESET_ALL}{player["boosters"]}\n {Fore.YELLOW}Кликеры: {Style.RESET_ALL}{player["clickers"]}')
        if clickerActive:
            print(f'{Fore.GREEN + Style.BRIGHT}ℹ До конца кликера осталось {toClickerEnd} сек.')
    elif command == 'exit':
        print(f'{Fore.RED + Style.BRIGHT}Сохранить игру перед выходом? [Y/N]')
        if reInput() == 'Y':
            save()
        break
        exit()
    elif command == 'exchange':
        cache = player['cookies'] / 100
        player['coins'] = player['coins'] + player['cookies'] / 100 + player['watermelons'] / 10
        player['cookies'] = 0
        print(f'{Fore.GREEN + Style.BRIGHT}💱 Ваши печеньки были обменены на монетки ({cache})')
    elif command == 'save':
        save()
    elif command == 'load':
        load()
    elif command == 'help':
        print(f"{Fore.GREEN + Style.BRIGHT}ℹ Команды CookieClicker'а\n\n{Style.RESET_ALL + Fore.YELLOW}help - {Style.RESET_ALL}это меню\n{Style.RESET_ALL + Fore.YELLOW}exchange - {Style.RESET_ALL}обменять печеньки на монетки с курсом 100 печенек к 1 монетке\n{Style.RESET_ALL + Fore.YELLOW}shop - {Style.RESET_ALL}магазин\n{Style.RESET_ALL + Fore.YELLOW}clicker - {Style.RESET_ALL}запустить автокликер\n{Style.RESET_ALL + Fore.YELLOW}save - {Style.RESET_ALL}сохранить игру\n{Style.RESET_ALL + Fore.YELLOW}load - {Style.RESET_ALL}загрузить игру\n{Style.RESET_ALL + Fore.YELLOW}exit - {Style.RESET_ALL}покинуть игру")
    elif command == 'reloadSysCompat':
        print(f"{Fore.GREEN + Style.BRIGHT}⏳ Перезагружаем SysCompat...{Style.RESET_ALL}")
        SysCompat()
        clear()
        print(f"{Fore.GREEN + Style.BRIGHT}✔ SysCompat успешно перезагружен, но зачем?{Style.RESET_ALL}")
    elif command == 'shop':
        shopcancel = 0
        print(f"{Fore.GREEN + Style.BRIGHT}ℹ Магазин\nДля покупки введите код продукта\n{Style.RESET_ALL + Fore.YELLOW}Бустер (1) - {Style.RESET_ALL}5 монет\n{Style.RESET_ALL + Fore.YELLOW}Кликер (2) - {Style.RESET_ALL}10 монет\n{Style.RESET_ALL + Fore.YELLOW}Арбуз (3) - {Style.RESET_ALL}20 монет\n{Style.RESET_ALL}")
        shopinput = reInput()
        if shopinput == '1':
            if player['coins'] >= 5:
                player['coins'] -= 5
                player['boosters'] += 1
                print(f"{Fore.GREEN + Style.BRIGHT}✔ Вы успешно купили 1 бустер!{Style.RESET_ALL}")
            else:
                shopcancel = 1
        elif shopinput == '2':
            if player['coins'] >= 10:
                player['coins'] -= 10
                player['clickers'] += 1
                print(f"{Fore.GREEN + Style.BRIGHT}✔ Вы успешно купили 1 кликер! Он работает 5 минут, для его включения напишите clicker{Style.RESET_ALL}")
            else:
                shopcancel = 1
        elif shopinput == '3':
            if player['coins'] >= 20:
                player['coins'] -= 20
                player['watermelons'] += 1
                print(f"{Fore.GREEN + Style.BRIGHT}✔ Вы успешно купили 1 арбуз!{Style.RESET_ALL}")
            else:
                shopcancel = 1
        if shopcancel == 1:
            print(f"{Fore.YELLOW + Style.BRIGHT}❌ Неверный код продукта или недостаточно монет!{Style.RESET_ALL}")
    elif command == 'clicker':
        if player['clickers'] < 1:
            print(f"{Fore.YELLOW + Style.BRIGHT}❌ У вас нет кликеров!{Style.RESET_ALL}")
        else:
            player['clickers'] -= 1
            clickerActive = True
            clickerActiveTime = time.time()
            clickerLastClick = clickerActiveTime
            print(f"{Fore.GREEN + Style.BRIGHT}✔ Кликер запущен!{Style.RESET_ALL}")