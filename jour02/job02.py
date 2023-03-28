class Personne():
    
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print("La personne a", self.age,"ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, newAge):
        self.age = newAge
        return self.age
    
class Eleve(Personne):
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self):
        self.__matière = ""
    def enseigner(self):
        print("le cours va commencer")
        
personne1 = Personne()
eleve1 = Eleve()
eleve1.affichageAge()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
Prof1 = Professeur()
Prof1.modifierAge(40)
Prof1.bonjour()
Prof1.enseigner()





    

    