import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
def say(text):
    os.system(f"say {text} ")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Saagar"

if __name__ == '__main__':
    say("Hello I am Sagar A.I, How May I help You?")
    while True:
        print("listiening.....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = "/Users/sagar/Downloads/music121.mp3"
            os.system(f"open {musicPath}")
        elif "the time" in query:
            musicPath = "/Users/sagar/Downloads/Ed Sheeran - Perfect _RingTone_ (320 kbps).mp3"
            hour_12 = datetime.datetime.now().strftime("%l").strip()
            min = datetime.datetime.now().strftime("%M")
            am_pm = datetime.datetime.now().strftime("%p")
            say(f"Sir, the time is {hour_12}  {min} minutes {am_pm}")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open Calculator".lower() in query.lower():
            os.system(f"open /System/Applications/Calculator.app")


        elif "Sagar exit".lower() in query.lower():
            exit()
