import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser

engine = pyttsx3.init('sapiS')
voices= engine.getproperty('voices')
print(voices)
engine.setproperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning guys")
    elif hour>=12 and hour<=20:
        speak("Good afternoon")
    else:
        speak("Good Night")
    speak("Hi Emma here, how can I help you?")
def take():
    # It takes microphone input from user and returns a str output
     r= sr.Recognizer() 
     with sr.microphone as source:
        print("Listening")
        r.pause_threshold = 2 
        audio= r.listen(source)
    try:    
        print("Recognizing")
        query= r.recognize_google(audio, language='en uk')
        print(f"User said: {query}\n")
    except Exception as error:    
        print("Say that again please")
        return "none"
    return query

if __name__ == "__main__":
    speak("Hi")
    wish()
    while True:
        query= take().lower()
        if wikipedia in query:
            speak("Searching wikipedia")
            query= query.replace(wikipedia, "")
            results= wikipedia.summary(query,sentences=2)
            speak=("As per wikipedia ")
            print(results)
            speak(results)
        elif open_youtube in query: 
             webbrowser.open("youtube.com") 
