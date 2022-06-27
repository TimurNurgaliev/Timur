class EuropeanDate:
    def __init__(self, year, month, day):
        lenm = len(str(month))
        lend = len(str(day))
        self.year = year
        if lenm == 1:
            month = '0' + str(month)
        self.month = month
        if lend == 1:
            day = '0' + str(day)
        self.day = day
 

class AmericanDate:
    def __init__(self, year, month, day):
        lenm = len(str(month))
        lend = len(str(day))
        self.year = year
        if lenm == 1:
            month = '0' + str(month)
        self.month = month
        if lend == 1:
            day = '0' + str(day)
        self.day = day
