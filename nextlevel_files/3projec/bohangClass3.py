import time
import sys
from threading import Thread, Event
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

class Bohang():
    def __init__(self):
        self.event = Event()
        self.eventElement = 0
        self.sec = "1"
        self.color = "green"
        self.image_files = []
        self.a = "go"

        # image_files= ["/home/pi/next_level/3projec/img2/bohang_1.jpg"]
        for i in range(15, 0, -1):
            self.image_files.append(f"/home/pi/next_level/Rpiprojec/imgs/bohang_green_{i}.jpg")
            # print(self.image_files)
            
        for i in range(15, 0, -1):
            self.image_files.append(f"/home/pi/next_level/Rpiprojec/imgs/bohang_red_{i}.jpg")
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
                    break
                for image_file in self.image_files:
                    # print(">>>>>>>>>>>>>>>>",image_file)
                    image = Image.open(image_file)
                    # Create a thumbnail that fits our screen
                    image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                    self.matrix.SetImage(image.convert('RGB'))
                    time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

    # basic 대신 odd만 사용하게 만들기
    def odd(self):
        try:
            while True:
                # 사진 시작 인덱스 찾기
                if self.a == "stop":
                    starts = [i for i in range(len(self.image_files)) if self.sec in self.image_files[i]]
                    print("시작후보는 ",starts)
                    if self.color == "green":
                        start = starts[0]
                    else:
                        start = starts[1]
                    print("시작은",start)
                    self.a = "go"
                else :
                    start = 0
                
                
                for i in range(start, 30):                    
                    # print(">>>>>>>>>>>>>>>>",self.image_files[i])
                    image = Image.open(self.image_files[i])
                    # Create a thumbnail that fits our screen
                    image.thumbnail((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                    self.matrix.SetImage(image.convert('RGB'))
                    time.sleep(1)
                    if self.eventElement == 1:
                        self.a = "stop"
                        break
                
                # 이벤트 여부에 따른 클래스 변수 초기화
                if self.eventElement == 0:
                    self.color = "green"
                    self.sec = "1"
                else:
                    self.eventElement = 0
        except KeyboardInterrupt:
            sys.exit(0)


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
    
    # b.odd()