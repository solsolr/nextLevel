# callback - 구독신청 후 broker와 접속이 완료됐을때, broker가 보낸 메시지가 도착했을때
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher
from threading import Thread, Event
# from yolov5 import main4
from bohangClass3 import Bohang


class MqttWorker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.connect_result
        self.client.on_message = self.on_message
        # 보행자 신호 객체 생성
        self.b = Bohang()
        # self.t = Thread(target=self.b.basic, daemon=True)
        # self.t.start()


    # client(subscriber)가 broker에 접속이 완료된 경우 호출
    def connect_result(self, client, userdata, flags, rc):    #rc가 0이면 접속 성공, 1이면 실패
        print("connect...." + str(rc))
        if rc ==0:
            client.subscribe("iot/#") # 구독신청 - iot/시작하는 토픽은 모두 구독하겠다는 의미
            # main4.mm
        else:
            print("연결실패...")
        

    def on_message(self, client, userdata, message):
        myval = message.payload.decode('utf-8')
        print(myval)
        myvals = myval.split()
        
        if myvals[0] == "green":
            # self.b.event.set() # 기본 보행자 신호 중지 됨.
            # self.b.event.clear() # 내부 플래그 초기화.
            self.b.color = myvals[0]
            self.b.sec = myvals[1]
            self.b.eventElement = 1
            print("green")
        elif myvals[0] == "red":
            # self.myled.led_off()
            self.b.color = myvals[0]
            self.b.sec = myvals[1]
            self.b.eventElement = 1
            print("red")

    # 사용자 전용 함수
    def mqtt_connect(self):
        try:
            # broker에 접속하기
            self.client.connect("172.30.1.99", 1883, 60)
            mythreadobj = Thread(target=self.client.loop_forever)
            mythreadobj.start()
        except KeyboardInterrupt:
            pass
        finally:
            pass
