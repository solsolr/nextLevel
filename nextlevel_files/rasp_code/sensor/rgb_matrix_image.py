import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

image_file = "/home/pi/next_level/img/man012.jpg"

image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 128
options.gpio_slowdown = 4
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)

# Create a thumbnail that fits our screen
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)


