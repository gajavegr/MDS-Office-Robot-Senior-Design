import RPi.GPIO as GPIO
import time

LED_PIN = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT,initial=GPIO.LOW)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()