class Cellule:
    def __init__(self, v, s):
        self.v = v
        self.s = s

class Pile:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None
        
    def empiler(self, e):
        self._contenu = Cellule(e, self._contenu)
        
    def depiler(self):
        if self.est_vide():
            raise IndexError("depile une pile vide")
        v = self._contenu.valeur
        self._contenu = self._contenu.suivante
        return v
        
class Historique:
    def __init__(self):
        self.adresse_courante = None
        self._adresses_precedentes = Pile()
        self._adresses_suivantes = Pile()
        
    def aller_a(self, adr):
        if not self.adresse_courante is None:
            self._adresses_precedentes.empiler(self.adresse_courante)
        self.adresse_courante = adr

        self._adresses_suivantes = Pile()
        
    def retour(self):
        self._adresses_suivantes.empiler(self.adresse_courante)

        if not self._adresses_precedentes.est_vide():
            self.adresse_courante = self._adresses_precedentes.depiler()
        else:
            self.adresse_courante = None

    def retour_avant(self):
        if not self._adresses_suivantes.est_vide():
            self._adresses_precedentes.empiler(self.adresse_courante)
            self.adresse_courante = self._adresses_suivantes.depiler(self.adresse_courante)

        