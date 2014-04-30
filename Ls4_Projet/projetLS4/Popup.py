# -*- coding: utf-8 -*-
from tkinter import messagebox
from tkinter.filedialog import *

from tkinter import colorchooser


dict = {1:
            {"Arbre binaire Complet": "ABC",
             "Arbre Alterné": "AA",
             "Nombres premiers": "NP",
             "Nombres paire/Impaire": "PI",
             "Croissant": "CR",
             "Fort/Faible": "FF"
            },
        2:
            {"Arbre n-aire": "ANC",
            }
}


def choix_Algo(fr):
    fr.liste1 = fr.arbre.st()
    popUp(fr)



def popUp(fr):
    '''
    Petite fenetre qui permet de choisir l'algo de construction des arbres binaires, n-aires a
    partir d'une liste de poids
    '''

    # POPUP
    fr.popup = Toplevel()

    fr.popup.title("Options d'ouverture")


    # choix binaire/n-aire
    fr.radio_var = StringVar(fr.popup)
    fr.radio_var.set(1)
    binaire = Radiobutton(fr.popup, text='Binaire', variable=fr.radio_var, value=1,
                          command=lambda: select_Naire(fr)).grid(row=0, column=0, sticky=W)
    naire = Radiobutton(fr.popup, text='N-aire', variable=fr.radio_var, value=2,
                        command=lambda: select_Naire(fr)).grid(row=0, column=1, sticky=W)

    # choix methode construction
    lab_Methode = Label(fr.popup, text="Methode de Construction :").grid(row=1, column=0, sticky=W)
    fr.var_methode = StringVar(fr.popup)
    fr.var_methode.set("Arbre binaire Complet")
    fr.listeMethode = OptionMenu(fr.popup, fr.var_methode, *dict[1].keys())

    fr.listeMethode.grid(row=1, column=1, sticky=W)

    # choix nombre d'arrete
    lab_nb_Arretes = Label(fr.popup, text="Nombre d'arrete :").grid(row=2, column=0, sticky=W)
    fr.nombre_arrete = StringVar()
    fr.nombre_arrete.set(3)
    fr.entry = Entry(fr.popup, textvariable=fr.nombre_arrete, state='disable')
    fr.entry.grid(row=2, column=1, sticky=W)

    fr.popup.bind('<Escape>', lambda event: end(fr,event))
    def end(fr, event):
        fr.popup.destroy()


    #*dict[1].keys()
    Bouton_A = Button(fr.popup, text="Annuler", command=fr.popup.destroy).grid(row=3, column=1, sticky=W)
    Bouton_OK = Button(fr.popup, text="OK", command=lambda: optionListe(fr)).grid(row=3, column=1, sticky=E)

def openfile_Liste(fr):
    fr.filename = askopenfilename(parent=fr)
    try:
        open(fr.filename)
    except IOError:
        return

    f = open(fr.filename)
    fr.liste1 = f.readlines()
    if not ficPoids("".join(fr.liste1)):
        messagebox.showerror("Erreur", "Fichier Poids incorrect")
        return
    popUp(fr)


def select_Naire(fr):
    if int(fr.radio_var.get()) == 1:  # si binaire
        fr.entry.configure(state='disabled')  # nombre d'arrete non modifiable

        # On change la liste des options d'ouverture
        liste = [i for i in dict[1].keys()]
        fr.var_methode.set(liste[0])
        menu = fr.listeMethode['menu']
        menu.delete(0, 'end')
        for item in liste:
            menu.add_command(label=item, command=lambda item=item: fr.var_methode.set(item))

    elif int(fr.radio_var.get()) == 2:  # si n-naire
        fr.entry.configure(state='normal')

        liste = [i for i in dict[2].keys()]
        fr.var_methode.set(liste[0])
        menu = fr.listeMethode['menu']
        menu.delete(0, 'end')
        for item in liste:
            menu.add_command(label=item, command=lambda item=item: fr.var_methode.set(item))


def optionListe(fr):
    '''
    Methode qui appel la construction de l'arbre en fonction de l'algo choisi
    '''
    liste1 = [int(i) for i in fr.liste1]

    methode = dict[int(fr.radio_var.get())][fr.var_methode.get()]
    if int(fr.radio_var.get()) == 2:
        try:
            i = int(fr.nombre_arrete.get())
            if i<2:
                messagebox.showerror("Erreur", "Le nombe d'arrete")
                return
        except :
            messagebox.showerror("Erreur", "Le nombe d'arrete")
            return
    fr.MAJ_Arbre(methode, liste1, int(fr.nombre_arrete.get()))
    fr.MAJ_Canvas()

    fr.popup.destroy()


def openfile_Arbre(fr):
    fr.filename = askopenfilename(parent=fr)
    try:
        f = open(fr.filename)
    except IOError:
        return
    liste1 = f.readline()
    if not ficArbre(liste1):
        messagebox.showerror("Erreur", "Fichier arbre incorrect")
        return
    liste1 = eval(liste1)

    fr.MAJ_Arbre("A", liste1)
    fr.MAJ_Canvas()


def color_Arbre(fr):
    tmp = fr.color
    fr.color = colorchooser.askcolor()
    if fr.color[0]:
        fr.color = list(fr.color[0])
        fr.MAJ_Canvas()
    else:
        fr.color = tmp


def save_arbre(fr):
    fr.filename = asksaveasfilename(parent=fr)
    if not fr.filename:
        return
    f = open(fr.filename, 'w')
    f.write(fr.arbre.chaine)
    f.close()


def ficArbre(L):
    if not L.startswith("[") or not L.endswith("]"):
        return None
    try:
        liste1 = eval(L)
    except:
        return None
    li = lt(liste1)
    for elt in li:
        if elt < 1:
            return None
    return liste1


def ficPoids(liste1):
    liste1 = [i.replace('\n', '') for i in liste1]
    for c in liste1:
        if c not in '0123456789':
            return False
    return True


def lt(l):
    if type(l) == list:
        a = []
        for elt in l:
            a.extend(lt(elt))
        return a
    else:
        return [l]


def nuance(col, n):
    '''
    Cette fonction renvoi un ensemble de couleur nuancé a a partir d'une couleur de depart
    '''

    p = 255//n
    moitier = n // 2
    color = []
    for i in range(moitier):
        m = moitier - i
        c2 = []
        for j in range(len(col)):
            c2 += [col[j] - m * p]
        for k in range(len(c2)):
            if c2[k] < 0:
                c2[k] = 0
        color += [c2]

    for i in range(moitier + (n % 2)):
        c2 = []
        for j in range(len(col)):
            c2 += [col[j] + i * p]
        for k in range(len(c2)):
            if c2[k] > 255:
                c2[k] = 255
        color += [c2]
    return color
