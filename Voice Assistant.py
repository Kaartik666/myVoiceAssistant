import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # generate speech from a given text.
    engine.runAndWait()
# runAndWait() - This command ensures that the speech is played completely before the program continues executing.


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("I am Jack sir. Please tell me how may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1     # wait for 1 second to listen to user
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')  # taking audio input from user and converts it into string.
        print(f"User said: {query}\n")

    except Exception:
        print("Say that agin please....")
        return "None"

    return query


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music = 'C:\\Users\\shaar\\Desktop\\songs'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[random.randint(1, len(songs) - 1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir the time is {strTime}')
        else:
            if 'stop' in query:
                StopIteration()
                break
