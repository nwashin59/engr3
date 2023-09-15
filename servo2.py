import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo
btn = DigitalInOut(board.D3) #connecting the button to pin 3
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN #this is my new pull down resistor

btn2 = DigitalInOut(board.D4) #connecting the button to pin 4
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN #this is my new pull down resistor

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

angle = 90

while True:
    if btn.value and angle<178:
        print(angle) #when the botton is pushed down
        angle = angle +5
        my_servo.angle = angle
   

    if btn2.value and angle>5:
        print(angle) #if the button is pushed the servo will move
        angle = angle - 5
        my_servo.angle = angle
   
    '''
for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02)
   '''     
    time.sleep(0.1) # sleep for debounce