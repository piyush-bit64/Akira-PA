import webbrowser
from ai_dicis import Dicision

try:
    from pywhatkit import playonyt
except Exception:
    pass


class youtube(Dicision):
    def __init__(self) -> None:
        super().__init__()

    def dicisions(self, query: str) -> str:
        if 'on' in query:
            lis=query.split(' ')
            self.remove_words(lis,'open','youtube','on')
            query=''
            query=self.join_word(lis,query)
            playonyt(query)

            return f'opening {query} on youtube'

        elif 'song' in query:
            lis = query.split(' ')
            self.remove_words(lis,'youtube','on')
            query=''
            query=self.join_word(lis,query)
            playonyt(query)

            return f'opening {query} on youtube'

        else:
            webbrowser.open('youtube.com')


