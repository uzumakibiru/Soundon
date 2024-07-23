from gtts import gTTS
from pdf import PDF

class TTS():
   
    
    def to_speech(self,text):
        self.tts=gTTS(text=text,tld="com.au",lang="en")
        

        self.tts.save(f"{text.split()[0]}.mp3")
        

