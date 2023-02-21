# callback - 구독신청 후 broker와 접속이 완료됐을때, broker가 보낸 메시지가 도착했을때
import paho.mqtt.client as mqtt

# client(subscriber)가 broker에 접속이 완료된 경우 호출
def connect_result(client, userdata, flags, rc):    #rc가 0이면 접속 성공, 1이면 실패
    print("connect...." + str(rc))
    if rc ==0:
        client.subscribe("iot/#") # 구독신청 - iot/시작하는 토픽은 모두 구독하겠다는 의미
    else:
        print("연결실패...")

def on_message(client, userdata, message):
    myval = message.payload.decode("utf-8")  # 디코딩 utf-8만
    print(myval)


try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message

    # broker에 접속하기
    mqttClient.connect("192.168.123.103", 1883, 60)
    mqttClient.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    pass
