import time

import PIL.Image
import matplotlib.pyplot as plt
import detecto
import numpy
from detecto.core import Dataset
import torch
from detecto.utils import read_image
from PIL import ImageGrab
import cv2
print(torch.cuda.is_available())
dataset = Dataset('Imagesandlabels')

def screenshot():
    monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
    img = ImageGrab.grab()
    #img = numpy.asarray(img)
    #PIL.Image.fromarray(img).show()

    return img

#mss.mss().save(mss.mss().monitors[0])

model = detecto.core.Model(["Target"])

from detecto.visualize import show_labeled_image

image, targets = dataset[0]
#show_labeled_image(image, targets['boxes'], targets['labels'])

loss = model.fit(dataset, verbose=True, epochs=12)


#image , targets, scores = model.predict(read_image('Imagesandlabels/20211226225109_1.jpg'))
#images = [read_image('Imagesandlabels/20211226225447_1.jpg'), read_image('Imagesandlabels/20211226225157_1.jpg'), read_image('Imagesandlabels/20211226225219_1.jpg'), read_image('Imagesandlabels/20211226225436_1.jpg')]

#detecto.visualize.plot_prediction_grid(model, [screenshot()])

model.save('Model')





