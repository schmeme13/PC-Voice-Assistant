#pip install SpeechRecognition
#pip install pyttsx3
#pip install PyAudio
#pip install pywhatkit

#imports
import speech_recognition as sr
import pyttsx3
import pywhatkit

#declaring objects
listener = sr.Recognizer()
engine = pyttsx3.init()

#Adjust the allowance of seconds of silence before stopping
listener.pause_threshold = 2

#Where to change voice engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Microphone active. Listening...")
            voice = listener.listen(source, timeout=5)
            print("Voice captured. Recognizing...")
            command = listener.recognize_google(voice)
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

run()
