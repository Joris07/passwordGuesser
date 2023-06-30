from Classes.Engine import Engine
from Classes.Config import Config

options = {
    "leet_min": True,
    "leet_maj": True,
    "leet_all": True,
    "to_capitalize": True,
    "to_upper": True,
    "to_lower": True,
    "remove_accents": True,
    "common_characteres": True,
    "all_characteres": True,
    "n_characteres": True,
    "get_day_number": True,
    "get_month_number": True,
    "get_year_number": True,
    "get_day_text": True,
    "get_month_text": True,
    "get_year_number_two_digits": True
}

words = [
    "titi",
    "tutu"
]

langs = [
    Config.get_default_language()
]

dates = [
    "0001-01-01"
]

engine = Engine(words, dates, options, langs)
#print(engine.dates)
print(engine.listeFinal)
print(len(engine.listeFinal))