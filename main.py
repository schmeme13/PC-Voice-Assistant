#pip install SpeechRecognition
#pip install pyttsx3
#pip install PyAudio

#imports
import speech_recognition as sr
import pyttsx3 as tts

#declaring objects
listener = sr.Recognizer()
engine = tts.init()

#Where to change voice engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Synthesis
try:
    print("Attempting to use microphone...")
    with sr.Microphone() as source:
        print("Microphone active. Listening...")
        voice = listener.listen(source, timeout=5, phrase_time_limit=10)
        print("Voice captured. Recognizing...")
        command = listener.recognize_google(voice)
        
        engine.say(command)
        engine.runAndWait()
except Exception as e:
    print(f"An error occurred: {e}")
