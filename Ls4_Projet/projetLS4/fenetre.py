#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from math import acos
from Popup import *
from Arbreclass import *

#hauteur des tiges
fil = 20

class Interface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.di = {}
        self.color = [127, 127, 127] # couleur de base des boule (gris)
        self.frame_gauche = Frame()  # partie boutons
        self.frame_droite = Frame()  # partie Image Module
        self.Largeur = 640
        self.Hauteur = 480
        self.frame_gauche.pack(side=LEFT, fill="y")
        self.frame_gauche.config(background='#303030')
        self.frame_droite.pack(side=RIGHT, fill="both", expand=1)


        self.bouton_arbre = Button(self.frame_gauche, text="Ouvrir fichier Arbre", fg="white", bg="#7F7F7F",
                                   highlightbackground='#303030', highlightthickness=3,
                                   command=lambda: openfile_Arbre(self))

        self.bouton_arbre.grid(row=0, column=0, sticky=W+N+E+S)

        self.bouton_liste = Button(self.frame_gauche, text="Ouvrir fichier Liste", fg="white", bg="#7F7F7F",
                                   highlightbackground='#303030', highlightthickness=3,
                                   command=lambda: openfile_Liste(self)).grid(row=1,  column=0, sticky=W+N+E+S)

        #zone d'affichage du type d'arbre ouvert
        self.texte = Label(self.frame_gauche, text="Pas d'arbre Ouvert", bg="#7F7F7F",
                           highlightbackground='#303030', highlightthickness=3)

        self.texte.grid(row=2,  column=0, sticky=W+N+E+S)  # ouvrir Liste

        # partie ou on dessine les arbres
        self.canvas = Canvas(self.frame_droite, background="#EDEDED", scrollregion=(0, 0, self.Hauteur, 480))

        # les ScrollBar de la partie où on dessine
        hbar = Scrollbar(self.frame_droite, orient=HORIZONTAL, activebackground="#333333")
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(self.frame_droite, orient=VERTICAL, activebackground="#333333")
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)

        # configuration du canevas dessin
        self.canvas.config(width=self.Largeur, height=self.Hauteur, xscrollcommand=hbar.set, yscrollcommand=vbar.set,
                           highlightbackground='#000000', borderwidth=1, highlightthickness=2)

        self.canvas.pack(expand=True, fill=BOTH)
        #self.canvas.bind('<4>', lambda event: self.canvas.yview('scroll', -1, 'units'))
        #self.canvas.bind('<5>', lambda event: self.canvas.yview('scroll', 1, 'units'))

        self.type_affichage = StringVar()
        self.radionormal = Radiobutton(self.frame_gauche, text="Normal", variable=self.type_affichage, value="Tiges_Droites",
                                       background='#303030', fg="white", selectcolor='#303030',
                                       highlightbackground='#303030', highlightthickness=3,
                                       command=self.MAJ_Canvas)

        self.radiocourbe = Radiobutton(self.frame_gauche, text="lignes courbées", variable=self.type_affichage, value="Tige_Courbées",
                                       background='#303030', fg="white", selectcolor='#303030',
                                       highlightbackground='#303030', highlightthickness=3,
                                       command=self.MAJ_Canvas)

        '''
        self.radiopoidstiges = Radiobutton(self.frame_gauche, text="Poid des tiges", variable=self.v, value=1,
                                           background='#303030', fg="white", selectcolor='#303030',
                                           highlightbackground='#303030', highlightthickness=3,
                                           command=self.MAJ_Canvas)
        '''

        self.bouton_color = Button(self.frame_gauche, text="Changer la couleur", fg="white", bg="#7F7F7F",
                                   highlightbackground='#303030', highlightthickness=3,
                                   command=lambda: color_Arbre(self))

        self.echelle = DoubleVar()
        self.echelle.set(1)
        self.scaleHorz = Scale(self.frame_gauche, orient=HORIZONTAL, from_=.1, to=5,  label="échelle",
                               resolution=.1, tickinterval=2, bigincrement=1, fg="white", bg="#303030",
                               highlightbackground='#303030', variable=self.echelle, command=self.MAJ_Canvas)

        self.changeAlgo = Button(self.frame_gauche, text="Ré-ouvrir", fg="white", bg="#7F7F7F",
                                  highlightbackground='#303030', highlightthickness=3,
                                  command=lambda: choix_Algo(self))
        self.modifArbre = BooleanVar()
        self.modifArbre.set(False)
        self.modif = Checkbutton(self.frame_gauche, text="Modifier", background='#303030', fg="white",
                                 selectcolor='#303030', highlightbackground='#303030', variable=self.modifArbre,
                                 onvalue=True, offvalue=False,command=self.MAJ_Canvas)

        self.bouton_save = Button(self.frame_gauche, text="Sauvegarder Arbre", fg="white", bg="#7F7F7F",
                                  highlightbackground='#303030', highlightthickness=3,
                                  command=lambda: save_arbre(self))

        self.radionormal.select()

        self.arbre = None

    def DessineArbre(self, arbre, x, y, ):
        '''

        '''

        if arbre.sous_arbre: # Si c'est un Arbre

            self.canvas.create_line(x, y, x, y + fil, width=1, joinstyle="round") # Tige


            if self.modifArbre.get():
                test = self.canvas.create_rectangle(x - 2.5, y + (fil // 2) - 2.5, x + 2.5, y + (fil // 2) + 2.5,
                                                    fill='green', tags=str(arbre.ID))
                self.canvas.tag_bind(test, '<Button-1>',self.menu_Arbre)


            if self.type_affichage.get() == "Tige_Courbées":

                yt = []

                for i in range(len(arbre.ecarts_Tiges)):
                    ax = x - arbre.barycentre + arbre.ecarts_Tiges[i]
                    cx = x

                    cy = y + fil + arbre.longueur_Tige_Total

                    p = arbre.longueur_Tige_Total**2

                    beta = 2 * cy
                    gamma = (ax - cx)**2 + cy**2 - p

                    delta = pow(beta, 2) - (4 * gamma)
                    delta = pow(delta, 1 / 2)

                    beta = -beta

                    y1 = ((0 - beta) + delta) / 2
                    y2 = ((0 - beta) - delta) / 2

                    yt += [min(y1, y2)]

                rayon = arbre.longueur_Tige_Total
                ax = x - arbre.barycentre
                ay = yt[0]
                sx = x + arbre.longueur_Tige_Total
                sy = y + fil + arbre.longueur_Tige_Total

                cx = x + arbre.longueur_Tige_Total - arbre.barycentre
                cy = yt[-1]

                AS = pow((sx - ax)**2 + (sy - ay)**2, 1 / 2)
                AC = pow((cx - ax)**2 + (cy - ay)**2, 1 / 2)

                s = (rayon**2 + rayon**2 - AS**2) / (2 * rayon * rayon)
                c = (rayon**2 + rayon**2 - AC**2) / (2 * rayon * rayon)

                start = (acos(s)*180)/math.pi
                end = (acos(c)*180)/math.pi

                x1 = x - arbre.longueur_Tige_Total
                y1 = y+fil

                x2 = x + arbre.longueur_Tige_Total
                y2 = y1 + arbre.longueur_Tige_Total*2
                end = -end
                self.canvas.create_arc(x1, y1, x2, y2, start=start, extent=end, style="arc", width=2)

                a = x - arbre.barycentre

                for i, elt in enumerate(arbre.sous_arbre):
                    self.DessineArbre(elt, a + arbre.ecarts_Tiges[i], yt[i])

            else:
                self.canvas.create_line(x - arbre.barycentre, y + fil,
                                        x + (arbre.longueur_Tige_Total - arbre.barycentre), y + fil, width=2,
                                        joinstyle="round")

                a, b = x - arbre.barycentre, y + fil
                for i, elt in enumerate(arbre.sous_arbre):
                    self.DessineArbre(elt, a+arbre.ecarts_Tiges[i], b)

        else:
            self.canvas.create_line(x, y, x, y + fil, width=1, joinstyle="round")
            if self.modifArbre.get() == 1:
                test = self.canvas.create_rectangle(x - 2.5, y + (fil // 4) - 2.5, x + 2.5, y + (fil // 4) + 2.5, fill='red', tags=str(arbre.ID))
                self.canvas.tag_bind(test, '<Button-1>', self.menu_Arbre)

            cv = self.di[arbre.poids]
            col = '#%02x%02x%02x' % (cv[0], cv[1], cv[2])
            pconst = arbre.pprop
            inv = [255 - cv[0], 255 - cv[1], 255-cv[2]]
            inv = '#%02x%02x%02x' % (inv[0], inv[1], inv[2])
            self.canvas.create_oval(x - pconst // 2, y + fil/2, x + pconst // 2, y + fil/2 + pconst, fill=col, width=1)
            if self.echelle.get() > .7:
                self.canvas.create_text(x, (y + fil/2 + 5 + (pconst // 4)), text=arbre.poids, fill=inv)
            self.Largeur = max(self.Largeur, y + 10 + pconst+50)
            self.canvas.config(scrollregion=(0, 0, self.Hauteur, self.Largeur))

    def MAJ_Arbre(self, methode, liste, i=0, ta=True):
        Arbre.stID = 1
        self.arbre = Arbre(methode, liste, i, ta)
        self.arbre.MAJ()

    def MAJ_Canvas(self, s=None):
        self.radionormal.grid(sticky=W, row=4)
        self.radiocourbe.grid(sticky=W, row=5)
        #self.radiopoidstiges.grid(sticky=W, row=6)
        self.bouton_color.grid(sticky=W, row=7)
        self.scaleHorz.grid(row=8, column=0, sticky=W + N + E + S)
        self.changeAlgo.grid(row=9, column=0, sticky=W + N + E + S)
        self.modif.grid(row=10, column=0, sticky=W + N + S)
        self.bouton_save.grid(row=11, column=0, sticky=W + N + E + S)
        self.canvas.delete("all")

        minx, maxx = self.arbre.getMinX(), self.arbre.getMaxX()
        self.Hauteur = (minx + maxx) + 100
        self.texte.config(text=Arbre.typeArbre, fg="white")

        listePoids = self.arbre.st()
        listePoids = list(set(listePoids))
        listeCouleur = nuance(self.color, len(listePoids))
        listePoids.sort()
        for li, col in zip(listePoids, listeCouleur):
            self.di[li] = col

        self.DessineArbre(self.arbre, minx + 50, 0)
        self.canvas.scale(ALL, 0, 0, self.echelle.get(), self.echelle.get())
        self.canvas.config(scrollregion=(0, 0, self.Hauteur * self.echelle.get(), self.Largeur * self.echelle.get()))


    def radio_menu_arbre(self):

        if self.radio_var_arbre.get() == "Ajouter":
            self.entry_poids.configure(state='normal')
            self.listeMethode.configure(state='normal')
            self.entry_ppoids.configure(state='disabled')

        elif self.radio_var_arbre.get() == "Supprimer":
            self.entry_poids.configure(state='disabled')
            self.listeMethode.configure(state='disabled')
            self.entry_ppoids.configure(state='disabled')

        else:
            self.entry_poids.configure(state='disabled')
            self.listeMethode.configure(state='disabled')
            self.entry_ppoids.configure(state='normal')


    def action_menu_arbre(self):
        '''

        '''
        if self.radio_var_arbre.get() == "Ajouter":
            if type(self.nouveauPoids.get()) != type(int()):
                messagebox.showerror("Erreur", "Le poids n'est pas un entier")

            if self.nouveauPoids.get()<1:
                messagebox.showerror("Erreur", "Le poids < 1")
            else:
                self.arbre.add(self.tags[0], self.nouveauPoids.get(), self.position.get())
        elif self.radio_var_arbre.get() == "Supprimer":
            self.arbre.suppr(self.tags[0])
        else :
            if self.changerPoids.get() < 1:
                messagebox.showerror("Erreur", "poids < 1")
            else:
                self.arbre.changepoids(self.tags[0],self.changerPoids.get())

        self.popup.destroy()
        self.arbre.MAJ()
        self.MAJ_Canvas()

    def menu_Arbre(self, event):
        item = self.canvas.find_withtag(CURRENT)
        self.tags = self.canvas.gettags(item)

        self.popup = Toplevel()
        self.popup.title("Options sur arbre")
        self.radio_var_arbre = StringVar(self.popup)
        self.radio_var_arbre.set("Ajouter")
        ajouter = Radiobutton(self.popup, text='Ajouter', variable=self.radio_var_arbre, value="Ajouter",
                              command=self.radio_menu_arbre ).grid(row=0, column=0, sticky=W)

        changer = Radiobutton(self.popup, text='Changer Poids', variable=self.radio_var_arbre, value="Changer",
                              command=self.radio_menu_arbre)

        self.changerPoids = IntVar()
        self.entry_ppoids = Entry(self.popup, textvariable=self.changerPoids)
        if self.arbre.isPoids(int(self.tags[0])):
            changer.grid(row=1, column=0, sticky=W)
            self.entry_ppoids.grid(row=1, column=1, sticky=W)
            self.entry_ppoids.configure(state='disabled')  # nombre d'arrete non modifiable

        supprimer = Radiobutton(self.popup, text='Supprimer', variable=self.radio_var_arbre, value="Supprimer",
                                command=self.radio_menu_arbre).grid(row=2, column=0, sticky=W)

        lab_poids = Label(self.popup, text="Poids :").grid(row=0, column=1, sticky=W)
        self.nouveauPoids = IntVar()
        self.entry_poids = Entry(self.popup, textvariable=self.nouveauPoids)
        self.entry_poids.grid(row=0, column=2, sticky=W)

        lab_position = Label(self.popup, text="Position du poids:").grid(row=0, column=3, sticky=W)
        self.position = IntVar(self.popup)
        self.listeMethode = OptionMenu(self.popup, self.position, *[i for i in range(self.arbre.lensa(int(self.tags[0]))+1)])
        self.listeMethode.grid(row=0, column=4, sticky=W)

        self.popup.bind('<Escape>', lambda event: end(self, event))

        def end(self, event):
            self.popup.destroy()


        Bouton_A = Button(self.popup, text="Annuler", command=self.popup.destroy).grid(row=2, column=3, sticky=W)
        Bouton_OK = Button(self.popup, text="OK", command=self.action_menu_arbre).grid(row=2, column=4, sticky=E)

