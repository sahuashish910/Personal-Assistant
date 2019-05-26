import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        print("Good Morning sir")
        speak("Good Morning sir")

    elif hour>=12 and hour<17:
        print("Good Afternoon sir")
        speak("Good Afternoon sir")

    elif hour>=17 and hour<19:
        print("Good Evening sir")
        speak("Good Evening sir") 

    else:
        print("Good Night sir")
        speak("Good Night sir")

    print("I am your Personal Assistant. Please tell me how may I help you\n")
    speak("I am your Personal Assistant. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

def takeSearch():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        key = r.recognize_google(audio, language='en-in')
        print(f"User said: {key}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return key

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            result = wikipedia.summary(query, sentences=1)
            print("According to Wikipedia : ")
            speak("According to Wikipedia")
            print(results,"\n")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.get(('C:/Users/Admin/AppData/Local/Google/Chrome/Application/chrome.exe %s')).open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.get(('C:/Users/Admin/AppData/Local/Google/Chrome/Application/chrome.exe %s')).open("facebook.com")

        elif 'open chrome' in query:
            os.startfile("C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")

        elif 'search' in query:
            print("Enter your query\n")
            speak("Enter your query")
            key = takeSearch().lower()
            address = 'http://www.google.com/#q='
            word=key
            new=address+word
            webbrowser.get(('C:/Users/Admin/AppData/Local/Google/Chrome/Application/chrome.exe %s')).open(new)
            
        elif 'weather' in query:
            print("Enter location\n")
            speak("Enter location")
            key = takeSearch().lower()
            webbrowser.get(('C:/Users/Admin/AppData/Local/Google/Chrome/Application/chrome.exe %s')).open('http://www.google.com/#q='+key)
  
        elif 'play music' in query:
            music_dir = 'D:\\New'
            songs = os.listdir(music_dir)
            print(songs,"\n")    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play sacred games first episode' in query:
            music_dir = 'C:\\Users\\Admin\\Videos\\Movies\\SERIES\\SACRED GAMES'
            songs = os.listdir(music_dir)
            print(songs,"\n")    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir, the time is ",strTime,"\n")
            speak(f"Sir, the time is {strTime}")

        elif 'open photos' in query:
            path="D:\\pythonpicture"
            os.startfile(path)

        elif 'who are you' in query:
            print("I'm Ashish Sahu's Personal Assistant. I can help you find answers, play music and video, open photos and get things done easily.\n")
            speak(f"I'm Ashish Sahu's Personal Assistant. I can help you find answers, play music and video, open photos and get things done easily.")

        elif 'ashish sahu' in query:
            print("I'm his Personal Assistant.\n")
            speak("I'm his Personal Assistant.")
            
        elif 'thank you and exit' in query:
            print("No problem sir, and have a nice day\n")
            speak("No problem sir, and have a nice day")
            sys.exit()

        else:
            print("Sorry sir please repeat again\n")
            speak("Sorry sir please repeat again")
   
