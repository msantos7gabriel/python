import pyautogui as pg
import time as tm

hora_atual = tm.localtime(tm.time())

print(hora_atual.tm_hour)

def abrir_opera():
    pg.moveTo(850, 1070, duration=1)
    pg.click()
    tm.sleep(5)
    pg.hotkey("ctrl", "t")
    pg.moveTo(850, 1070, duration=1)
    pg.click()
    pg.write("https://www.google.com/")

