from ai_dicis import Dicision
from datetime import *

class Time(Dicision):
    def __init__(self) -> None:
        super().__init__()
    
    def dicisions(self, query: str) -> str:
        if 'date' in query:
            date=datetime.now().date()
            return f'today\'s date is {date}'
        
        elif 'time' in query:
            dici=datetime.now().time()
            return f'current time is {dici}'
