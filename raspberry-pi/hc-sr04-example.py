import RPi.GPIO as GPIO
import time
import sys

triggerPin = 7
echoPin = 11

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def main():
    try:
        while True:
            GPIO.output(triggerPin, GPIO.LOW)           # Set pin to LOW
            time.sleep(2)                               # Wait 2 seconds
    
            GPIO.output(triggerPin, GPIO.HIGH)          # Set pin to HIGH
            time.sleep(0.0001)                          # wait 10 microseconds (10us HIGH pulse)
            GPIO.output(triggerPin, GPIO.LOW)           # Set pin to LOW (End 10us HIGH pulse)

            while GPIO.input(echoPin) == 0:             # wait for input from echo. if low record time
                pulse_start = time.time()
            while GPIO.input(echoPin) == 1:             # wait for input from echo. if high record time
                pulse_end = time.time()

            duration = pulse_end - pulse_start          # Calculate time difference
            inches = (duration / 2) * 13503.9           # Convert to inches
            cm = (duration / 2) * 343 * 100             # Convert to centimeters

            # Display output to user.
            print("in: %0.2f\tcm: %0.2f" % (inches, cm))

    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)


if __name__ == '__main__':
    main()
    sys.exit(0)
sys.exit(0)
try:
    GPIO.setmode(GPIO.BOARD)

    triggerPin = 7
    echoPin = 11

    GPIO.setup(triggerPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

    GPIO.output(triggerPin, GPIO.LOW)

    time.sleep(2)

    GPIO.output(triggerPin, GPIO.HIGH)

    time.sleep(0.0001)

    GPIO.output(triggerPin, GPIO.LOW)

    while GPIO.input(echoPin)==0:
        pulse_start = time.time()
    while GPIO.input(echoPin)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150, 2)
    print "distance:", distance,"cm"
finally:
    GPIO.cleanup()
