import pyttsx3
import pyaudio
import speech_recognition as sr

#Listen to our microphone and return the audio as text using google

def transform():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 0.8
    said = r.listen(source)
    try:
        q = r.recognize_google(said, language="ar")
        return q
    except sr.UnknownValueError:
      print("Sorry I didn't understand")
      return "I'm waiting"
    except sr.RequestError:
      print("Sorry the service is down")
      return "I'm waiting"

print(transform())