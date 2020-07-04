import os
import time
import playsound
import speech_recognition as sr
import chess
from gtts import gTTS

PieceDict = {
    'Knight' : 'N',
    'Bishop' : 'B',
    'Rook' : 'R',
    'Queen' : 'Q',
    'King' : 'K',
    'Pawn' : ''
}

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "audio/temp.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        spoken = ""

        try:
            spoken = r.recognize_google(audio)
            #print(spoken)
        except Exception as e:
            print("Exception: " + str(e))

    return spoken

#Gets the move and converts it to the proper format
def get_move():
    playerSaid = "".join(get_audio().lower().split())

    #print(f'I heard: {playerSaid.strip()}')

    return playerSaid.strip()