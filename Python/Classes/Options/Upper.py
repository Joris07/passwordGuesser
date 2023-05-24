class Upper:
    def __init__(self, words):
        self.words = words
        self.possibilites = self.run()
    
    def run(self):
        return [word.upper() for word in self.words]
    
class ToUpper(Upper):
    def __init__(self, words):
        super().__init__(words)