from Config_object import Config
from datetime import datetime
from babel.dates import format_date, format_datetime

class Liste_date:
	def __init__(self, liste_initiale):
		self.liste_initiale = liste_initiale
		self.liste_finale = liste_initiale[:]
		self.config = Config()

	def fct_getListeInitiale(self):
		return self.liste_initiale
	
	def fct_getListeFinale(self):
		return self.liste_finale
	
	def fct_extractDaysOrMonthsOrYears(self, index): # 0 -> Année | 1 -> Mois | 2 -> Jour
		for date_1 in self.liste_initiale:
			self.liste_finale.append(date_1.split("-")[index])

	def fct_extractYearIn2Digits(self):
		for date in self.liste_initiale:
			self.liste_finale.append(date.split("-")[0][-2]+date.split("-")[0][-1])
	
	def fct_separateDateNumbers(self):
		for date in self.liste_initiale:
			self.liste_finale += date.split("-")

	def fct_monthInLetters(self, lang):
		for date in self.liste_initiale:
			date_obj = datetime.strptime(date, '%Y-%m-%d')
			month_formatted = format_date(date_obj, format='MMMM', locale=lang)
			self.liste_finale.append(month_formatted)
    
	def fct_daysInLetters(self, lang):
		for date in self.liste_initiale:
			date_obj = datetime.strptime(date, '%Y-%m-%d')
			weekday_formatted = format_datetime(date_obj, format='EEEE', locale=lang)
			self.liste_finale.append(weekday_formatted)