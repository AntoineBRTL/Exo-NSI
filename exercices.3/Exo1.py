class Chrono:

    def __init__(self, s):
        self.s = s

    def avance(self, s):
        self.s += s

    def _coversion(self):
        return (self.s // 3600, (self.s // 60) % 60, self.s % 60)

    def __str__(self):
        h, m, s = self._coversion()
        return str(h) + "h " + str(m) + "m " + str(s) + "s "

    def clone(self):
        return Chrono(self.s)

    def __eq__(self, chrono):
        return self.s == chrono.s