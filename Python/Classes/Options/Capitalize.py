class Capitalize:
    def __init__(self, words):
        self.words = words
        self.possibilites = self.run()
    
    def run(self):
        return [word.capitalize() for word in self.words]
    
class ToCapitalize(Capitalize):
    def __init__(self, words):
        super().__init__(words)
        


