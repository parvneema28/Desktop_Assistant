import pyttsx3                      # text to speech conversion 
import speech_recognition as sr     # for recognizing what is being said 
import datetime                     # for getting the date and time
import webbrowser                   # for opening web browsers like google,youtube,facebook and many more
import wikipedia                    # for getting the content available on wikipedia
import os                           # for opening files present on the system



engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour <12):
        speak("Good Morning!")
        
    
    elif(hour>12 and hour<18):
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    speak("I am Joey. Please tell me how may I help you?")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        # Logic for exceuting tasks based on query
        if 'wikipedia' in query:
            # wikipedia.set_lang("hi")
            speak("Searching Wikipedia...") 
            query = query.replace("wikipedia","")               # replaces wikipedia with blank so that it does occur when we search for someone
            results = wikipedia.summary(query,sentences = 2)    # sentences = 2 means these many lines will be read by the assistant from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        
        elif 'open gmail' in query:
            speak("Opening gmail")
            webbrowser.open("gmail.com")
        
        elif 'play music' in query:
            speak("Playing music")
            music_dir = "C:\\Users\parvn\\Documents\\Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'what is the date today' in query:
            strDate = datetime.datetime.now().strftime("%d %b %Y")   # %b is for month name, %b is for month number, %a is for day
            speak(f"Today's date is {strDate}")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\parvn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'hey joey how are you' and 'how are you' in query:
            speak("Hello sir I am very good. what about you")

        elif 'quit' and 'stop' in query:
            speak("Quitting")
            break
            
