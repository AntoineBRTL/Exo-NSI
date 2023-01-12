class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d
        
    def __eq__(self, a):
        return (self.gauche == a.gauche) and (self.droit == a.droit) and self.valeur == a.valeur and a is not None