class Dicision():
    def __init__(self) -> None:
        pass

    def dicisions(self, query: str) -> str:
        RuntimeError('Function should be overrided')
    
    def remove_words(self,lst: list,*args: str):
        for word in args:
            try:
                lst.remove(word)
            except Exception:
                pass

    def join_word(self, lst: list | tuple, stri: str):
        for word in lst:
            stri+=' '+word
        return stri

    def query_check(self, iter: list | tuple, query: str):
        checker = False
        for word in iter:
            if word in query:
                checker = True
        return checker

