#this program is for Text-to Speech in python
import gtts
from gtts import gTTS
import os

my_message='Hello this is text to speech sample'
my_val=gtts.gTTS(text=my_message,slow=False,lang='en')
my_val.save('testmessage3.mp3')
os.system('testmessage3.mp3')
