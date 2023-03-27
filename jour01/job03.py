class Operation():
    

    def constructeur(self):
        self.nombre1 = 12
        self.nombre2 = 3
        self.resultat = 0
    def addition(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.resultat = nombre1 + nombre2
        print(self.resultat)
        return self.resultat

test = Operation()

test.addition(nombre1=12, nombre2=3)
