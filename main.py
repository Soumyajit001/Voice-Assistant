import pyttsx3
import speech_recognition as sr
# import pyaudio
from selenium_web import *
from yt import *
from info import *

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# engine.say("Hey!! How Can I help you?")
# engine.runAndWait()
# engine.stop()
#
r = sr.Recognizer()
speak("hello Sir..!! It's your voice assistant. How are you?")
with sr.Microphone() as source:
    r.energy_threshold = 10000     # If we increase the value of energy_threshold it will captures low voices also.
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

# if "what" and "about" and "you" in text:
#     speak("I am also having a good day sir...")
speak("What can I do for you??")

with sr.Microphone() as source:
    r.energy_threshold = 10000     # If we increase the value of energy_threshold it will captures low voices also.
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "give" and "some" or "details" in text2:
    speak("Okk sir..")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # If we increase the value of energy_threshold it will captures low voices also.
        r.adjust_for_ambient_noise(source, 1.2)
        print(text2)
        print("listening...")
        audio = r.listen(source)
        information = r.recognize_google(audio)
    speak("searching {} in google".format(information))
    assist = google()
    assist.get_google_info(information)


elif "information" in text2:
    speak("Sure sir, you need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # If we increase the value of energy_threshold it will captures low voices also.
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)


elif "play" and "song" or "video" in text2:
    speak("Okk sir, you want me to play which video??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # If we increase the value of energy_threshold it will captures low voices also.
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print("Playing {} on Youtube".format(vid))
        assist = music()
        assist.play(vid)

