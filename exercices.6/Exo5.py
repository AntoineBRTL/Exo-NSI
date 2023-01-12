class Chrono:
    def __init__(self, h, m, s):

        if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
            self._heures = h
            self._minutes = m
            self._secondes = s
        else:
            raise ValueError()

    def avance(self, s):
        self._secondes += s
        self._minutes += self._secondes // 60
        self._secondes = self._secondes % 60
        self._heures += self._minutes // 60
        self._minutes = self._minutes % 60
        self._heures = self._heures % 24

print(Chrono(25, 10, 12)._heures)