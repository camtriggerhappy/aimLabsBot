import detecto.core
import pyautogui
from PIL import ImageGrab


def screenshot():
    img = ImageGrab.grab()

    return img


def getModel():
    return detecto.core.Model.load('Model', ["Target"])

def getClicks(boxes):
    print("getting clicks")
    xCords = []
    yCords = []
    for i in boxes:
        xCords.append((i[0] + i[2]) / 2)
        yCords.append((i[1] + i[3]) / 2)
    print(xCords,yCords )
    return [xCords, yCords]

def click(x , y):

    pyautogui.dragTo(x, y)
    pyautogui.click()