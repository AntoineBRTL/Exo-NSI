class DbTab:
    def __init__(self, droite:list, gauche:list):
        self.droite = droite
        self.gauche = gauche

    def imax(self):
        return len(self.droite) - 1

    def imin(self):
        return -len(self.gauche)

    def append(self, x):
        self.droite.append(x)

    def prepend(self, x):
        self.gauche.append(x)

    def vide(self):
        return self.imin == 0 and self.imax == -1

    def __getitem__(self, i:int):
        if(i < 0):
            return self.gauche[-i + 1]
        return self.droite[i]

    def __setitem__(self, i:int, x):
        pass
