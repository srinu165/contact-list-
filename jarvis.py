

import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit
import webbrowser

from speech_recognition import Microphone

engine = pyttsx3.init()
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices",voices[1].id)
def say(audio):
    engine.say(audio)
    engine.runAndWait()

    return audio
def takeCommand():
    r = sr.Recognizer()
    source: Microphone
    with sr.Microphone() as source:

        r.pause_threshold =0.5

        audio = r.listen(source)
       # print("Recognizing...")
        try:
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            return "some error occured sorry from jarvis"


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
    say("Hello boss!")
    wish()
    while True:
        print("Say something")
        query = takeCommand()
        say(query)


        query = takeCommand()
        sites = [['YouTube','https://www.youtube.com'],['Google','https://www.google.com'],['Facebook','https://www.facebook.com'],['instagram','https://www.instagram.com'],['my portal','http://tkrec.in//student//']]
        for site in sites:

            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir....")
                webbrowser.open(site[1])
        if 1:
            if "hi jarvis" in query.lower():
                say(f"hi krishna sir....")
            elif "jarvis" in query.lower():
                say(f"hi srinu  sir....")


            elif "hello jarvis" in query.lower():
                say(f"hello aaneel sir....")
            elif "how are you" in query.lower():
                say(f"I am fine. How are you?")
            elif "email password" in query.lower():
                say(f"9908584745 sir....")
            elif "open music" in query.lower():
                musicPath = "C:\\Users\Srinivas\\Music\\MEmu Music\\[iSongs.info] 01 - Chirunama Thana Chirunama.mp3"
                os.startfile(musicPath)
            elif "open photo" in query.lower():
                photoPath ="C:\\Users\Srinivas\\Pictures\\Screenshots\\Screenshot 2024-05-15 130434.png"
                os.startfile(photoPath)
            elif ("good night") in query.lower():
                say(f"good night madam....")

            else:
                say(f"say it again")






