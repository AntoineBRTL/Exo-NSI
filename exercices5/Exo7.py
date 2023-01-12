class FileBornee:
    def __init__(self, c):
        self.contenu = [None] * c
        self.nb = 0
        self.premier = 0

    def est_vide(self):
        return self.nb == 0

    def est_pleine(self):
        return self.nb == len(self.contenu)

    def ajouter(self, t):
        if(self.est_pleine()):
            raise IndexError("Error")

        # mettre la valeur
        index = (self.premier + self.nb) % len(self.contenu)
        self.contenu[index] = t

        # changer indices
        self.nb = 1 + self.nb

    def retirer(self):
        if(self.est_vide()):
            raise IndexError("Error")

        # recuperer valeurs
        v = self.contenu[self.premier]
        self.contenu[self.premier] = None

        # changer indices
        index = (self.premier + 1) % len(self.contenu)
        self.premier = index
        return v

def creer_file(c):
    return FileBornee(c)

file = creer_file(10)

for i in range(10):
    file.ajouter(1)

for i in range(10):
    print(file.retirer())