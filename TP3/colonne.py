#! /usr/bin/env python3
#TP3
#1.5 Fichiers
# Q1


def colonne(path, i):
    try:
        f = open(path)
    except IOError:
        print("Erreur : ouverture fichier")
        return

    liste = ""
    for ligne in f.readlines():
        if len(ligne) > i-1 and i > 0:
            liste += ligne[i-1]
        else :
            return "indice trop petit ou trop grand"
    return liste


print(colonne("fichier.txt", 1))
print(colonne("fichier.txt", 2))
print(colonne("fichier.txt", 0))
print(colonne("fichier.txt", 20))
