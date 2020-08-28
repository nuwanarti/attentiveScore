import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib
# from tensorflow.keras import keras

from keras.models import load_model
# from tensorflow.keras.models import load_model

from keras.preprocessing import image
# from tensorflow.keras.preprocessing import image

import numpy as np

import keras


data_dir = '/attentiveness/attentiveScore/bodyLanguage/labeledImages/'
batch_size = 32
img_height = 300
img_width = 300

model = keras.models.load_model("/home/manula/Documents/attentiveScore/bodyLanguage/final_model.h5")

data_dir = '/home/manula/Documents/attentiveScore/bodyLanguage/resized/'

# predicting images

img = image.load_img(data_dir + 'seg_0.jpg', target_size=(img_width, img_height), color_mode="grayscale")
# print(img)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict_classes(images, batch_size=32)
print('classes :')
print (classes)
