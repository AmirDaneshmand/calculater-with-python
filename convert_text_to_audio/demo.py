
from gtts import gTTS
import os

with open('demo.txt', 'r') as f:
    text = f.read()
# text = "today is a good day"

output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')  # اصلاح `sava()` به `save()`

os.system("mpg123 output.mp3")  # اجرای فایل صوتی
