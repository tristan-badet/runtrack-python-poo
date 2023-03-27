class Animal():
    age = 0
    prenom = "Snoop Dogg"
    def constructeur(self, age, prenom):
        self.prenom = prenom
        self.age = age
    def vieillir(self):
        self.age += 1
    def nommer(self, prenom):
        self.prenom = prenom

objet = Animal()
print(objet.age)
objet.vieillir()
print(objet.age)
print(objet.prenom)
    

