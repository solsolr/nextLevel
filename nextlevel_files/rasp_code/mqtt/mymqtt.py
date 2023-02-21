# callback - 구독신청 후 broker와 접속이 완료됐을때, broker가 보낸 메시지가 도착했을때
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher
from threading import Thread
from ..sensor.led import LED
from mysensor import PirSensor

class MqttWorker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.connect_result
        self.client.on_message = self.on_message
        self.myled = LED()
        self.pir = PirSensor(self.client) # 클라이언트 객체를 넣어줘야 publisher가 호출을 한다.
        self.pir.start() # 쓰레드임으로 start 해줘야함.


    # client(subscriber)가 broker에 접속이 완료된 경우 호출
    def connect_result(self, client, userdata, flags, rc):    #rc가 0이면 접속 성공, 1이면 실패
        print("connect...." + str(rc))
        if rc ==0:
            client.subscribe("iot/#") # 구독신청 - iot/시작하는 토픽은 모두 구독하겠다는 의미
        else:
            print("연결실패...")

    def on_message(self, client, userdata, message):
        myval = message.payload.decode('utf-8')
        print(myval)
        if myval == "led_on":
            self.myled.led_on()
            print("on")
        elif myval == "led_off":
            self.myled.led_off()
            print("off")

    # 사용자 전용 함수
    def mqtt_connect(self):
        try:
            # broker에 접속하기
            self.client.connect("172.30.1.9", 1883, 60)
            mythreadobj = Thread(target=self.client.loop_forever)
            mythreadobj.start()
        except KeyboardInterrupt:
            pass
        finally:
            pass
