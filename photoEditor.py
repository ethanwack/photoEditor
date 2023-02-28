from PIL import Image, ImageEnhance, ImageFilter
import os

path - './Pictures'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFileter.SHARPEN).rotate(-90)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splittext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg)