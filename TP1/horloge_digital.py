"""Créer une horloge digitale.
"""

# Importer Tkinter
from tkinter import *


# Création d'une fenêtre, racine de l'interface
fenetre = Tk()
fenetre.title('Horloge Digitale')

# Création d'une ligne de texte (un label) contenant l'affichage de l'heure
# Note : le constructeur label prend en argument la fenêtre contenant l'interface
# graphique.
heure = Label(fenetre, text="Affichage de l'heure", width=30, height=5)

# Création d'une fonction de mise à jour de l'heure

def update():
    ''' affiche l'heure courante '''
    #################################################################
    now = "12h 36min 5s " # COMPLETER AVEC L'HEURE ACTUELLE avec time
    #################################################################
    # Commande qui met à jour le label temps
    heure.config(text=now)
    # Commande qui rappelle la fonction update après 600ms
    heure.after(200,update)

# Création d'un bouton pour demarrer l'horloge
demarre = Button(fenetre, text="demarrer", command=update)
# Création d'un bouton pour quitter l'horloge
quitte = Button(fenetre, text="quitter", command=fenetre.destroy)

# Affichage du label et des boutons dans la fenêtre
heure.grid(row=0, column=0, columnspan=2)
demarre.grid(row=1, column=0)
quitte.grid(row=1, column=1)

# Démarrage de la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
