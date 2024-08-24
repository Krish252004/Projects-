import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

print("Initializing Speakify")
MASTER = "Krishna"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    print(hour)
    if hour >= 0 and hour < 12:
        speak("Good morning " + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good afternoon " + MASTER)
    else:
        speak("Good evening " + MASTER)
    speak("I am your assistant. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
        except sr.WaitTimeoutError:
            print("Sorry, you did not say anything.")
        return None



def main():
    speak("Initializing Speakify...")
    wishMe()
    query = takeCommand()

    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        url = "https://www.youtube.com"
        webbrowser.open(url)

    elif 'open google' in query.lower():
        url = "https://www.google.com"
        webbrowser.open(url)

    elif 'play music' in query.lower():
        songs_dir = "E:\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER}, the time is {strTime}")


if __name__ == "__main__":
    main()
