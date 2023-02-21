import paho.mqtt.publish as publisher

def showMenu():
    print("#######원하는 작업을 선택하세요########")
    print("1. led켜기")
    print("2. led끄기")
    print("3. 종료하기")
    
if __name__ == "__main__":
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