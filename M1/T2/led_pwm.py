import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 24

GPIO.setup(led, GPIO.OUT)

led_pwm = GPIO.PWM(led, 100)
print("100")
led_pwm.start(100)

time.sleep(20)
print("50")
led_pwm.ChangeDutyCycle(50)
time.sleep(20)
print("20")
led_pwm.ChangeDutyCycle(20)
time.sleep(20)

led_pwm.stop()
GPIO.cleanup()
