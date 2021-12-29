import Functions
import cv2
import pyautogui


model = Functions.getModel()


while True:
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    img = Functions.screenshot()
    i, boxes, j = model.predict(img)
    if boxes.size:
        toClick = Functions.getClicks(boxes)
        print("Click attempted")
        print(toClick)
        if len(toClick)>2:
            for i in toClick:
                print(i)
                if len(i) > 0:
                    print('attempting click')
                    Functions.click(i[0] , i[1])
        elif len(toClick) == 2:
            Functions.click(toClick[0], toClick[1])

