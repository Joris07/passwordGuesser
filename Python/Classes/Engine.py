from .Config import Config
from .Options.Leet import LeetMin, LeetMaj, LeetAll
from .Options.Capitalize import ToCapitalize
from .Options.Upper import ToUpper
from .Options.Lower  import ToLower
from .Options.Accents import RemoveAccents
from .Options.Characters import CommonCharacteres, AllCharacteres, NCharacters
from .Options.Date import GetDay, GetMonth, GetYear

class Engine:
	def __init__(self, words, dates, options):
		self.options = options
		self.words = words
		self.dates = dates
		self.run()
	
	def fct_addPossibilities(self, liste, in_words = True):
		if in_words:
			self.words = list(set(self.words + liste))
		else:
			self.dates = list(set(self.dates + liste))

	def run(self):
		if self.options["get_day"]:
			self.fct_addPossibilities(GetDay(self.dates).possibilites, False)
		if self.options["get_month"]:
			self.fct_addPossibilities(GetMonth(self.dates).possibilites, False)
		if self.options["get_year"]:
			self.fct_addPossibilities(GetYear(self.dates).possibilites, False)
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
		# 
		# Leet à la fin