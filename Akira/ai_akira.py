from datetime import datetime
from ai_agent import AI,NO_INTERNET
from ai_dicis_conver import conversation
from ai_dicis_on import On
from ai_dicis_open import Open
from ai_dicis_play import play
from ai_dicis_time import Time

class akira(AI):
    def __init__(self) -> None:
        self.initialize()
        
        
    def ask(self) -> None:

        self.query = self.takeCom().lower()
        print('User - ',self.query)

        if self.query == 'requesterror':
            self.speak('Please Connect to a stable internet connection')
            self.mode=NO_INTERNET
            self.exit=True

        elif self.query == 'unknownvalueerror':
            self.query=''
            self.speak('please, repeat that again sir')
            self.speak('i didn\'t listen it, carefully')

        elif self.query is None:
            self.query=''
            self.speak('please, repeat that again sir')
            self.speak('i didn\'t listen it')

        elif 'play' in self.query:
            dici=play().dicisions(self.query)
            self.speak(dici)
        
        elif 'open' in self.query:
            dici=Open().dicisions(self.query)
            self.speak(dici)
        
        elif 'on' in self.query:
            dici = On().dicisions(self.query)
            self.speak(dici)
        
        elif 'what' in self.query:
            dici = Time().dicisions(self.query)
            self.speak(dici)
        
        else:
            dici = conversation().dicisions(self.query)
            self.speak(dici)


    def initialize(self):
        super().__init__()
        self.name = 'Akira'
        self.query = ''

    def wish(self) -> str:
        hour = int(datetime.now().hour)
        
        if 0<= hour <12:
            return 'what,a sweet morning sir, what are your orders'

        elif 12<=hour<18:
            return 'Good afternoon sir, what should i do for you'
        
        else:
            return 'Hello sir, how can i serve you'


