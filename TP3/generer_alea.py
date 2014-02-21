#! /usr/bin/env python3
#TP3
#1.5 Fichiers
# Q1

from charger import charger
import random

def generer_alea(path):
    try:
        f = open(path)
    except IOError:
        print("Erreur : ouverture fichier")
        return

    dico = charger(path)
    fileout = open('alea-poeme.txt', 'w')

    for ligne in range(14):
        fileout.write(dico[ligne][random.randrange(10)])

    fileout.close()


print(generer_alea("vers-queneau.txt"))
