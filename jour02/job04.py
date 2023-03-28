class Forme():
    def aire():
        return 0
    
class Rectangle(Forme):
    def __init__(self):
        self.largeur = 15
        self.longueur = 15
    def getLargeur(self):
        return self.largeur
    def getLongueur(self):
        return self.longueur
    def aire(self):
        print("l'aire du rectangle est", (self.getLargeur() * self.getLongueur()))

rect1 = Rectangle()
rect1.aire()