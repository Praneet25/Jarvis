import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Morning!")
    speak(" I'm Jarvis , How can i help you?")

def takecommand():
    #it takes command from user's microphone and store it as a string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising..")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    
    except Exception as e:
        
        print("Say that again please..")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("email adress","password")
    server.sendmail("email address",to,content)


if __name__ == "__main__":
    
    speak("Hello Praneet")
    Wishme()
    
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia',"")
            results= wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia:")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir ="C:\\Users\\Praneet\\Downloads\\Music"
            files = os.listdir(music_dir)
            num = random.randint(0,len(files)-1)
            os.startfile(os.path.join(music_dir,files[num]))
        
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sirthe time is {time}")
        
        elif "open studio" in query:
            file_path = "C:\\Users\\Praneet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(file_path)
        
        elif "send email" in query:
            try:
                speak("What should i say")
                content = takecommand()
                to = "praneetkshd180@gmail.com"
                sendEmail(to,content)
                speak("Your email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry my master , I was not able to send the mail")
        
        elif "close program" in query:
            speak("It was my pleasure assisting you , bye!")
            exit()