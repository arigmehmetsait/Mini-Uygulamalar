# Deneme adindaki txt dosyasini sesli bir şekilde okutabiliriz.

from gtts import gTTS
import os


dosya = open("deneme.txt","r").read()
konusma = gTTS(text = dosya, lang = 'tr',slow = False)
konusma.save("deneme.mp3")
os.system("deneme.mp3")