import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

def b_speak(audios):
    tts = gTTS(text=audios, lang='en')
    audio = 'audio.mp3'
    tts.save(audio)
    playsound.playsound(audio)
    print(audios)
    os.remove(audio)
    
def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            b_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en")
        except sr.UnknownValueError:
            b_speak("Sorry i did not get that") 
        except sr.RequestError:
            b_speak("sorry service is down")
        return voice_data.lower()

def respond(voice_data):
    if 'الاسم' in voice_data or 'اسم' in voice_data:
        b_speak('مريومة القمورة')
    if 'الوقت' in voice_data or 'الساعه' in voice_data:
        b_speak(ctime)
    """if 'بحث' in voice_data or 'البحث' in voice_data:
        search = record('')
        url = '' + search
        webbrowser.get().open(url)
        b_speak(''+ search)"""
    
    if 'exit' in voice_data:
        exit()
b_speak('can i help you')        
while 1:
    voice_data = record()
    respond(voice_data)            


                               
    

