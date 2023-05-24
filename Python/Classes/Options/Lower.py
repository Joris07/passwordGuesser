class Lower:
    def __init__(self, words):
        self.words = words
        self.possibilites = self.run()
    
    def run(self):
        return [word.lower() for word in self.words]
    
class ToLower(Lower):
    def __init__(self, words):
        super().__init__(words)