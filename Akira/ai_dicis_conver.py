from ai_dicis import Dicision

class conversation(Dicision):
    def __init__(self) -> None:
        super().__init__()

    def dicisions(self, query: str) -> str:
        super().dicisions(query)
        
        if query == None:
            return 'sorry I was unable to listen that'
            
        elif self.query_check(('hello', 'hi', 'namaste'), query):
            return 'hello, sir'
        
        elif self.query_check(('who are you', 'your name'), query):
            return 'My name is Akira, here to make you lazy'

        elif 'what are you' in query:
            return 'your freindly companion'

        elif 'am i looking' in query:
            return 'if only i could see how you are looking, but you must have good looks' 

        elif self.query_check(('exit','bye'),query):
            return 'EXIT'
        
        elif 'akira' in query:
            return 'Yes sir, i am present right here'
        else:
            return 'I am afraid i didnt understand that'
        