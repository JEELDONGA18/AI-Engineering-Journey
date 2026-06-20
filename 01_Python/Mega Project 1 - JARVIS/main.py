import requests
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from gtts import gTTS
import pygame
import os

recognize= sr.Recognizer()  # for recognize our sppech(command)
engine = pyttsx3.init()         # for initializing our pyttsx3
newsapi='3f197f2809094f58b4f628ccc0dd3f67' # for giving me a news
 
def speak_old(text):    # This is speak function which carry text for speaking
    engine.say(text)    # by this text will speak
    engine.runAndWait()  # this is for helping giving audi  o of speaking text

def speak(text):
    tts=gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def processCommand(c):
    # print(c)
    if 'open google' in c.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://youtube.com')
    elif 'open linkedin' in c.lower():
        webbrowser.open('https://linkedin.com')
    elif 'open unacademy' in c.lower():
        webbrowser.open('https://unacademy.com')
    elif 'open facebook' in c.lower():
        webbrowser.open('https://facebook.com')
    elif c.lower().startswith('play'):
        song=c.lower().split(' ')[1]  # this takes song name which is after the play word.
        link=musicLibrary.music[song]
        webbrowser.open(link)
        
    elif 'news' in c.lower():
        r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}')
        if r.status_code == 200:
            data = r.json()  # Parse the JSON response
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])  # Print the title of each article
                
    else:
        # Let OpenAI handle the request
        pass

if __name__=='__main__': # this means this module is not imported from the other 
    speak('Initializing Jarvis..')
    
    while True:
        #Listen for the wake word 'Jarvis'
        #obtain audio from the microphone
        r=sr.Recognizer()    
        print('recognizing...')
        
        try:
            with sr.Microphone() as source: # sr package provide Microphone function and we access it by source
                print('Listening...')
                audio=r.listen(source,timeout=10,phrase_time_limit=1)  # timeout= total listening time and phrase_time_limit=total delay time
            word=r.recognize_google(audio)  # for recognize our wake(initializing the jarvis) word
            if (word.lower()=='jarvis'): # for response of the jarvis
                speak('Ya sir')
                # Listen for the command
                with sr.Microphone() as source:  # for checking jarvis is active or not
                    print('Jarvis active')
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
    
                    processCommand(command)

            
        except sr.UnknownValueError:  # If command is not recognize command then raise error
            print('Sorry sir!! I could not understand audio')
        except sr.RequestError as e:  # If above exception is not working than it will raise an error.
            print('error; {}'.format(e))