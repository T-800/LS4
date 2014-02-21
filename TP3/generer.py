#! /usr/bin/env python3
#TP3
#1.5 Fichiers
# Q1

from charger import charger

def generer(i,path):
    try:
        f = open(path)
    except IOError:
        print("Erreur : ouverture fichier")
        return

    dico = charger(path)
    fileout = open('i-poeme.txt', 'w')

    for ligne in range(14):
        fileout.write(dico[ligne][i])

    fileout.close()


print(generer(2,"vers-queneau.txt"))
