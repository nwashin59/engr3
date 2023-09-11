import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit motor import servo
btn = DigitalInOut(board.D3)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D4)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
while True:
    if btn.value:
        print("BTN1 is down")
    else:
        print("BTN1 is up")
        pass

    if btn2.value:
        print("BTN2 is down")
    else:
        print("BTN2 is up")
        pass

for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02)
        
    time.sleep(0.1) # sleep for debounce