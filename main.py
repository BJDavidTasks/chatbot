from itertools import takewhile

import pyttsx3
import datetime
import speech_recognition as sr


engine =pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("bonjour soufiane")
    speak("l'heure actuel est ")
    time()
    speak("la date d'aujourd'hui")
    date()
    speak("Esprit est votre assistant personnel intelligent. s'il vous plait dis-moi comment je peux vous aider?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="fr-FR" )
        print(query)
        speak("vous avez dit " + query)
        if "date" in query:
            date()
        if "time" in query:
            time()
        else :
            speak("désolé je peux pas exécuter ce que vous avez dit")

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

takeCommand()







