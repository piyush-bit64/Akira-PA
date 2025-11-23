from ai_dicis import Dicision

try:
    from pywhatkit import search, info


except Exception:
    pass

class google(Dicision):
    def __init__(self) -> None:
        super().__init__()

    def dicisions(self, query: str) -> str:
        if 'on' in query:
            
            lis=query.split(' ')
            self.remove_words(lis,'open','google','on')
            query=''
            query=self.join_word(lis,query)

            
            query_info=info(query)

            if query_info is not None:
                return f'This is what I found: {query_info}'
            else:
                search(query)
                return f'searching google for {query}'

