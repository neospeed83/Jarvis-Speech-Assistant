import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
import time
from time import ctime

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak("Sorry I did not get that")
        except sr.RequestError:
            alexis_speak("My server is down")
        return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('my name is Jarvis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'stop' in voice_data:
        exit()


time.sleep(1)
alexis_speak('hi, How can I help you?')
while True:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
