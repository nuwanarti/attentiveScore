import os
import numpy as np
import cv2
import numpy as np
from PIL import Image
# import tensorflow as tf
import pathlib
# from tensorflow.keras import keras

# from keras.models import load_model
from keras.preprocessing import image
import numpy as np

import keras




def classifyImages(images):
    folder = '/home/manula/Documents/attentiveScore/bodyLanguage/cdcl-semantic-segmentation/input/'
    index = 0
    # remove everything inside the input folder
    os.system("rm -r " + folder + "/*")
    for img in images:
        
        cv2.imwrite(folder + str(index) + '.jpg', img)
        index = index + 1

    os.system(folder + '../semanticSegmentImages.sh')
    # remove all the resized images
    os.system('rm -r ' + folder + '../../resized/*')
    # os.system('python3 /home/rt/Documents/gayan/attentiveScore/bodyLanguage/resizeImages.py')
    path = '/home/manula/Documents/attentiveScore/bodyLanguage/cdcl-semantic-segmentation/output/'
    files = os.listdir(path)
    # resizedImages = []
    for file in files:
        # print(file)
        img = black_background_thumbnail(path + file)
        img.save('/home/manula/Documents/attentiveScore/bodyLanguage/resized/' + file)
        # resizedImages.append(img)



    
    data_dir = '/home/manula/Documents/attentiveScore/bodyLanguage/resized/'
    batch_size = 32
    img_height = 300
    img_width = 300

    model = keras.models.load_model("/home/manula/Documents/attentiveScore/bodyLanguage/final_model.h5")

    

    files = os.listdir(data_dir)
    # resizedImages = []
    classes = []
    for file in files:
        # predicting images
        print(file)
        img = image.load_img(data_dir + file, target_size=(img_width, img_height), color_mode="grayscale")
        # print(img)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)   
        images = np.vstack([x])
        prediction = model.predict_classes(images, batch_size=32)
        classes.append(prediction[0])

    
    # img = image.load_img(data_dir + 'seg_0.jpg', target_size=(img_width, img_height), color_mode="grayscale")
    # # print(img)
    # x = image.img_to_array(img)
    # x = np.expand_dims(x, axis=0)   
    # images = np.vstack([x])
    # prediction = model.predict_classes(images, batch_size=32)
    # # classes.append(prediction)
    # print(prediction)
    # return prediction[0]
    print('prediction clases ', len(files))
    print (classes)
    return classes


def black_background_thumbnail(path_to_image, thumbnail_size=(300,300)):
    background = Image.new('RGB', thumbnail_size, "black")    
    source_image = Image.open(path_to_image).convert("RGB")
    source_image.thumbnail(thumbnail_size)
    (w, h) = source_image.size
    background.paste(source_image, (round((thumbnail_size[0] - w) / 2), round((thumbnail_size[1] - h) / 2 )))
    return background

        
    