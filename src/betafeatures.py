from typing import Text
import pyttsx3
engine = pyttsx3.init()

textsr = input('Text: ')

engine.say(f'{ textsr }')

engine.runAndWait()