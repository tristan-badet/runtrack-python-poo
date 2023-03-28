class Rectangle():
    def constructeur(self):
        self.__largeur = 0
        self.__longueur = 0
    
    def getLongueur(self):
        return self.__longueur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLargueur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
    def périmètre(self):
        print("le périmètre est de", (self.getLargeur() + self.getLongueur())*2)
    
    def surface(self):
        print("La surface est de ", (self.getLargeur() * self.getLongueur()))

class Parallélépipède(Rectangle):
    def __init(self):
        Rectangle.constructeur(self)
        self.__hauteur = 0
    def getHauteur(self):
        return self.__hauteur
    def setHauteur(self, hauteur):
        self.__hauteur = hauteur
        return self.__hauteur


    def volume(self):
        print("Le volume du parallélépipède est de", (self.getLargeur() * self.getLongueur() * self.getHauteur()) )

rect1 = Rectangle()
rect1.setLongueur(15)
rect1.setLargueur(10)
rect1.périmètre()
rect1.surface()

para = Parallélépipède()
para.setLongueur(15)
para.setLargueur(10)
para.setHauteur(10)
para.volume()