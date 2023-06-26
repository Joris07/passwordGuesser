from .Possibilites import Possibilites

class Date(Possibilites):
    def __init__(self, dates):
        self.dates = dates
        super().__init__()

    @property
    def dates(self):
        return self.__dates

    @dates.setter
    def dates(self, dates):
        self.__dates = dates