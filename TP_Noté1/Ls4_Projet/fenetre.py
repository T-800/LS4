#! /usr/bin/env python3

from tkinter.filedialog import *
from Arbre import Arbre
dict = {1:
            {"Arbre binaire Complet":"ABC",
             "Arbre Alterné":"AA",
             "Nombres premiers":"NP",
             "Nombres paire/Impaire":"PI",
             "Arbre Equilibré":"EQ"
            },
        2:
            {"Arbre n-aire Complet": "ANR",
             "Arbre n-aire Random": "ANC"
            }
}



class Interface(Frame):
    '''
    '''

    def __init__(self, fenetre):
        Frame.__init__(self, fenetre)
        frame_gauche = Frame(fenetre) # partie boutons
        frame_droite = Frame(fenetre) # partie Image Module

        frame_gauche.pack(side=LEFT, fill="y")
        frame_droite.pack(side=RIGHT,fill="both",expand=1)
        frame_gauche.config(background='#303030')

        Bouton_A = Button(frame_gauche, text="Ouvrir fichier Arbre", fg="white", bg="#7F7F7F", highlightbackground='#303030', highlightthickness=3, command=self.openfile_Arbre).grid(row=0, column=0, sticky=W+N+E+S) # ouvrir Arbre
        Bouton_B = Button(frame_gauche, text="Ouvrir fichier Liste", fg="white", bg="#7F7F7F", highlightbackground='#303030', highlightthickness=3, command=self.openfile_Liste).grid(row=1,  column=0, sticky=W+N+E+S) # ouvrir Liste
        self.texte = Label(frame_gauche, text="Pas d'arbre Ouvert", bg="#7F7F7F", highlightbackground='#303030', highlightthickness=3)
        self.texte.grid(row=2,  column=0, sticky=W+N+E+S) # ouvrir Liste


        self.canvas = Canvas(frame_droite, background="#EDEDED", scrollregion=(0,0,1920,1080)) # partie ou on dessine les arbres

        # les ScrollBar de la partie ou on dessine
        hbar = Scrollbar(frame_droite, orient=HORIZONTAL,activebackground="#333333")
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(frame_droite, orient=VERTICAL,activebackground="#333333")
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)

        # configuration du canevas dessin
        self.canvas.config(width=640,height=480, xscrollcommand=hbar.set, yscrollcommand=vbar.set, highlightbackground='#000000', borderwidth=1, highlightthickness=2)
        self.canvas.pack(expand=True,fill=BOTH)
        self.canvas.bind('<4>', lambda event: self.canvas.yview('scroll', -1, 'units'))
        self.canvas.bind('<5>', lambda event: self.canvas.yview('scroll', 1, 'units'))




    def openfile_Arbre(self):
        self.filename = askopenfilename(parent=self)
        try:
            f = open(self.filename)
        except IOError:
            print('Pas de fichier')
            return
        liste1 = f.readline()
        liste1 = eval(liste1)

        self.construct_Arbre("A", liste1)



    def openfile_Liste(self):
        self.filename = askopenfilename(parent=self)

        # POPUP
        self.popup = Toplevel()

        self.popup.title("Options d'ouverture")

        # choix binaire/n-aire
        self.radio_var = StringVar(self.popup)
        self.radio_var.set(1)
        binaire = Radiobutton(self.popup, text='Binaire', variable=self.radio_var, value=1,command=self.select_Naire).grid(row=0, column=0, sticky=W)
        naire = Radiobutton(self.popup, text='N-aire', variable=self.radio_var, value=2,command=self.select_Naire).grid(row=0, column=1, sticky=W)

        # choix methode construction
        lab_Methode = Label(self.popup, text="Methode de Construction :").grid(row=1, column=0, sticky=W)
        self.var_methode = StringVar(self.popup)
        self.var_methode.set("Arbre binaire Complet")
        self.listeMethode = OptionMenu(self.popup, self.var_methode, *dict[1].keys())
        self.listeMethode.grid(row=1, column=1, sticky=W)

        # choix nombre d'arrete
        lab_nb_Arretes = Label(self.popup, text="Nombre d'arrete :").grid(row=2, column=0, sticky=W)
        self.nombre_arrete = StringVar()
        self.nombre_arrete.set(3)
        self.entry = Entry(self.popup, textvariable=self.nombre_arrete, state='disable')
        self.entry.grid(row=2, column=1, sticky=W)

        #
        Bouton_A = Button(self.popup, text="Annuler", command=self.popup.destroy).grid(row=3, column=1, sticky=W)
        Bouton_OK = Button(self.popup, text="OK", command=self.optionListe).grid(row=3, column=1, sticky=E)


    def select_Naire(self):

        if int(self.radio_var.get())== 1:  # si binaire
            self.entry.configure(state='disabled')  # nombre d'arrete non modifiable

            # On change la liste des options d'ouverture
            liste = [i for i in dict[1].keys()]
            self.var_methode.set(liste[0])
            menu = self.listeMethode['menu']
            menu.delete(0, 'end')
            for item in liste:
                menu.add_command(label=item, command=lambda item=item: self.var_methode.set(item))



        elif int(self.radio_var.get())==2:  # si n-naire
            self.entry.configure(state='normal')

            liste = [i for i in dict[2].keys()]
            self.var_methode.set(liste[0])
            menu = self.listeMethode['menu']
            menu.delete(0, 'end')
            for item in liste:
                menu.add_command(label=item, command=lambda item=item: self.var_methode.set(item))


    def optionListe(self):
        print("Vous Avez Choisi la : "+self.var_methode.get()+" nb arrete: "+str(self.nombre_arrete.get()))
        f = open(self.filename)
        liste1 = f.readlines()
        liste1 = [int(i) for i in liste1]

        methode = dict[int(self.radio_var.get())][self.var_methode.get()]
        self.construct_Arbre(methode,liste1, int(self.nombre_arrete.get()))
        self.popup.destroy()
        self.arbre.saveArbre('test1')

    def afficheArbre(self,arbre, x, y):

        self.canvas.create_line(x,y,x,y+30, width=3)

        if arbre.sous_arbre:
            self.canvas.create_line(x-arbre.barycentre,y+30,x+(arbre.longueur_Tige_Total-arbre.barycentre),y+30, width=3)
            a, b = x-arbre.barycentre,y+30
            for i,elt in enumerate(arbre.sous_arbre):
                self.afficheArbre(elt,a+arbre.ecarts_Tiges[i], b)

        else :
            pconst = arbre.pprop
            self.canvas.create_oval(x-pconst//2, y+30, x+pconst//2, y+30+(pconst), fill='deep sky blue',width=2)
            self.canvas.create_text(x, (y+35+(pconst//4)), text=arbre.poids)


    def rollWheel(event):
        if event.num == 4:
            self.module.yview('scroll', -1, 'units')
        elif event.num == 5:
            self.module.yview('scroll', 1, 'units')


    def construct_Arbre(self, methode, liste, i=0):

        self.canvas.delete("all")

        self.arbre = Arbre(methode, liste, i)
        self.arbre.MAJ()
        self.arbre.calcul_Pos_SA()
        self.arbre.calcul_barycentre()
        self.texte.config(text=Arbre.typeArbre, fg="white")
        self.afficheArbre(self.arbre, 1920 // 2, 0)


if __name__ == '__main__':

    fenetre = Tk()
    fenetre.title("Projet Python")
    interface = Interface(fenetre)
    interface.pack(fill="both", expand=True)
    interface.mainloop()

