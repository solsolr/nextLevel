import paho.mqtt.client as client

# mqttClient 객체가 갖고 있는 publish 이용하기
# publish는 메세지를 보내고 리턴값을 가지고 돌아온다.
# callback 함수도 실행 가능. 메세지 보내고 되돌아와서 처리해야되는 작업 있을때 사용

# 메시지 전송하고 다시 되돌아와서 실행될 callback 함수
def publish_ok(client, userdata, mid):
    print(client, userdata, mid)
    print("데이터전송완료- 메시지를 보내고 되돌아와서 처리할 일이 있는 경우, publish를 다양한 위치했을때 처리하고 싶은 일이 있는경우")
    

try:
    mqttClient = client.Client("python_pc_pub")
    mqttClient.connect("172.30.1.9", 1883)
    mqttClient.on_publish = publish_ok
    result = mqttClient.publish("iot/led", "led~~~~~~")
    print("호출결과>>", result) # result 값이 mid 값이다. mid 값으로 제어
    mqttClient.loop(2)
except Exception as err:
    print("에러", err)