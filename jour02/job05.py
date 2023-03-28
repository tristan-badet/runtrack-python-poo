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

class Cercle(Forme):
    def __init__(self):
        self.radius = 10
    def aire(self):
        print("l'aire du cercle est",(self.radius ** 2))

rect2 = Rectangle()
cer = Cercle()
rect2.aire()
cer.aire()
