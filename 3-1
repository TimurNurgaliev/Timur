class LeftParagraph:
    def __init__(self, number=int()):
        self.number = number
        self.n = []

    def add_word(self, stroka=str()):
        if len(self.n) == 0 or len(stroka + self.n[-1]) >= self.number:
            self.n.append(stroka)
        else:
            self.n[-1] = self.n[-1] + ' ' + stroka

    def end(self):
        for element in self.n:
            print(element)


class RightParagraph:
    def __init__(self, number=int()):
        self.number = number
        self.n = []

    def add_word(self, stroka=str()):
        if len(self.n) == 0 or len(stroka + (self.n[-1]).lstrip()) >= self.number:
            self.n.append(stroka.rjust(self.number, " "))
        else:
            self.n[-1] = (self.n[-1].lstrip() + ' ' + str(stroka)).rjust(' ', self.number)

    def end(self):
        for element in self.n:
            print(element)


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()
