class PileBorne:
    def __init__(self, tailleMax):
        self._tailleMax = tailleMax
        self.contenu = list()

    def __len__(self):
        return len(self.contenu)

    def est_vide(self):
        return self.__len__() == 0

    def est_pleine(self):
        return self.__len__() == self._tailleMax

    def empiler(self, x):
        if(self.__len__() < self._tailleMax):   
            self.contenu.append(x)
            return
        raise IndexError("Taille maximale")

    def depiler(self):
        if(not self.est_vide()):
            return self.contenu.pop(0)
        raise IndexError("Aucun element dans la pile")