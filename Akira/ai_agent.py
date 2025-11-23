'''
This file contains the parent class of the sub-models or there sub-classes
'''

import pyttsx3
import speech_recognition as sr

STAND_BY = 0
LISTENING = 1
SPEAKING = 2
NO_INTERNET = 4

FEMALE=1
MALE=0

class AI():
    def __init__(self) -> None:

        self.exit=False
        
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.voice = self.genVoice(self,FEMALE)
        
        self.mic = sr.Microphone()
        self.recog = sr.Recognizer()        

        # setting SR Properties
        self.recog.pause_threshold = 1

        self.mode = None


    def speak(self, audio) -> any:
        '''Text -> Speech
        Function makes model speak the words in arguments using the default outlets
        '''
        if audio == None:
            audio=''
        if 'EXIT' in audio:
            self.engine.say('Bye')
            self.engine.runAndWait()

            self.mode = 44

            self.exit=True
                        
        else:
            self.mode = SPEAKING
            self.engine.say(audio)
            self.engine.runAndWait()

            self.mode = STAND_BY
            print('Akira - ', audio)
            return audio

    @staticmethod
    def genVoice(self, voice_ind=0) -> str:
        '''Function for: Voice indexing and Choosing voice of the model '''
        
        if voice_ind not in (0,1):
            RuntimeError('voice index out of range')

        self.engine.setProperty('voice', self.voices[voice_ind].id)

        return FEMALE if voice_ind==1 else MALE

    
    def takeCom(self) -> str:
        '''Speech -> String
        Function takes command from the user from the default inlets once called.'''
        self.mode = LISTENING
        r = self.recog
        with self.mic as source:
            print('Listening...')
            self.recog.adjust_for_ambient_noise(source)

            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-us')
                self.mode = STAND_BY
                
                return query
            
            except sr.UnknownValueError:
                self.mode = STAND_BY
                return 'UnknownValueError'

            except sr.RequestError:
                self.mode = NO_INTERNET
                return 'RequestError'

            except:
                self.mode = 44
                return 'UnknownError'
                
    
    def check_for_error(self, sig):
        if sig == 'RequestError':
            self.speak('No Internet Connection available, please turn it on to proceed')

        elif sig == 'UnknownValueError':
            self.speak('Say that again please, i wasnt able to listen that')


    def current_mode(self)->str:
        if self.mode==0:
            return 'Stand By'
        
        elif self.mode==1:
            return 'Listening...'
        
        elif self.mode == 3:
            return 'Speaking...'
        
        elif self.mode == 4:
            return 'No Internet'
        else:
            return 'Switched Off'