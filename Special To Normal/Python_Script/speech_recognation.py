# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:52:03 2020

@author: Sameer Ahmed
"""
     
"""
import speech_recognition as sr

r = sr.Recognizer()
mic =sr.Microphone(device_index=1)
with mic as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
"""

import speech_recognition as sr
import subprocess
#record = ["arecord", "-f", "S32_LE", "-c1", "-r", "48000", "-D", "plughw:1,0", "-d", "5","record.wav"]
record = ["arecord", "-D", "plughw:1", "-c1", "-r", "48000", "-f", "S32_LE","-d", "5","-t", "wav", "-V", "mono", "-v", "record.wav"]
p = subprocess.Popen(record, stdout=subprocess.PIPE)
r = sr.Recognizer()
import time
time.sleep(10)
#speech = sr.Microphone(device_index=0)
speech = sr.AudioFile('record.wav')
with speech as source:
    print("say something!…")
    
    #audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
"""
with open("audio_file.wav", "wb") as file:
    file.write(audio.get_wav_data())"""
try:
    recog = r.recognize_google(audio,language="en-US")

    print("You said: " + recog)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

"""

import pyttsx3
import speech_recognition as sr
import pyaudio
#from gpiozero import LED

for i, mic_name in enumerate (sr.Microphone.list_microphone_names()):
    print("mic: " + mic_name)
    if "USB Audio Device" in mic_name:
        print("USB Audio Devic " + mic_name)
        mic = sr.Microphone(device_index=i, chunk_size=1024, sample_rate=48000)


pi_ear = sr.Recognizer()
pi_mouth = pyttsx3.init()

while True:
    need_speak = False
    with mic as source:
        # pi_ear.pause_thpi_eareshold=1
        pi_ear.adjust_for_ambient_noise(source, duration=0.5)
        print("\033[0;35mpi: \033[0m I'm listening")
        audio = pi_ear.listen(source)
    try:
        you = pi_ear.recognize_google(audio)
    except:
        you = ""
    msg = you
    print(msg)
    
    print("\033[0;32myou:\033[0m " + you)
    print("\033[0;35mpi:\033[0m " + msg)
    if need_speak == True:
        pi_mouth.say(msg)
        pi_mouth.runAndWait()
        


import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


"""













