# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---
## distance sensor 

### Description & Code Snippets
In this assignment, we used a distance sensor to make a light change color. The light changed colors by how far my hand was from the sensor. My serial monitor printed off "KEIRA F'ed up" to show that it was working and saw my hand.

```python
#josh and computer
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 1.0  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance < 5:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255, 0,0)
                pixels.show()
        if sonar.distance > 5 and sonar.distance < 20:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, (sonar.distance - 5 / 15 * 255))
                pixels.show()
             
        if sonar.distance > 20 and sonar.distance < 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, (sonar.distance - 5 / 15 * 255), 255-(sonar.distance - 5 / 15 * 255))
                pixels.show()
        if sonar.distance > 35:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = ( 0, 255, 0)
                pixels.show()  
    except RuntimeError:
        print("KEIRA F'ed up")
    time.sleep(0.1)  

```



### Evidence
![image1 (1)](https://github.com/nwashin59/engr3/assets/143545685/25693227-4e1e-4b4a-a05e-ee9fcb81c4b7)



And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection



## Hello_CircuitPython

### Description & Code Snippets


```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.

![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
In conclusion, this was kinda easy but my serial monitor wasn't listening to my sensor which was very annoying. I at first thought it was my wiring so I unwired and rewired just for that not to be the problem. lastly, I thew a fit and of course, and Mr.Helmstetter fixed it!! Turns out it was something in my code.


## CircuitPython_Servo

### Description & Code Snippets
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

```

**Lastly, please end this section with a link to your code or file.**  


### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.

![image0 (1)](https://github.com/nwashin59/engr3/assets/143545685/55e82e88-701e-413e-a3e1-b5b30b43a577)


Here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**


## CircuitPython_LCD

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  


### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)


### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**





## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

## NextAssignment ONSHAPE 

## HANGER

### Assignment Description
This assignment was to get back in the feel of onshape. we used things like Extrude, sketch, fillet, and mating, etc.

### Part Link 
[ONSHAP LINK](https://cvilleschools.onshape.com/documents/45a9fb19e83d9993db54c31d/w/9740a8f8d38a0a33e7753d6b/e/27caf1af251b6bed86f38b9e?renderMode=0&uiState=65381066db79bb4ed4d81d)2d

## Onshape_Assignment_Template


### Evidence

![Hanger](https://github.com/nwashin59/engr3/assets/143545685/d8d1f170-9a7c-4d8e-961f-eadf97344339)

### Reflection
on the hanger assignment It was the first assignment reintroducing onshape. we used almost all the tools we would need on onshape to build our own project. But, I will say the most challenging thing was holes. I struggle with circles because for one I don't enjoy walking, drawing, or onshaping circles, So it was definitely difficult. in all seriousness, This whole assignment was hard because it had been a minute since we did onshape and I can't lie I forgot what I was doing.


## NextAssignment
#SWING ARM

### Assignment Description
In this assignment, we had a video to follow and it was actually much easier for me.
### Part Link 
https://cvilleschools.onshape.com/documents/63fdd7a24c6198cc0edb6fcf/w/202c4bfa74ce090cfb622653/e/a72190d31616af386856877b?renderMode=0&uiState=653abb394e90d9537ed2535e 
### Evidence
![swing arm](https://github.com/nwashin59/engr3/assets/143545685/313b599e-8def-4fc7-a420-abb1da7ae6b8)

### Reflection
This assignment was easier for me because I had got the hang of onshape and I also had the video. but what was challenging was the dimensions. It was hard for me because I started my sketch on the wrong plan and It made my life harder. in conclusion, I didn't have to draw as many circles so I'd say it's a win-win!!

Rotary Encoder & LCD
CODE
import rotaryio
import time
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None
menu = ["stop", "caution", "go"]
last_index = None
menu_index = 0

while True:
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None
    menu_index = enc.position
    #if last_index == None or menu_index != last_index:
        #print(menu_index)
    menu_index_lcd = menu_index % 3
    #print(menu_index_lcd)
    menu[menu_index_lcd]
    print(menu[menu_index_lcd])
    time.sleep(0.2)
    lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    lcd.set_cursor_pos(1,0)
    lcd.print("          ")
    lcd.set_cursor_pos(1,0)
    lcd.print(menu[menu_index_lcd])
    if menu_index_lcd == 0:
     led[0] = (255, 0, 0)
    if menu_index_lcd == 1:
     led[0] = (255, 255, 0)
    if menu_index_lcd == 2:
     led[0] = (0, 255, 0)

![image0 (3)](https://github.com/nwashin59/engr3/assets/143545685/2a5c24ed-2cdf-4c29-8dbf-6cd6174c0b7c)


IR SENSOR
