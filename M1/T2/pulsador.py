import RPi.GPIO as GPIO

LED = 24
PULSADOR = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(PULSADOR, GPIO.IN)

while True:
    if GPIO.input(PULSADOR) == True:
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
