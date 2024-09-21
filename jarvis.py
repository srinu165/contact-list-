import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
def say(audio):
    engine.say(audio)
    engine.runAndWait()
    return audio
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.pause_threshold = 0.5
        audio = r.listen(source)
        # print("Recognizing...")
        try:
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            return "some error occured .srry from jarvis"


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning!")
    elif hour>=12 and hour<18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    say("I am Jarvis tell me how can I help you!")

if __name__ == '__main__':
    say("Hello srinu!")
    wish()
    while True:
        print("Say something")
        query = takeCommand()
        say(query)


        query = takeCommand()
        sites = [['YouTube','https://www.youtube.com'],['Google','https://www.google.com'],['Facebook','https://www.facebook.com'],['instagram','https://www.instagram.com']]
        for site in sites:

            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir....")
                webbrowser.open(site[1])
