from math import cos, pi, sin


class Angle:
    def __init__(self, angle:int):
        self.angle = angle
    
    def __str__(self):
        return str(self.angle) + " degrés"

    def ajoute(self, angle):
        self.angle += angle.angle
        self._mettreDansIntervale()
        return self

    def _mettreDansIntervale(self):
        self.angle = self.angle % 360

    def _rad(self):
        return pi/180.0 * self.angle

    def cos(self):
        return cos(self._rad())

    def sin(self):
        return sin(self._rad())