#! /usr/bin/env python3
#TP3
#1.5 Fichiers
# Q1


def disparition(path):
    try:
        f = open(path)
    except IOError:
        print("Erreur : ouverture fichier")
        return

    fileout = open('out.txt', 'w')

    for ligne in f.readlines():
        for p in 'EéÉèÈêÊe':
            ligne = ligne.replace(p, '')

        fileout.write(ligne)

    fileout.close()


print(disparition("fichier.txt"))
