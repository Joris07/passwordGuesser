from .Date import Date
import re

class DateNumber(Date):
	def __init__(self, dates, index, twoDigits = False):
		self.index = index
		self.twoDigits = twoDigits
		super().__init__(dates)
	
	def run(self):
		la_tableau = []
		if self.index in [0, 1, 2]:
			for date in self.dates:
				if re.match("^[\d]{4}-[\d]{2}-[\d]{2}$", date):
					if self.twoDigits:
						la_tableau.append(date.split("-")[self.index][-2]+date.split("-")[self.index][-1])
					else:
						la_tableau.append(date.split("-")[self.index])
				else:
					continue
		return la_tableau
		
	@property
	def index(self):
		return self.__index

	@index.setter
	def index(self, index):
		self.__index = index
		
	@property
	def twoDigits(self):
		return self.__twoDigits
 
	@twoDigits.setter
	def twoDigits(self, twoDigits):
		self.__twoDigits = twoDigits
	
class GetDayNumber(DateNumber):
	def __init__(self, dates):
		super().__init__(dates, 2)

class GetMonthNumber(DateNumber):
	def __init__(self, dates):
		super().__init__(dates, 1)

class GetYearNumber(DateNumber):
	def __init__(self, dates):
		super().__init__(dates, 0)

class GetYearNumber2Digits(DateNumber):
	def __init__(self, dates):
		super().__init__(dates, 0, True)