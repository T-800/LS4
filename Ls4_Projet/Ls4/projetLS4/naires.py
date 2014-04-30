import math

def Arbre_n_aire(liste, n):

    nb = len(liste)
    print(liste)

    if nb >= 3:

        alpha = int(math.log(nb, n))
        reste = int(nb - (n ** alpha))


        sous_liste = []

















Arbre_n_aire([1,2,3,4,5,6,7,8],3)