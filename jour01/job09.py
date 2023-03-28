class Student():
    def identité(self):
        self.__nom = "Doe"
        self.__prénom = "John"
        self.__numeroetudiant = "145"
        self.__crédits = 0
        self.__level = ""
    
    def getCrédits(self):
        return self.__crédits
    def getNom (self):
        return self.__nom
    def getPrenom (self):
        return self.__prénom
    def getId(self):
        return self.__numeroetudiant
    
    def add_crédits(self, addcrédits, crédits):
        self.__crédits = crédits
        if addcrédits > 0 and addcrédits%1 == 0:
            crédits += addcrédits
            self.__crédits = crédits
            return self.__crédits
    
    def _studentEval(self,creditsactuels):
        creditsactuels = Student.getCrédits()
        if creditsactuels > 0 and creditsactuels < 60:
            print("Insuffisant")
        elif creditsactuels >= 60 and creditsactuels < 70:
            print("passable")
        elif creditsactuels >= 70 and creditsactuels < 80:
            print("bien")
        elif creditsactuels >= 80 and creditsactuels < 90:
            print("très bien")
        elif creditsactuels >= 90:
            print("excellent")
    def studentInfo(self):
        print("Nom")
        print("Prénom")
        print("ID")
        print("Niveau")




Eleve1 = Student()
Eleve1.add_crédits(5,0)
Eleve1.add_crédits(15,5)
Eleve1.add_crédits(10,20)
print(Eleve1.getCrédits())
print(Eleve1.studentInfo)
