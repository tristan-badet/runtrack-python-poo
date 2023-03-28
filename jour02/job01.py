class Personne():
    
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print("La personne a", self.age,"ans")
    
    def bonjour():
        print("Hello")
    
    def modifierAge(self, newAge):
        self.age = newAge
        return self.age
    
class Eleve(Personne):
    
    def allerEnCours():
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur():
    def __init__(self):
        self.__matière = ""
    def enseigner():
        print("le cours va commencer")
        
personne1 = Personne()
eleve1 = Eleve()
eleve1.affichageAge()




    

    