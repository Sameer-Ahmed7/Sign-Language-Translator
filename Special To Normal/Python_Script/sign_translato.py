# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 07:33:14 2020

@author: Sameer Ahmed
"""

"""
Libraries Add
"""
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
#import speech_recognition as sr
import os

#PCA_9685
#from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

#Opencv Image show
import cv2

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
#servo_min = 150  # Min pulse length out of 4096
#servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    #pules =(pulse*2.5)+150 #Sameer edit
    
    
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

"""
Servo_name Pin
Servo-1    (0)
Servo-2    (1)
Servo-3    (2)
Servo-4    (3)
Servo-5    (4)
Servo-6    (6)
Servo-7    (7)
Servo-8    (9)
Servo-9    (10)
Servo-10   (8)
Servo-11   (12)
Servo-12   (15)
"""

def nice_to_meet_you():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/nice_to_meet_you.jpg')
    cv2.imshow('Nice To Meet You',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/nice_to_meet_you.jpg")
    deg = {0:450,1:200,2:275,3:200,4:625,6:275,15:600,9:200,10:200,8:200,12:625,7:300}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def thank_you():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/thank_you.jpeg')
    cv2.imshow('Thank You',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/thank_you.jpeg")
    deg = {0:325,1:600,2:275,3:525,4:300,6:600,15:275,9:550,10:500,8:600,12:200,7:225,}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def good_bye():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/goodbye.jpg')
    cv2.imshow('Good Bye',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/goodbye.jpg")
    deg = {0:100,1:200,2:575,3:200,4:600,6:275,15:275,9:550,10:500,8:200,12:200,7:475}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)
        
def hello():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/hello.jpg')
    cv2.imshow('Hello',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/hello.jpg")
    deg = {0:100,1:200,2:575,3:200,4:600,6:275,15:400,9:325,10:325,8:325,12:400,7:475,7:250}
    
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def yes():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/yes.jpeg')
    cv2.imshow('Yes',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/yes.jpeg")
    deg = {0:100,1:200,2:575,3:200,4:600,6:275,15:600,9:200,10:200,8:200,12:600,7:475}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def no():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/no.jpeg')
    cv2.imshow('No',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/no.jpeg")
    deg = {0:100,1:200,2:575,3:200,4:600,6:275,15:400,9:345,10:345,8:375,12:400,7:475}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def your_welcome():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/your_welcome.jpeg')
    cv2.imshow('Your Welcome',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/your_welcome.jpeg")
    deg = {0:100,1:200,2:575,3:200,4:600,6:275,15:400,9:325,10:325,8:325,12:400,7:250,7:475}
    
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)
    
def sorry():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/sorry.jpeg')
    cv2.imshow('Sorry',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/sorry.jpeg")
    deg = {0:100,1:200,2:575,3:200,4:600,6:275,15:600,9:200,10:200,8:200,12:600,7:200}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def good_morning():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/good_morning.jpeg')
    cv2.imshow('Good Morning',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/good_morning.gif")
    your_welcome()
    deg = {0:350,1:600,2:275,3:550,4:300,6:600,15:400,9:325,10:325,8:325,12:200,7:300}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)

def good_night():
    img = cv2.imread('/home/pi/FYP/Python_Script/Images/good_night.png')
    cv2.imshow('Good Night',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Image.open("/home/pi/FYP/Python_Script/Images/good_night.png")
    your_welcome()
    deg = {0:500,15:600,9:200,10:200,8:200,12:200,7:300,7:200}
    for channel, pulse in deg.items():
        pwm.set_pwm(channel, 0, pulse)
        time.sleep(5)


def Normal_To_Special():
    
    
    
    def textData():
        
        textData = text_data.get()
        text_data.delete(0,len(textData))
        print((textData))
        
        
        if textData.lower() == "nice to meet you":
            nice_to_meet_you()
        elif textData.lower() == "thank you":
            thank_you()
        elif textData.lower() == "good bye":
            good_bye()
            
        elif textData.lower() == "hello":
            hello()
            
        elif textData.lower() == "yes":
            yes()
            
        elif textData.lower() == "no":
            no()
        
        elif textData.lower() == "your welcome":
            your_welcome()
            
        elif textData.lower() == "sorry":
            sorry()
            
        elif textData.lower() == "good morning":
            good_morning()
            
        elif textData.lower() == "good night":
            good_night()
        combine_text = "You Enter : "+textData.lower()
        label4 = Label(window2,text=combine_text,bg="snow",fg="khaki4",font="Times 24 bold")
        label4.place(x=100,y=500)
        
        
    def useMic():
        
        
        print("Mic")
        
        import speech_recognition as sr
        import subprocess
        #record = ["arecord", "-f", "S32_LE", "-c1", "-r", "48000", "-D", "plughw:1,0", "-d", "5","record.wav"]
        record = ["arecord", "-D", "plughw:1", "-c1", "-r", "48000", "-f", "S32_LE","-d", "5","-t", "wav", "-V", "mono", "-v", "/home/pi/FYP/Python_Script/record.wav"]
        p = subprocess.Popen(record, stdout=subprocess.PIPE)
        r = sr.Recognizer()
        import time
        time.sleep(10)
        #speech = sr.Microphone(device_index=0)
        speech = sr.AudioFile('/home/pi/FYP/Python_Script/record.wav')
        with speech as source:
            print("say something!…")
            
            #audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        """
        with open("audio_file.wav", "wb") as file:
            file.write(audio.get_wav_data())"""
        try:
            recog = r.recognize_google(audio,language="en-US")
            print(recog)
            
            if recog.lower() == "nice to meet you":
                nice_to_meet_you()
            elif recog.lower() == "thank you":
                thank_you()
            elif recog.lower() == "good bye" or recog.lower() == "goodbye" :
                good_bye()
                
            elif recog.lower() == "hello":
                hello()
                
            elif recog.lower() == "yes":
                yes()
                
            elif recog.lower() == "no":
                no()
            
            elif recog.lower() == "your welcome":
                your_welcome()
                
            elif recog.lower() == "sorry":
                sorry()
                
            elif recog.lower() == "good morning":
                good_morning()
                
            elif recog.lower() == "good night":
                good_night()
                
            print("You said: " + recog)
        except sr.UnknownValueError:
            recog = "Something wrong please try again!"
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            recog = "Something wrong please try again!"
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        label4 = Label(window2,text=recog,bg="snow",fg="khaki4",font="Times 24 bold")
        label4.place(x=100,y=500)
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                comnine_text = " You Say :  "+text
                label4 = Label(window2,text=comnine_text,bg="snow",fg="khaki4",font="Times 24 bold")
                label4.place(x=100,y=500)
                
            except:
                print("Sorry could not recognize what you said")
                comnine_text = "Sorry could not recognize what you said"
                label4 = Label(window2,text=comnine_text,bg="snow",fg="red",font="Times 24 bold")
                label4.place(x=20,y=500)
            """    
            

        
    print("Normal_To_Special")
    window2 = Toplevel()
    window2.title("Normal To Special")
    window2.configure(background="snow")
    window2.geometry("600x600")
    if "nt" == os.name:
        window2.wm_iconbitmap(bitmap='/home/pi/FYP/Python_Script/sign-language.ico')
    else:
        window2.wm_iconbitmap(bitmap='@/home/pi/FYP/Python_Script/sign-language.xbm')
    #window2.iconbitmap('sign-language.ico')
    
    my_img = ImageTk.PhotoImage(Image.open("/home/pi/FYP/Python_Script/image.png"))
    my_label = Label(window2,image=my_img).pack()
    
    label = Label(window2,text="Real Time Sign-Translato",bg="snow",fg="saddle brown",font="Times 32 bold").pack()
    labe2 = Label(window2,text="Normal To Special",bg="snow",fg="saddle brown",font="Times 24 bold").pack()
    label3 = Label(window2,text="Enter Text :",bg="snow",fg="saddle brown",font="Times 16 bold")
    text_data = Entry(window2,borderwidth=2,font="Times 16 bold",bg="black",fg="snow")
    button_text = Button(window2,text="Enter",bg="saddle brown",fg="white",font="Times 16 bold",command=textData)#lambda:(textData(),window2.destroy())
    button_useMic = Button(window2,text="Use Mic",bg="saddle brown",fg="white",font="Times 22 bold",command=useMic)#lambda:(useMic(),window2.destroy())
    label3.place(x=100,y=370)
    text_data.place(x=220,y=350,width=200,height=50)
    button_text.place(x=430,y=360)
    
    button_useMic.place(x=100,y=420,width=400,height=50)
    window2.mainloop()




def Special_To_Normal():
    
    def openRaspCam():
        print("Camera Open")
        
    
    
    
    print("Special_To_Normal")
    window2 = Toplevel()
    window2.title("Special To Normal")
    window2.configure(background="snow")
    window2.geometry("600x600")
    if "nt" == os.name:
        window2.wm_iconbitmap(bitmap='/home/pi/FYP/Python_Script/sign-language.ico')
    else:
        window2.wm_iconbitmap(bitmap='@/home/pi/FYP/Python_Script/sign-language.xbm')
    #window2.iconbitmap('sign-language.ico')
    
    my_img = ImageTk.PhotoImage(Image.open("/home/pi/FYP/Python_Script/image.png"))
    my_label = Label(window2,image=my_img).pack()
    
    label = Label(window2,text="Real Time Sign-Translato",bg="snow",fg="saddle brown",font="Times 32 bold").pack()
    labe2 = Label(window2,text="Special To Normal",bg="snow",fg="saddle brown",font="Times 24 bold").pack()
    
    button_openRaspCam = Button(window2,text="Open Camera",bg="saddle brown",fg="white",font="Times 22 bold",command=openRaspCam)
    
    button_openRaspCam.place(x=200,y=370)
    
    window2.mainloop()

"""
Closing The Root Window
"""    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()    
    
    
root = Tk()
root.title("Real Time Sign Translato")
root.configure(background="snow")
root.geometry("600x600")

if "nt" == os.name:
    root.wm_iconbitmap(bitmap='/home/pi/FYP/Python_Script/sign-language.ico')
else:
    root.wm_iconbitmap(bitmap='@/home/pi/FYP/Python_Script/sign-language.xbm')
#root.iconbitmap('sign-language.ico')

my_img = ImageTk.PhotoImage(Image.open("/home/pi/FYP/Python_Script/image.png"))
my_label = Label(root,image=my_img).pack()
label = Label(root,text="Real Time Sign-Translato",bg="snow",fg="saddle brown",font="Times 32 bold").pack()
button_NormalToSpecial = Button(root,text="Normal To Special",bg="saddle brown",fg="white",font="Times 22 bold",command=Normal_To_Special)
button_SpecialToNormal = Button(root,text="Special To Normal",bg="saddle brown",fg="white",font="Times 22 bold",command=Special_To_Normal)
button_quit = Button(root,text="Exit Program",bg="saddle brown",fg="white",font="Times 12 bold",command=on_closing)

button_NormalToSpecial.place(x=170,y=300)
button_SpecialToNormal.place(x=170,y=370)
button_quit.place(x=250,y=500)
root.mainloop()