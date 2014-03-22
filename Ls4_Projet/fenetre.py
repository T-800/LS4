#! /usr/bin/env python3

from tkinter.filedialog import *
from main2 import Arbre




class Interface(Frame):
    '''
    '''

    def __init__(self, fenetre):
        fenetre
        Frame.__init__(self, fenetre)
        frame_gauche = Frame(fenetre) # partie boutons
        frame_droite = Frame(fenetre) # partie Image Module

        frame_droite.pack(side=RIGHT)
        frame_gauche.pack(side=LEFT, fill="both")
        Bouton_A = Button(frame_gauche, text="Ouvrir fichier Arbre", command=self.openfile_Arbre).grid(row=0, column=0, sticky=W+N+E+S) # ouvrir Arbre
        Bouton_B = Button(frame_gauche, text="Ouvrir fichier Liste", command=self.openfile_Liste).grid(row=1,  column=0, sticky=W+N+E+S) # ouvrir Liste

        module = Canvas(frame_droite, width=800, height=600, background="white").pack()

    def openfile_Arbre(self):
        filename = askopenfilename(parent=self)
        f = open(filename)
        liste1 = f.readline()
        liste1 = eval(liste1)
        self.arbre = Arbre("A",liste1)
        self.arbre.calcul_longueur()
        self.arbre.afficheArbre()
        print("profondeur "+str(self.arbre.profondeur()))
        print("profondeur_max "+str(self.arbre.profondeur_max))


    def openfile_Liste(self):
        self.filename = askopenfilename(parent=self)
        self.popup = Toplevel()
        self.popup.geometry("%dx%d%+d%+d" % (325, 100, 300, 500))
        self.popup.title("Options d'ouverture")

        self.radio_var = StringVar(self.popup)
        self.radio_var.set(1)
        binaire = Radiobutton(self.popup, text='Binaire', variable=self.radio_var, value=1,command=self.select_Naire).grid(row=0, column=0, sticky=W)
        naire = Radiobutton(self.popup, text='N-aire', variable=self.radio_var, value=2,command=self.select_Naire).grid(row=0, column=1, sticky=W)


        lab_Methode = Label(self.popup, text="Methode de Construction").grid(row=1, column=0, sticky=W)
        self.variable = StringVar(self.popup)
        self.variable.set("ABC")
        self.binaire_Tuple = ("ABC","AA","NP","PI","EQ")
        self.n_aire_Tuple = ("ANC","ANR")
        self.listeMethode = OptionMenu(self.popup, self.variable,*(self.binaire_Tuple+self.n_aire_Tuple))
        self.listeMethode.grid(row=1, column=1, sticky=W)

        lab_nb_Arretes = Label(self.popup, text="Nombre d'arrete :").grid(row=2, column=0, sticky=W)
        self.nombre_arrete = StringVar()
        self.nombre_arrete.set(3)
        self.entry = Entry(self.popup, textvariable=self.nombre_arrete, state='disable')
        self.entry.grid(row=2, column=1, sticky=W)# verifier int

        Bouton_A = Button(self.popup, text="Annuler", command=self.popup.destroy).grid(row=3, column=1, sticky=W)
        Bouton_OK = Button(self.popup, text="OK", command=self.optionListe).grid(row=3, column=1, sticky=E)



    def select_Naire(self):
        print(self.radio_var.get())
        if int(self.radio_var.get())==1:
            self.entry.configure(state='disabled')
        elif int(self.radio_var.get())==2:
            self.entry.configure(state='normal')




    def optionListe(self):
        print("Vous Avez Choisi la : "+self.variable.get()+" nb arrete: "+str(self.nombre_arrete.get()))
        f = open(self.filename)
        liste1 = f.readlines()
        liste1 = [int(i) for i in liste1]
        print(liste1)
        a = Arbre(self.variable.get(), liste1, int(self.nombre_arrete.get()))
        a.calcul_longueur()
        a.Aff()
        print("profondeur "+str(a.profondeur()))
        print("profondeur_max "+str(a.profondeur_max))
        self.popup.destroy()




fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()

