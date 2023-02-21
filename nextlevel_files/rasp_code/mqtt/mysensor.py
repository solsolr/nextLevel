import paho.mqtt.client as mqtt
import time
from threading import Thread
import RPi._GPIO as gpio

# Thread 클래스 상속 받음
class PirSensor(Thread):
    # 생성자
    def __init__(self, client):
        super().__init__()
        gpio.setmode(gpio.BCM)
        self.pir_pin = 27
        gpio.setup(27, gpio.IN)
        self.client = client
        
    # run 메소드 오버라이딩
    def run(self):
        try:
            while True:
                if gpio.input(self.pir_pin) == 1:
                    print("motion detected....")
                    self.client.publish("pir", "motion detected")
                else:
                    print("no motion....")
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            pass