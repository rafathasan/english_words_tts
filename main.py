from gtts import gTTS
import os
import random

lang = 'en'
words = []
words_index = []
save_filename = 'tts.mp3'
with open('words.txt', 'rb') as f:
    words = f.readlines()

random.shuffle(words)

for text in words:
    text = text.decode("utf-8")
    print(text.strip())
    gTTS(text=text, lang=lang, slow=0).save(save_filename)
    os.system(f"mpg321 -q {save_filename} > /dev/null 2>&1")
