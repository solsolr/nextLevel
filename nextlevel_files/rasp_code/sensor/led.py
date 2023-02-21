import RPi.GPIO as gpio

class LED:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.led_pin = 19
        gpio.setup(self.led_pin, gpio.OUT)
    
    def led_on(self):
        gpio.output(self.led_pin, gpio.HTGH)
    
    def led_off(self):
        gpio.output(self.led_pin, gpio.LOW)
    
    def clean(self):
        gpio.cleanup()