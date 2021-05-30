import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
print(voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()