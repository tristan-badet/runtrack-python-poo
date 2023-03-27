import tkinter
from tkinter import *
class Rectangle():
    def constructeur(self):
        self.__longueur = 0
        self.__largeur = 0
    
    def setLongueur(self, longueur):
        self.__longueur = longueur 
        return self.__longueur
    
    def getLongueur(self):
        return self.__longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
    def getLargeur(self):
        return self.__largeur

rectangle = Rectangle()
rectangle.setLargeur(5)
rectangle.setLongueur(10)
dessiner = tkinter.Tk()
dessiner.title("Rectangle")
dessiner.geometry("500x500")
can = Canvas(dessiner)
can.pack()
can.create_rectangle(0,0,rectangle.getLargeur(),rectangle.getLongueur(), fill= "red")
can.update()
dessiner.mainloop()