import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

image_files = []

# image_files= ["/home/pi/next_level/3projec/img2/bohang_1.jpg"]
for i in range(5, 0, -1):
    image_files.append("/home/pi/next_level/3projec/img2/bohang_green_{}.jpg".format(i))
    print(image_files)
    
for i in range(5, 0, -1):
    image_files.append("/home/pi/next_level/3projec/img2/bohang_red_{}.jpg".format(i))
    print(image_files)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 128
options.gpio_slowdown = 4
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)

def basic():
    try:
        while True:
            for image_file in image_files:
                image = Image.open(image_file)
                # Create a thumbnail that fits our screen
                image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
                matrix.SetImage(image.convert('RGB'))
                time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

basic()

# def odd(color, sec):
    

# try:
#     print("Press CTRL-C to stop")
#     while True:
#         time.sleep(5)
# except KeyboardInterrupt:
#     sys.exit(0)


