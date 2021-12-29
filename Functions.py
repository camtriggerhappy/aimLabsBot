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
    Cords = []
    #normalize to center of screen
    for i in boxes:
        Cords.append([-((2560/2) - ((i[0] + i[2]) / 2)) , -((1440/2) - (i[1] + i[3]) / 2)])




    return Cords
#also returns to origin
def click(x , y):

    pyautogui.move(x, y)
    pyautogui.click()
    pyautogui.move(-x, -y)
