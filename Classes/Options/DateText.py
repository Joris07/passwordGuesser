import re
from .Date import Date
from babel.dates import format_date, format_datetime
from datetime import datetime

class DateText(Date):
	def __init__(self, dates, langs, formatDate):
		self.langs = langs
		self.formatDate = formatDate
		super().__init__(dates)
	
	def run(self):
		la_tableau = []
		for date in self.dates:
			if re.match("^[\d]{4}-[\d]{2}-[\d]{2}$", date):
				for lang in self.langs:
					formatted = format_date(datetime.strptime(date, '%Y-%m-%d'), format=self.formatDate, locale=lang)
					la_tableau.append(formatted)
			else:
				continue
		return la_tableau

	@property
	def langs(self):
		return self.__langs

	@langs.setter
	def langs(self, langs):
		self.__langs = langs

	@property
	def formatDate(self):
		return self.__formatDate

	@formatDate.setter
	def formatDate(self, formatDate):
		self.__formatDate = formatDate
	
class GetDayText(DateText):
	def __init__(self, dates, langs):
		super().__init__(dates, langs, 'EEEE')

class GetMonthText(DateText):
	def __init__(self, dates, langs):
		super().__init__(dates, langs, 'MMMM')