import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 7
ECHO = 11

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10µs pulse
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound = 343 m/s

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
