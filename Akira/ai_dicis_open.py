import webbrowser
from ai_dicis import Dicision
from ai_dicis_google import google
from ai_dicis_youtube import youtube


class Open(Dicision):
    def __init__(self) -> None:
        super().__init__()

    def dicisions(self, query: str) -> str:
        if 'youtube' in query:
            dici = youtube().dicisions(query)
            return dici
            
        elif 'google' in query:
            dici = google().dicisions(query)
            return dici

        elif 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            return "Indeed a great tool for class of programmer"

        elif self.query_check(('insta', 'instagram', 'reel'),query):
            webbrowser.open('instagram.com')
            return 'yeah, who doesn\'t enjoy some reels'

        elif 'facebook' in query:
            webbrowser.open('facebook.com')
            return 'Yep a great site to socialize'

            
