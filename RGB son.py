from guizero import App, Slider, TextBox, Text, PushButton
import RPi.GPIO as GPIO
import random

def change_red(redslider_value):
    red = redslider_value

redpin=3
bluepin=5
greenpin=7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(bluepin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)

pwm_redled = GPIO.PWM(redpin,500)
pwm_redled.start(100)
pwm_blueled = GPIO.PWM(bluepin,500)
pwm_blueled.start(100)
pwm_greenled = GPIO.PWM(greenpin,500)
pwm_greenled.start(100)


def change_red(redslider_value):
    brightness = (redslider_value)
    duty = int(brightness)
    pwm_redled.ChangeDutyCycle(duty)

def change_blue(blueslider_value):
    brightness = (blueslider_value)
    duty = int(brightness)
    pwm_blueled.ChangeDutyCycle(duty)
    
def change_green(greenslider_value):
    brightness = (greenslider_value)
    duty = int(brightness)
    pwm_greenled.ChangeDutyCycle(duty)
    
def dancebaby ():
    
        
            brightnessred = (random.randint(0,100))
            brightnessblue = (random.randint(0,100))
            brightnessgreen = (random.randint(0,100))
            dutyred = int(brightnessred)
            dutyblue = int(brightnessblue)
            dutygreen = int(brightnessgreen)
            pwm_redled.ChangeDutyCycle(dutyred)
            pwm_blueled.ChangeDutyCycle(dutyblue)
            pwm_greenled.ChangeDutyCycle(dutygreen)
            
            
            

app = App()
text= Text(app, text="Red Slider", color="blue")
redslider = Slider(app, command=change_red)
text2= Text(app, text="Blue Slider", color="green")
blueslider = Slider(app, command=change_blue)
text3= Text(app, text="Green Slider", color="red")
greenslider = Slider(app, command=change_green)
pushbutton = PushButton(app, command=dancebaby)

app.display()


