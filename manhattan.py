import pyautogui
import random
import winsound
from plyer import notification
from threading import Thread


notification.notify(
    title = 'Manhattan Virus',
    message = 'skill issue imagine getting a virus lololololol XD',
    app_icon = None,
)


def mouseJitter(dumy):
    while 1:
        pyautogui.moveRel((random.random()-0.5)*20,(random.random()-0.5)*20, duration = 0.01)

t=Thread(target=mouseJitter,args=(1,))
t.start()
sz=pyautogui.size()
while(1):
    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
