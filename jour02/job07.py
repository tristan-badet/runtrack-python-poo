import random

class Carte():
    def __init__(self):
        self.couleur = ""
        self.valeur = 0
        self.numero = 0
        self.numero2 = 0
    def tirerUneCarte(self, numero, numero2):
        numero = random.randint(0,3)
        numero2 = random.randint(0,12)
        self.numero = numero
        self.numero2 = numero2
        return self.numero, self.numero2
    def assignerValeur1(self):
        if self.numero == 0:
            self.couleur = "Coeur"
        elif self.numero == 1:
            self.couleur = "Carreau"
        elif self.numero == 2:
            self.couleur = "Pique"
        elif self.numero == 3:
            self.couleur = "Trèfle"
    def assignerValeur2(self, choixduun = int(input())):
        for x in range (1, 8):
            if self.numero2 == 0:
                if choixduun == 1:
                    self.valeur = 1
                    return self.valeur
                elif choixduun == 11:
                    self.valeur = 11
                    return self.valeur
                else:
                    print("erreur")
            elif self.numero2 == 9 or self.numero2 == 10 or self.numero2 == 11 or self.numero2 == 12:
                self.valeur = 10
                return self.valeur
            elif self.numero2 == x:
                self.valeur = x
                return self.valeur
            
class Jeu(Carte):