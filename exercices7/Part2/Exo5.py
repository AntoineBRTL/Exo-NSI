from exercices7.Part1.Exo7 import parfait

def remplir(a, t):
    if a is None:
        return
    
    remplir(a.gauche, t)
    t.append(a.valeur)
    remplir(a.droite, t)

a = parfait(3)
t = []

remplir(a, t)

print(t)