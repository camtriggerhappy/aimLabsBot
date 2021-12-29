import pathlib
import time
from pathlib import Path
from PIL import ImageGrab
import os
import Functions

p = Path("Pictures")

count = 0
while True:

    ImageGrab.grab().save("Pictures/" + f"pic {count}" +".jpg", format = "JPEG")
    time.sleep(4)
    count += 1