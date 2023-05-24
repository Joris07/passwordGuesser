from Liste_date_object import Liste_date
from Liste_mot_object import Liste_mot
from Classes.Engine import Engine

options = {
    "leet_min": True,
    "leet_maj": False,
    "leet_all": False,
    "to_capitalize": False,
    "to_upper": False,
    "to_lower": False,
    "remove_accents": False,
    "common_characteres": False,
    "all_characteres": False,
    "n_characteres": False,
    "get_day_number": False,
    "get_month_number": False,
    "get_year_number": False,
    "get_day_text": True,
    "get_month_text": False,
    "get_year_number_two_digits": False
}

words = [
    "Arthur",
    "éolienne"
]

langs = [
    "FR",
    "EN"
]

dates = [
    "2022-02-09",
    "2023-08-21",
    "2022-06-10"
]

engine = Engine(words, dates, options, langs)
#print(engine.dates)
print(engine.listeFinal)
print(len(engine.listeFinal))


#liste_date.fct_extractDaysOrMonthsOrYears(0)
#liste_date.fct_separateDateNumbers()
#liste_date.fct_extractYearIn2Digits()
#liste_date.fct_monthInLetters("FR")
#liste_date.fct_daysInLetters("EN");
#print(liste_date.fct_getListeFinale())

#liste_mot.fct_toCapitalize()
#liste_mot.fct_toLower()
#liste_mot.fct_toUpper()
#liste_mot.fct_removeAccents()
#liste_mot.fct_stringToL33t()
#liste_mot.fct_addRandomCommonSpecialCharacters()
#liste_mot.fct_addAllRandomSpecialCharacters()
#liste_mot.fct_addAllRandomSpecialCharactersLimitNb(5)
#print(liste_mot.fct_getListeFinale())


