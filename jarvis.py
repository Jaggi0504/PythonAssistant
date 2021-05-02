import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import cv2
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Your_email_id', 'Your_password')
    email = EmailMessage()
    email['From'] = 'Your_email_id'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'jay': 'singh.jagdeep0504@gmail.com',
}

def get_email_info():
    speak('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('Please tell the subject')
    subject = get_info()
    talk('Please tell the message')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Email sent successfully, Do you want to send more mails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hey, Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Hey, Good Afternoon!")
    else:
        speak("Hey, Good Evening!")
    speak("I am your assistant. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.non_speaking_duration = 0.1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please!")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('What do you want to watch on YouTube?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak!")
                audio = r.listen(source)
                try:
                    print("Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

                except Exception as e:
                    print("Unable to recognize, Sorry!")

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'portfolio' in query:
            webbrowser.open('https://jaggi0504.github.io/deploy-react1')

        elif 'song' in query:
            webbrowser.open('https://music.youtube.com')

        elif 'email' in query:
            get_email_info()

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            speak("Press q to capture the image and escape button to quit")
            while cap.isOpened():
                k = cv2.waitKey(33)
                ret, back = cap.read()
                if ret:
                    cv2.imshow("image", back)
                    if cv2.waitKey(5) & 0xFF == ord('q'):
                        cv2.imwrite('image.jpg', back)
                    elif k == 27:
                        cap.release()
            cv2.destroyAllWindows()