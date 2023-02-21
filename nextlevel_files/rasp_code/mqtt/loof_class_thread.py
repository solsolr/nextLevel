import time
import sys
import cv2

# from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

def set():
    image_files = []

    # image_files= ["/home/pi/next_level/3projec/img2/bohang_1.jpg"]
    for i in range(5, 0, -1):
        image_files.append(f"C:/Users/orang/Desktop/bohang_img/bohang_green_{i}.jpg")
        print(image_files)
        
    for i in range(5, 0, -1):
        image_files.append(f"C:/Users/orang/Desktop/bohang_img/bohang_red_{i}.jpg")
        print(image_files)
    return image_files

# Configuration for the matrix
# options = RGBMatrixOptions()
# options.rows = 32
# options.cols = 128
# options.gpio_slowdown = 4
# options.chain_length = 1
# options.parallel = 1
# options.hardware_mapping = 'adafruit-hat'

# matrix = RGBMatrix(options=options)

def basic():
    try:
        while True:
            for image_file in image_files:
                print(">>>>>>>>>>>>>>>>",image_file)
                
                # opencv 
                # image read
                # color = cv2.imread(image_file, cv2.IMREAD_COLOR)
                
                # # image show
                # cv2.imshow('Color', color)
                # # gray image write
                # # cv2.imwrite(fwname, gray)

                # # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                
                # image = Image.open(image_file)
                
                # Create a thumbnail that fits our screen
                # image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
                # matrix.SetImage(image.convert('RGB'))
                time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)


def odd(color, sec):
    try:
        starts = [i for i in range(len(image_files)) if sec in image_files[i]]
        print("시작후보는 ",starts)
        if color == "green":
            start = starts[0]
        else:
            start = starts[1]
        print("시작은",start)
        for i in range(start, 11):
            print(">>>>>>>>>>>>>>>>",image_files[i])
            time.sleep(1)
    except:
        pass

image_files = set()
print("이미지 리스트 목록: ",image_files)
odd("red", "3")
basic()

# try:
#     print("Press CTRL-C to stop")
#     while True:
#         time.sleep(5)
# except KeyboardInterrupt:
#     sys.exit(0)

