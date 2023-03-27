class Livre():
    def construct(self):
        self.__titre = ""
        self.__auteur = ""
        self.__nbpages = 0
        self.__disponibilité = True
    
    def setTitre(self, titre):
        self.__titre = titre
        return self.__titre
    def getTitre(self):
        return self.__titre
    
    def setAuteur(self, auteur):
        self.__auteur = auteur 
        return self.__auteur
    def getAuteur(self):
        return self.__auteur
    
    def setNbpages(self, nbpages):
        if nbpages >= 0 and nbpages%1 == 0:
            self.__nbpages = nbpages
            return self.__nbpages
        else:
            print("Erreur, le nombre de pages doit être supérieur à 0 et être un nombre entier")
    def getNbpages(self):
        return self.__nbpages
    
    def vérification(self, disponibilité):
        self.__disponibilité = disponibilité
        if disponibilité == True:
            return self.__disponibilité
        elif disponibilité == False:
            return self.__disponibilité == False
    def emprunter(self, emprunter):
        emprunter = False
        if emprunter == True:
            self.vérification = False
        elif self.vérification == True:
            emprunter = False
    def rendre(self, rendre):
        rendre = False
        if rendre == True and self.emprunter == True:
            self.__disponibilité = True



Livre1 = Livre()
Livre1.setAuteur("Jean Pascal Bouché")
Livre1.setNbpages(40)
Livre1.setTitre("Claude François, une vie électrique")
print(Livre1.getAuteur(), Livre1.getTitre(), Livre1.getNbpages())
