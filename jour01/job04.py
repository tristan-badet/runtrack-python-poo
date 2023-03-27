class Personne():
    
    def constructeur(self):
        self.nom = "John"
        self.prenom = "Doe"

    def SePresenter(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        print("Je suis", prenom, nom)
        return nom, prenom

        
test = Personne()

test.SePresenter(prenom = "John", nom = "Doe")