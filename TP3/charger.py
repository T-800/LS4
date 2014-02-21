#! /usr/bin/env python3
#TP3
#1.5 Fichiers
# Q1


def charger(path):
    try:
        f = open(path)
    except IOError:
        print("Erreur : ouverture fichier")
        return

    dico = {}
    for i in range(14):
        dico[i] = []
        vers = 0
        while (vers < 10):
            dico[i] += [f.readline()]
            vers += 1
        f.readline()

    return dico


#
#
#dico = charger("vers-queneau.txt")
#
#for i in range(14):
#    print(i+1)
#    print (str([s for s in dico[i]])+"\n")
