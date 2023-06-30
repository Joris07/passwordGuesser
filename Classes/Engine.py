from .Options.Leet import LeetMin, LeetMaj, LeetAll
from .Options.Capitalize import ToCapitalize
from .Options.Upper import ToUpper
from .Options.Lower import ToLower
from .Options.Accents import RemoveAccents
from .Options.Characters import CommonCharacteres, AllCharacteres, NCharacters
from .Options.DateNumber import GetDayNumber, GetMonthNumber, GetYearNumber, GetYearNumber2Digits
from .Options.DateText import GetDayText, GetMonthText
import itertools
import random

class Engine:
	def __init__(self, words, dates, options, langs):
		self.options = options
		self.words = words
		self.dates = dates
		self.langs = langs
		self.listeFinal = self.run()
	
	def fct_addPossibilities(self, liste, in_words = True):
		if in_words:
			self.words = list(set(self.words + liste))
		else:
			self.dates = list(set(self.dates + liste))
   
	# Composition dans les fonctions fct_addPossibilities
	def run(self):
		if self.options["get_day_text"]:
			self.fct_addPossibilities(GetDayText(self.dates, self.langs).possibilites)
		if self.options["get_month_text"]:
			self.fct_addPossibilities(GetMonthText(self.dates, self.langs).possibilites)
		if self.options["get_day_number"]:
			self.fct_addPossibilities(GetDayNumber(self.dates).possibilites, False)
		if self.options["get_month_number"]:
			self.fct_addPossibilities(GetMonthNumber(self.dates).possibilites, False)
		if self.options["get_year_number"]:
			self.fct_addPossibilities(GetYearNumber(self.dates).possibilites, False)
		if self.options["get_year_number_two_digits"]:
			self.fct_addPossibilities(GetYearNumber2Digits(self.dates).possibilites, False)
		if self.options["to_capitalize"]:
			self.fct_addPossibilities(ToCapitalize(self.words).possibilites)
		if self.options["to_upper"]:
			self.fct_addPossibilities(ToUpper(self.words).possibilites)
		if self.options["to_lower"]:
			self.fct_addPossibilities(ToLower(self.words).possibilites)
		if self.options["remove_accents"]:
			self.fct_addPossibilities(RemoveAccents(self.words).possibilites)
		if self.options["common_characteres"]:
			self.fct_addPossibilities(CommonCharacteres(self.words).possibilites)
		if self.options["all_characteres"]:
			self.fct_addPossibilities(AllCharacteres(self.words).possibilites)
		if self.options["n_characteres"]:
			self.fct_addPossibilities(NCharacters(self.words, self.options["n_characteres"]).possibilites)
		if self.options["leet_min"]:
			self.fct_addPossibilities(LeetMin(self.words).possibilites)
		if self.options["leet_maj"]:
			self.fct_addPossibilities(LeetMaj(self.words).possibilites)
		if self.options["leet_all"]:
			self.fct_addPossibilities(LeetAll(self.words).possibilites)

		finalList = random.sample(self.words + self.dates, 10)
		#finalList = self.words + self.dates
		returnList = []
		for i in range(1, len(finalList) + 1):
			for p in itertools.permutations(finalList, i):
				returnList.append("".join(p))
		return returnList