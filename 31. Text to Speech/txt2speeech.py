# Day 31: Text to speech

# pip install pygame
# pip install gtts
# install these modules before running this program

import io
import pygame
from gtts import gTTS

def speak(text):
    with io.BytesIO() as file:
        gTTS(text=text, lang="en").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file)
        sound.play()
        while pygame.mixer.get_busy():
            continue

if __name__ == '__main__':
    text = input("write here what you want me to say >")
    speak(text)
