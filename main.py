#pip install SpeechRecognition
#pip install pyttsx3
#pip install PyAudio
import speech_recognition as sr


listener = sr.Recognizer()
print("Recognizer initialized.")

try:
    print("Attempting to use microphone...")
    with sr.Microphone() as source:
        print("Microphone active. Listening...")
        voice = listener.listen(source, timeout=5, phrase_time_limit=10)
        print("Voice captured. Recognizing...")
        command = listener.recognize_google(voice)
        print(f"Command: {command}")
except Exception as e:
    print(f"An error occurred: {e}")
