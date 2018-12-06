from PIL import Image, ImageDraw, ImageFont
import glob
import datetime
import os
from time import sleep

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size=80)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width/2, height/2), 'JYY JYY', font=myfont, fill=fillcolor)
    #img.save('result.jpg','jpeg')
    return 0



if __name__ == '__main__':
    target_dir=r"C:\Users\tommy\Desktop\Pics\Result"
    if not os.path.exists(target_dir):
        print('Target file path not exist, Creating...')
        os.mkdir(target_dir)
    for files in glob.glob(r'C:\Users\tommy\Desktop\Pics\IMG_*.jpg'):
        print('Processing the image in location:', files)
        image = Image.open(files)
        add_num(image)
        name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = target_dir + os.sep + name + '_result.jpg'
        sleep(2)
        image.save(filename)
        print('Process image saved to', filename)
    print('The processing Done!')