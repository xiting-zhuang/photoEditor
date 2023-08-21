from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'



for filename in os.listdir(path): 
    print(filename)
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')



    output_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{output_name}_edited.jpg')

     
     