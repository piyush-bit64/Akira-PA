from ai_dicis import Dicision
from ai_dicis_youtube import youtube
from ai_dicis_google import google


class On(Dicision):
    def __init__(self) -> None:
        super().__init__()

    def dicisions(self, query: str) -> str:
        if 'youtube' in query:
            dici = youtube().dicisions(query)
            
            return dici
        
        elif 'google' in query:
            dici = google().dicisions(query)
            return dici
        
            

