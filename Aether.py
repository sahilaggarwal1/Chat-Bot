import pyttsx3
import datetime
import wikipedia
import os
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Evening !")
    elif hour >= 18 and hour <= 0:
        speak("Good Night !")

    speak("I am Aether. Tell me how can i help you.")


def takeCommand():
    r = sr.Recognizer(language='en-in')
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize(audio)
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while (True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipeadia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipeadia")
            print(result)
            speak(result)
        elif 'youtube' in query:
            webbrowser.open(f"youtube.com")

        elif 'play music' in query:
            music_dir = "D:\\Favourite Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            nowTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(nowTime)
            print(f"The time is :{nowTime}")

        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            exit()
