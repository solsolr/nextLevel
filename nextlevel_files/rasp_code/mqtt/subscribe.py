import paho.mqtt.client as mqtt



# subscriber callback

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)



# subscriber

broker_address="172.30.1.34"
client1 = mqtt.Client("ClientSubscriber")
client1.connect(broker_address)
client1.subscribe("vds1/data")
client1.on_message = on_message
client1.loop_forever()