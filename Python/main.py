from Liste_date_object import Liste_date
from Liste_mot_object import Liste_mot

items_date = ["2022-01-07", "2022-04-10", "2021-10-25"]
items_mot = ["Arthur"]
liste_date = Liste_date(items_date)
liste_mot = Liste_mot(items_mot)

#liste_date.fct_extractDaysOrMonthsOrYears(0)
#liste_date.fct_separateDateNumbers()
#liste_date.fct_extractYearIn2Digits()
#liste_date.fct_monthInLetters("EN")
#liste_date.fct_daysInLetters("EN");
# print(liste_date.fct_getListeFinale())

liste_mot.fct_toCapitalize()
liste_mot.fct_toLower()
liste_mot.fct_toUpper()
liste_mot.fct_removeAccents()
liste_mot.fct_stringToL33t()
liste_mot.fct_addRandomCommonSpecialCharacters()
liste_mot.fct_addAllRandomSpecialCharacters()
liste_mot.fct_addAllRandomSpecialCharactersLimitNb(5)
print(liste_mot.fct_getListeFinale())
