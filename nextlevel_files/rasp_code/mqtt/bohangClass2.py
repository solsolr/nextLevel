import time
import sys
from threading import Thread, Event
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

class Bohang():
    def __init__(self):
        self.event = Event()
        self.eventElement = 0
        self.image_files = []

        # image_files= ["/home/pi/next_level/3projec/img2/bohang_1.jpg"]
        for i in range(5, 0, -1):
            self.image_files.append(f"/home/pi/next_level/3projec/img2/bohang_green_{i}.jpg")
            # print(self.image_files)
            
        for i in range(5, 0, -1):
            self.image_files.append(f"/home/pi/next_level/3projec/img2/bohang_red_{i}.jpg")
            # print(self.image_files)
            
        # Configuration for the matrix
        self.options = RGBMatrixOptions()
        self.options.rows = 32
        self.options.cols = 128
        self.options.gpio_slowdown = 4
        self.options.chain_length = 1
        self.options.parallel = 1
        self.options.hardware_mapping = 'adafruit-hat'

        self.matrix = RGBMatrix(options=self.options)
        print(self.image_files)

    def basic(self):
        try:
            while True:
                # 이벤트 내부플래그가 True면 쓰레드 stop!
                # if self.event.is_set():
                #     # print('Infinite Loop Stop!')
                #     return
                if self.eventElement == 1:
                    return
                for image_file in self.image_files:
                    # print(">>>>>>>>>>>>>>>>",image_file)
                    image = Image.open(image_file)
                    # Create a thumbnail that fits our screen
                    image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                    self.matrix.SetImage(image.convert('RGB'))
                    time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)


    def odd(self, color, sec):
        try:
            starts = [i for i in range(len(self.image_files)) if sec in self.image_files[i]]
            print("시작후보는 ",starts)
            if color == "green":
                start = starts[0]
            else:
                start = starts[1]
            print("시작은",start)
            for i in range(start, 11):
                print(">>>>>>>>>>>>>>>>",self.image_files[i])
                time.sleep(1)
        except:
            pass


if __name__ == '__main__':
    b = Bohang()
    # t = Thread(target=b.basic, daemon=True)
    # t.start()

    def test():
        print('>>>>>>>Script Start!')
        for i in range(1, 6):
            time.sleep(3)
            print('for loop #{}'.format(i))
            if i == 3:
                b.eventElement = 1
                # b.event.set() # 기본 보행자 신호 중지 됨.
                # b.event.clear() # 내부 플래그 초기화.
        print('Script End!')
    
    g = Thread(target=test, daemon=True)
    g.start()
    b.basic()