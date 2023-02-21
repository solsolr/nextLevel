'''
<LED 제어하기>
- LED불켜기, 불끄기
- 라즈베리파이가 subscriber
message가 led_on이 오면 : led켜기
message가 led_off가 오면 : led끄기
- Application(PC=CMD)가 publisher
키보드로 입력받은 메시지를 publish
'''

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

led_pin = 24
# GPIO핀을 어떤 방법으로 액세스할 것인지 모드를 설정
GPIO.setmode(GPIO.BCM)
# GPIO핀이 입력인지 출력인지 설정하기
GPIO.setup(led_pin,GPIO.OUT)

def connect_result(client, userdata, flags, rc):
    print("connect.."+str(rc))  # rc가 0이면 접속 성공, 1이면 실패
    if rc==0:  # 연결 성공하면, 구독신청
        client.subscribe("iot/#")  # iot/로 topic명이 시작하면 뒤에는 어떤 키워드가 와도 모두 수신
    else:
        print("연결 실패..")

def on_message(client, userdata, message):
    myvalue = message.payload.decode("utf-8")
    print(message.topic+"---"+myvalue)
    if myvalue == "led_on":
        GPIO.output(led_pin, GPIO.HIGH)  # 24번으로 출력 
    else:
        GPIO.output(led_pin, GPIO.LOW)  # 24번으로 출력 

try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    # mqttClient.on_message = on_message  # 메시지가 broker에서 전달됐을 때, callback함수가 호출되도록 등록
    mqttClient.connect("172.30.1.78",1883,60)
    mqttClient.loop_forever()  # 등록한 topic의 메시지를 broker에서 전송받아야 하므로 대기
except KeyboardInterrupt:
    pass
finally:
    pass