import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MotorEnable = 22  # Enable Pin
MotorInput1 = 27  # Input Pin
MotorInput2 = 17  # Input Pin

GPIO.setup(MotorEnable, GPIO.OUT)
GPIO.setup(MotorInput1, GPIO.OUT)
GPIO.setup(MotorInput2, GPIO.OUT)
def motor_off():
 GPIO.output(MotorEnable, GPIO.LOW)
 GPIO.cleanup()

def motor_on():
 GPIO.output(MotorEnable, GPIO.HIGH)
 GPIO.output(MotorInput1, GPIO.LOW)
 GPIO.output(MotorInput2, GPIO.HIGH)


# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
# fix