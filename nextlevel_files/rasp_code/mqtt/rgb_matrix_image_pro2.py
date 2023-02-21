import time
import sys
from threading import Thread, Event
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

event = Event()
image_files = []

# image_files= ["/home/pi/next_level/3projec/img2/bohang_1.jpg"]
for i in range(5, 0, -1):
    image_files.append("/home/pi/next_level/Rpiprojec/imgs/bohang_green_{}.jpg".format(i))
    print(image_files)
    
for i in range(5, 0, -1):
    image_files.append("/home/pi/next_level/Rpiprojec/imgs/bohang_red_{}.jpg".format(i))
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
            if event.is_set():
                # print('Infinite Loop Stop!')
                return
            for image_file in image_files:
                image = Image.open(image_file)
                # Create a thumbnail that fits our screen
                image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
                matrix.SetImage(image.convert('RGB'))
                time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

# t = Thread(target=basic, daemon=True)
# t.start()

# print('>>>>>>>Script Start!')
# for i in range(1, 6):
#     time.sleep(3)
#     print('for loop #{}'.format(i))
#     if i == 3:
#         event.set() # 기본 보행자 신호 중지 됨.
#         event.clear() # 내부 플래그 초기화.
# print('Script End!')

basic()

# def odd(color, sec):
    

# try:
#     print("Press CTRL-C to stop")
#     while True:
#         time.sleep(5)
# except KeyboardInterrupt:
#     sys.exit(0)

