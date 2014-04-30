__author__ = 'renaud'

import math


def Arbre_n_aire(liste, n):
    print("##IN##")
    print(str(liste))

    nb = len(liste)
    sous_arbre = []
    if nb > n:

        h = math.log(nb, n)
        h //= 1
        reste = int(nb - (n ** h))
        npas = int((n ** h) / n)
        print("npas :"+str(npas))
        print("reste :" + str(reste))

        tmp = []

        while liste != []:
            if reste >= n**2:
                print("1")
                sous_arbre += [Arbre_n_aire(liste[:npas + n**2], n)]
                liste = liste[npas + n**2:]
                reste -= n**2

            elif reste > 0:
                print("2")
                sous_arbre += [Arbre_n_aire(liste[:npas + reste], n)]
                liste = liste[npas + reste:]
                reste -= reste
            else:
                print("3")
                sous_arbre += [Arbre_n_aire(liste[:npas], n)]
                liste = liste[npas:]




    elif nb == 1:
        sous_arbre = liste[0]
        pass
    else:
        for i in liste:
            sous_arbre += [Arbre_n_aire([i], n)]
    print("##OUT##")
    return sous_arbre



s = Arbre_n_aire([1,2,3,4,5,6,7,8,9,10,11,12,13,14],3)

print(s)