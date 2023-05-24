from .Words import Words

class Lower(Words):
	def __init__(self, words):
		super().__init__(words)

	def run(self):
		return [word.lower() for word in self.words]
	
class ToLower(Lower):
	def __init__(self, words):
		super().__init__(words)