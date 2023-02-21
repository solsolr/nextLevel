import paho.mqtt.publish as publisher

# single은 서버로 한 번 메세지 보내고 연결을 끊는다.
publisher.single("iot", "led_on", hostname="172.30.1.9")


# 계속 무한루프로 값 보내는 코드

# import datetime as dt
# import paho.mqtt.client as mqtt

# count = 0

# # mqtt publisher
# broker_address="192.168.123.194"
# client2 = mqtt.Client("ClientPublisher")
# client2.connect(broker_address)


# while True:

#     count += 1
#     time = dt.datetime.now().strftime("%M%S.%f")
#     pub_data = "{0},{1}".format(count, time)


#     # mqtt publisher
#     client2.publish("vds1/data", pub_data)