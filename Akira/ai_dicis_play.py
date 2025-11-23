from ai_dicis import Dicision
from ai_dicis_youtube import youtube 

SONG_DIR=None

class play(Dicision):
    def __init__(self) -> None:
        super().__init__()

    def dicisions(self, query: str) -> str:
        super().dicisions(query)
        
        if self.query_check(('youtube','song','movie', 'game'),query):
            dici = youtube.dicisions()
            return dici
        else:
            dici='play what'
            return dici

            
        
        