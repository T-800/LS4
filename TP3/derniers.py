#! /usr/bin/env python3
#TP3
#1.5 Fichiers
# Q1


def derniers(path):
    try:
        f = open(path)
    except IOError:
        print("Erreur : ouverture fichier")
        return

    liste = []
    for ligne in f.readlines():
        liste.append(ligne.split()[-1])

    return liste


print(derniers("fichier.txt"))
