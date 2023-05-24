class Date:
	def __init__(self, dates, index = False):
		self.dates = dates
		self.index = index
		self.possibilites = self.run()
	
	def run(self):
		if self.index != False and self.index in [0, 1, 2]:
			return [(date.split("-")[self.index]) for date in self.dates]
	
class GetDay(Date):
	def __init__(self, dates):
		super().__init__(dates, 2)

class GetMonth(Date):
	def __init__(self, dates):
		super().__init__(dates, 1)

class GetYear(Date):
	def __init__(self, dates):
		super().__init__(dates, 0)