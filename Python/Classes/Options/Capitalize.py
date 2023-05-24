from .Words import Words

class Capitalize(Words):
    def __init__(self, words):
        super().__init__(words)
    
    def run(self):
        return [word.capitalize() for word in self.words]
    
class ToCapitalize(Capitalize):
    def __init__(self, words):
        super().__init__(words)
        


