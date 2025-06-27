import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")
    speak("I am your Assistant")
    speak("Jarvis 1 point o")

def username():
    speak("What should I call you, sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    print(f"Welcome Mr. {uname}")
    speak("How can I Help you, Sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Unable to Recognize your voice.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'play music' in query:
            speak("Here you go with music")
            music_file = "E:\\My pixels\\K For Kabaradakkam  Guruvayoorambala Nadayil  Prithviraj  Basil  Asal Kolaar  Ankit Menon.mp3"
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "")
            webbrowser.open(query)
        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Shutting down the system")
            subprocess.call('shutdown /p /f')
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptied")
        elif "where is" in query:
            query = query.replace("where is", "").strip()
            speak(f"User asked to Locate {query}")
            webbrowser.open(f"https://www.google.com/maps/place/{query}")
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera", "img.jpg")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "write a note" in query:
            speak("What should I write, sir?")
            note = takeCommand()
            with open('jarvis.txt', 'w') as file:
                file.write(note)
            speak("Note written successfully")
        elif "show note" in query:
            speak("Showing Notes")
            with open("jarvis.txt", "r") as file:
                content = file.read()
                print(content)
                speak(content[:6])
        elif "weather" in query:
            api_key = "your_api_key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            speak("Which city?")
            city_name = takeCommand()
            complete_url = f"{base_url}{city_name}&appid={api_key}"
            response = requests.get(complete_url)
            x = response.json()
            if x.get("cod") != "404":
                y = x.get("main", {})
                current_temperature = y.get("temp", "N/A")
                current_pressure = y.get("pressure", "N/A")
                current_humidity = y.get("humidity", "N/A")
                weather_description = x.get("weather", [{}])[0].get("description", "N/A")
                speak(f"Temperature: {current_temperature}, Pressure: {current_pressure}, Humidity: {current_humidity}, Description: {weather_description}")
            else:
                speak("City Not Found")
