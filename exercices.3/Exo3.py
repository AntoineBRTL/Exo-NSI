class Intervalle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def estVide(self):
        return (self.b <= self.a)

    def __len__(self):
        if(self.estVide()):
            return 0
        return abs(self.b - self.a)

    def __contains__(self, x):
        return self.a <= x <= self.b

    def __eq__(self, intervalle):
        return self.a == intervalle.a and self.b == intervalle.b

    def __le__(self, intervalle):
        if(self.estVide()):
            return True
        return self.a <= intervalle.a and self.b <= intervalle.b

    def intersection(self, intervalle):
        return Intervalle(
            min(self.a, intervalle.a),
            max(self.b, intervalle.b)
        )

    def union(self, intervalle):
        return Intervalle(
            max(self.a, intervalle.a),
            min(self.b, intervalle.b)
        )