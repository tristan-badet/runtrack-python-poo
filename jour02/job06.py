class vehicule():
    
    def __init__(self, marque, prix, année, modele):
        self.marque = marque
        self.prix = prix
        self.année = année
        self.modele = modele
    
    def informationsVehicule(self):
        print("Marque =",self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.année)
        print("Prix =", self.prix)
    
    def demarrer(self):
        print("Attention, je roule")

class voiture(vehicule):
    
    def __init__(self, marque, prix, année, modele, portes):
        vehicule.__init__(self, marque, prix, année, modele)
        self.portes = portes
    
    def informationsVehicule(self):
        print("Marque =",self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.année)
        print("Prix =", self.prix)
        print("Nombres de portes =", self.portes)
    def demarrer(self):
        print("La voiture fait vroom vroom")

voiture1 = voiture(marque = "Mercedes", prix = 18500, année = 2020, modele = "classe 1", portes = 4)
voiture1.informationsVehicule()
voiture1.demarrer()

class moto(vehicule):
    
    def __init__(self, marque, prix, année, modele, roues):
        vehicule.__init__(self, marque, prix, année, modele)
        roues = 2
        self.roues = roues
    
    def informationsVehicule(self):
        print("Marque =",self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.année)
        print("Prix =", self.prix)
        print("Nombres de portes =", self.roues)
    def demarrer(self):
        print("la moto fonce à toute berzingue")

moto1 = moto(marque = "Mercedes", prix = 18500, année = 2020, modele = "classe 1", roues= 2)
moto1.informationsVehicule()
moto1.demarrer()
