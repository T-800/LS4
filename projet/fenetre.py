#! /usr/bin/env python3

from tkinter import *
import tkinter.filedialog
from main2 import Arbre

class Interface(Frame):
    '''
    '''

    def __init__(self,fenetre, **kwargs):
        Frame.__init__(self,fenetre,width=800,height=600,**kwargs)
        module = Canvas(fenetre,width=400,height=400,background="white").pack()
        Bouton_A = Button(fenetre, text="Ouvrir fichier Arbre", command=self.openfile_Arbre).pack() # ouvrir Arbre
        Bouton_B = Button(fenetre, text="Ouvrir fichier Liste", command=self.openfile_Liste).pack() # ouvrir Liste
        self.arbre = Arbre()

    def openfile_Arbre(self):
        filename = tkinter.filedialog.askopenfilename(parent=self)
        f = open(filename)
        liste1 = f.readline()
        liste1 = eval(liste1)
        self.arbre = Arbre(liste1)
        self.arbre.calcul_longueur()
        self.arbre.afficheArbre()
        print("profondeur "+str(self.arbre.profondeur()))
        print("profondeur_max "+str(self.arbre.profondeur_max))


    def openfile_Liste(self):



        filename = tkinter.filedialog.askopenfilename(parent=self)
        f = open(filename)
        popup = Toplevel()
        popup.title("OPJBV")
        variable = StringVar(popup)
        listeMethode = OptionMenu(popup, variable, "Methode 1", "Methode 2", "Methode 3").pack()

        Bouton_OK = Button(popup, text="OK", command=None).pack() # ouvrir Arbre
        Bouton_A = Button(popup, text="Annuler", command=popup.destroy).pack() # ouvrir Liste
        def ok():
            print("value is", variable.get())
            popup.quit()

        button = Button(popup, text="OK222", command=ok).pack()
        '''
        liste1 = f.readline()
        liste1 = eval(liste1)
        self.arbre = Arbre(liste1)
        self.arbre.calcul_longueur()
        self.arbre.afficheArbre()
        print("profondeur "+str(self.arbre.profondeur()))
        print("profondeur_max "+str(self.arbre.profondeur_max))
'''


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
