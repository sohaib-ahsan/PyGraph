import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
def male_female(ind):
    engine.setProperty('voice', voices[ind].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("Greetings! I am Py graph, How may i help you?")


def takecommand(c):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"User said: {text}\n")
    except:
        speak("Kindly Say that again...")
        c.delete('listen')
    return text

def proceed():
    speak('Do you want to Proceed')

#wishme()
#takecommand()