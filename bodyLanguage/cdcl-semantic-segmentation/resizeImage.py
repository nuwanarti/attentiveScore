from PIL import Image

def black_background_thumbnail(path_to_image, thumbnail_size=(300,300)):
    background = Image.new('RGBA', thumbnail_size, "black")    
    source_image = Image.open(path_to_image).convert("RGBA")
    source_image.thumbnail(thumbnail_size)
    (w, h) = source_image.size
    background.paste(source_image, ((thumbnail_size[0] - w) / 2, (thumbnail_size[1] - h) / 2 ))
    return background

if __name__ == '__main__':
    img = black_background_thumbnail('WTF.jpg')
    img.save('tmp.jpg')
    img.show()