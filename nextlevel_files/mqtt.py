import paho.mqtt.publish as publisher

publisher.single("study","hellohello",hostname="172.30.1.78")     #주제, 메시지, 브로커ip