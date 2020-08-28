from PIL import Image
import os

def black_background_thumbnail(path_to_image, thumbnail_size=(300,300)):
    background = Image.new('RGB', thumbnail_size, "black")    
    source_image = Image.open(path_to_image).convert("RGB")
    source_image.thumbnail(thumbnail_size)
    (w, h) = source_image.size
    background.paste(source_image, (round((thumbnail_size[0] - w) / 2), round((thumbnail_size[1] - h) / 2 )))
    return background

if __name__ == '__main__':

    path = '/home/manula/Documents/attentiveScore/bodyLanguage/cdcl-semantic-segmentation/output/'
    files = os.listdir(path)
    for file in files:
        # print(file)
        img = black_background_thumbnail(path + file)
        img.save('/home/manula/Documents/attentiveScore/bodyLanguage/resized/' + file)
    # img.show()


# from PIL import Image
# import os

# path = "/attentiveness/attentiveScore/bodyLanguage/cdcl-semantic-segmentation/output/"
# resize_ratio = 0.5  # where 0.5 is half size, 2 is double size

# def resize_aspect_fit():
#     dirs = os.listdir(path)
#     for item in dirs:
#         if item == '.jpg':
#             continue
#         if os.path.isfile(path+item):
#             image = Image.open(path+item)
#             file_path, extension = os.path.splitext(path+item)

#             new_image_height = int(image.size[0] / (1/resize_ratio))
#             new_image_length = int(image.size[1] / (1/resize_ratio))

#             image = image.resize((new_image_height, new_image_length), Image.ANTIALIAS)
#             image.save(file_path + '_small' + extension, 'JPEG', quality=90)


# resize_aspect_fit()
# from PIL import Image

# def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
#     x, y = im.size
#     size = min(min_size, x, y)
#     new_im = Image.new('RGBA', (size, size), fill_color)
#     new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
#     return new_im

# test_image = Image.open('WTF.jpg')
# new_image = make_square(test_image)
# new_image.show()