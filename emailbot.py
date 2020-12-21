from credentials import *  
import speech_recognition as sr
import smtplib
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine =pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('話してください：')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender,sender_pw)
    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'jack': '宛先@gmail.com'
    }

def get_email_info():
    talk('Who do you want to send na email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)

get_email_info()
    


