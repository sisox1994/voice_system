from flask import Flask
from flask import request #載入Request物件
from flask import render_template
from flask import redirect
import RPi.GPIO as GPIO
import os


Ctrl_Pin = 16 #this is pin number!!! not GPIO number
Ctrl_Pin_2 = 18 #this is pin number!!! not GPIO number

global light_sw 
light_sw = 0

def Ctrl_Pin_ini():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(Ctrl_Pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(Ctrl_Pin_2, GPIO.OUT, initial=GPIO.HIGH)


def Swith_ON():
    GPIO.output(Ctrl_Pin,GPIO.HIGH)
    GPIO.output(Ctrl_Pin_2,GPIO.HIGH)

def Swith_OFF():
    GPIO.output(Ctrl_Pin,GPIO.LOW)    
    GPIO.output(Ctrl_Pin_2,GPIO.LOW) 

Ctrl_Pin_ini()

app = Flask(
    __name__,
    static_folder='static',    
    static_url_path='/' ,
    template_folder='template'
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit')
def submit_func():
    #name = request.args.get("Name","")  #對應html name 參數
    #age  = request.args.get("Age","")


    global light_sw 
    if(light_sw == 0):
        light_sw = 1
        Swith_ON()
    elif(light_sw == 1):
        light_sw = 0
        Swith_OFF()


    #age  = request.args.get("Age","")

    return render_template("index.html")

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=80, debug=True)