import RPi.GPIO as GPIO
import time

LED = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)

for i in range(10):
    GPIO.output(LED, True)
    time.sleep(2)
    GPIO.output(LED, False)
    time.sleep(2)
    
GPIO.cleanup()