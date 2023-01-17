# IMPORTING REQUIRED MODULES

import pyttsx3
import datetime
import speech_recognition as SR
import pyaudio
import wikipedia
import webbrowser
import os
import subprocess
import speedtest
#import smtplib

engine = pyttsx3.init('sapi5')
Assistant_voices = engine.getProperty('voices')            # getting available assistant voices
engine.setProperty('voice',Assistant_voices[1].id)         # Setting Voice

def Speak(audio):                                          # Speaking Function
    engine.say(audio)
    engine.runAndWait()

def Greet():                                               # Greeting function
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        Speak('Good Morning')
    elif hour>=12 and hour<18:
        Speak('Good Afternoon')
    else:
        Speak('Good Evening')

def Listen():                                              # hearing function

    temp = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        temp.pause_threshold = 1
        audio = temp.listen(source)
    try:                                                           # try block --> if assistant was able to listen
        print("Recognizing")
        Speech = temp.recognize_google(audio,language='en-in')
        print("You said",Speech)   
    except Exception as e:                                         # except block --> if assistant hears nothing
        Speak("did you say something??")
        print("say it again please...")
        return"None"
    return Speech

if __name__=="__main__":
   intro='I am Jarvis, and i am your Assistant. Please tell me how may i help you.'
   Greet()
   Speak(intro)



   # listening user commands until user stops
   while(True):
    Speech = Listen().lower()   # user command --> converting to lower to match with the queries
     
    # Logic to Execute tasks
    if 'wikipedia' in Speech:
        Speak('Searching in Wikipedia...')
        Speech = Speech.replace("wikipedia","")
        result = wikipedia.summary(Speech,sentences=2)
        print(result)
        Speak("According to wikipedia")
        Speak(result)
    elif 'how are you' in Speech:
        Speak('I am Good ')
    elif 'who are you' in Speech:
        Speak(intro)

    elif 'open youtube' in Speech or 'start youtube' in Speech:
        Speak('starting youtube')
        webbrowser.open('youtube.com')
    elif 'open google' in Speech or 'start google' in Speech:
        Speak('opening google')
        webbrowser.open('google.com')
    elif 'open gmail' in Speech or 'open my inbox' in Speech:
        Speak('opening your gmail')
        webbrowser.open('gmail.com')
    elif 'open my github profile' in Speech or 'github' in Speech:
        Speak('opening github')
        webbrowser.open('github.com')
    elif 'hackerrank' in Speech or 'hackerrank dashboard' in Speech:
        Speak('opening hackerrank')
        webbrowser.open('hackerrank.com')

    elif 'brave' in Speech:
        Speak('opening brave')
        subprocess.Popen('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
    elif 'google chrome' in Speech or 'open chrome' in Speech:
        Speak('opening google chrome')
        subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    elif 'open vs code' in Speech or 'start code' in Speech or 'open code' in Speech:
        Speak('starting visual studio code')
        subprocess.Popen('D:\\Microsoft VS Code\\Code.exe') 
    elif 'open word' in Speech or 'ms word' in Speech:
        Speak('opening microsoft word')
        subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe')
    elif 'powerpoint' in Speech or 'ppt' in Speech:
        Speak('opening microsoft powerpoint')
        subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe')
    elif 'open excel' in Speech or 'ms excel' in Speech:
        Speak('opening microsoft excel')
        subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.exe')
    elif 'outlook' in Speech:
        Speak('opening outlook')
        subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.exe')
    
    elif 'current time' in Speech or 'time' in Speech:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        Speak(f"the time is {time}")
    
    elif 'network speed' in Speech or 'speed test' in Speech:
        network = speedtest.Speedtest()
        D = network.download()
        U = network.upload()
        print("Download -->",D)
        print("Upload -->",U)
        Speak(f"Here is your network download and upload speed")

    elif 'close' in Speech or 'exit' in Speech or 'quit' in Speech:
       Speak("thank you, it was nice talking to you. Have a great day.")
       break
    print()
