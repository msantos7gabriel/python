from random import randint
import pyautogui as pg
import time as tm

hora_atual = tm.localtime(tm.time())

print(hora_atual.tm_hour)


def verificar_hr():
    if hora_atual.tm_hour < 12:
        return "Bom dia Grupo!"
    elif hora_atual.tm_hour < 18:
        return "Boa tarde Grupo!"
    else:
        return "Boa noite Grupo!"


def mandar_mensagem():
    tm.sleep(15)
    pg.moveTo(420, 180, duration=1)
    pg.click()
    pg.write("Os Mano", interval=0.1)
    pg.moveTo(480, 350, duration=1)
    pg.click()
    pg.moveTo(970, 1000, duration=1)
    pg.click()
    mensagem = str(verificar_hr())
    pg.write(mensagem, interval=0.1)
    pg.hotkey("enter")
    pg.moveTo(740, 1000, duration=1)
    pg.click()
    pg.moveTo(830, 1000, duration=1)
    pg.click()
    pg.moveTo(780, 720, duration=1)
    pg.click()
    pg.write(mensagem, interval=0.1)
    pg.moveTo(randint(715, 1810), randint(745, 960), duration=1)
    pg.click()
    tm.sleep(2)
    pg.hotkey("enter")
    pg.hotkey("ctrl", "w")


def abrir_opera():
    pg.moveTo(850, 1070, duration=1)
    pg.click()
    tm.sleep(2)
    pg.hotkey("ctrl", "t")
    pg.hotkey("alt", "tab")
    pg.moveTo(850, 1070, duration=1)
    pg.click()
    pg.moveTo(330, 60, duration=1)
    pg.click()
    pg.write("https://web.whatsapp.com", interval=0.1)
    pg.hotkey("enter")
    mandar_mensagem()


abrir_opera()
