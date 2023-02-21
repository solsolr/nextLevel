# pc에서 실행되는 Application이 pub/sub 역할을 해야 한다.
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher
import threading

# client(subscriber)가 broker에 접속이 완료된 경우 호출
def connect_result(client, userdata, flags, rc):    #rc가 0이면 접속 성공, 1이면 실패
    print("connect...." + str(rc))
    if rc ==0:
        client.subscribe("test") # 구독신청 - iot/시작하는 토픽은 모두 구독하겠다는 의미
    else:
        print("연결실패...")

def on_message(client, userdata, message):
    myval = message.payload.decode('utf-8')
    print(myval)


def showMenu():
    print("#######원하는 작업을 선택하세요########")
    print("1. led켜기")
    print("2. led끄기")
    print("3. 종료하기")        

def menu_run():
    while True:
        showMenu()
        num = int(input("원하는 작업을 선택하세요"))
        led_state = ""
        if num == 1:
            led_state = "led on"
        elif num == 2:
            led_state = "led_off"
        else:
            exit(0)
        publisher.single("iot/led", led_state, hostname="172.30.1.9")


try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message
    
    # broker에 접속하기
    mqttClient.connect("172.30.1.9", 1883, 60)
    obj = threading.Thread(target=menu_run) # 쓰레드 사용해서 무한 루프 돌리기
    obj.start()
    mqttClient.loop_forever()
    
except KeyboardInterrupt:
    pass
finally:
    pass