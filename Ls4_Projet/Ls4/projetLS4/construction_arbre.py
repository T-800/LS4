# -*- coding: utf-8 -*-
import Arbreclass
import math


def constuct_Arbre(ar, larbre):
    '''
    Construction de l'arbre apartir d'un tableau représentant un arbre
    '''
    if type(larbre) == int:
        ar.poids = larbre
    else:
        if not ar.sous_arbre:
            ar.sous_arbre = []
        for elt in larbre:
            ar.sous_arbre += [Arbreclass.Arbre("A", elt)]

def Arbre_Binaire_Croissant(ar, liste):
    liste.sort()
    print(liste)
    ar.sous_arbre = []
    ar.sous_arbre += [Arbreclass.Arbre("ABC", liste, ta=False)]


def Arbre_Binaire_Complet(ar, liste):
    '''

    '''

    if len(liste) >= 2:
        nb = len(liste)
        h = int(math.log(nb, 2))
        reste = int(nb - (2 ** h))
        n = int((2 ** (h-1)))

        if reste > n:
            liste1 = liste[:2*n]
            liste2 = liste[2*n:]
        else :
            liste1 = liste[:n+reste]
            liste2 = liste[n+reste:]

        ar.sous_arbre = []
        ar.sous_arbre += [Arbreclass.Arbre("ABC", liste1, ta=False)]
        ar.sous_arbre += [Arbreclass.Arbre("ABC", liste2, ta=False)]


    else:
        ar.poids = liste[0]



def Arbre_n_aire(ar, liste, n):

    nb = len(liste)

    if nb > n:

        h = math.log(nb, n)
        h //= 1
        reste = int(nb - (n ** h))
        npas = int((n ** h) / n)
        ar.sous_arbre = []
        while liste != []:
            if reste >= n ** 2:
                ar.sous_arbre += [Arbreclass.Arbre("ANC", liste[:npas + n ** 2], n, ta=False)]
                liste = liste[npas + n ** 2:]
                reste -= n ** 2

            elif reste > 0:
                ar.sous_arbre += [Arbreclass.Arbre("ANC", liste[:npas + reste], n, ta=False)]
                liste = liste[npas + reste:]
                reste -= reste
            else:
                ar.sous_arbre += [Arbreclass.Arbre("ANC", liste[:npas], n, ta=False)]
                liste = liste[npas:]





    elif nb == 1:
        ar.poids = liste[0]
        pass
    else:
        ar.sous_arbre = []
        for i in liste:
            ar.sous_arbre += [Arbreclass.Arbre("ANC", [i], n, ta=False)]


def construct_Random_Arbre():
    pass


def Arbre_Nombre_Premier(ar, liste):
    #
    prime = []
    nprime = []

    for elt in liste:
        if est_Premier(elt):
            prime += [elt]
        else:
            nprime += [elt]
    # Ajouter les tests si une des liste est vide
    if not ar.sous_arbre:
        ar.sous_arbre = []
    if prime == [] or nprime == []:
        Arbre_Binaire_Complet(ar, liste)
        Arbreclass.Arbre.typeArbre = "Arbre binaire Complet"
    else:
        ar.sous_arbre += [Arbreclass.Arbre("ABC", prime, ta=False)]
        ar.sous_arbre += [Arbreclass.Arbre("ABC", nprime, ta=False)]


def Arbre_Nombres_Pairs(ar, liste):
    pair = []
    npair = []

    for elt in liste:
        if elt % 2 == 0:
            pair += [elt]
        else:
            npair += [elt]
    # Ajouter les tests si une des liste est vide
    if not ar.sous_arbre:
        ar.sous_arbre = []
    if pair == [] or npair == []:

        Arbre_Binaire_Complet(ar,liste)
        Arbreclass.Arbre.typeArbre = "Arbre binaire Complet"
    else:
        ar.sous_arbre += [Arbreclass.Arbre("ABC", pair, ta=False)]
        ar.sous_arbre += [Arbreclass.Arbre("ABC", npair, ta=False)]


def construct_Alt_Arbre(ar, liste, i=1):
    if i == 0:
        if type(liste) == int:
            ar.poids = liste
        elif len(liste) == 1:
            ar.poids = liste[0]
        else:
            if not ar.sous_arbre:
                ar.sous_arbre = []
            ar.sous_arbre += [Arbreclass.Arbre("AA", liste[0], 1)]
            ar.sous_arbre += [Arbreclass.Arbre("AA", liste[1:], 1)]

    else:
        if type(liste) == int:
            ar.poids = liste
        elif len(liste) == 1:
            ar.poids = liste[0]
        else:
            if not ar.sous_arbre:
                ar.sous_arbre = []
            ar.sous_arbre += [Arbreclass.Arbre("AA", liste[1:], 0)]
            ar.sous_arbre += [Arbreclass.Arbre("AA", liste[0], 0)]


def est_Premier(nombre):
    if nombre == 1:
        return False
    k = 2
    r = math.sqrt(nombre)
    while k <= r:

        if nombre % k == 0:
            return False
        k += 1
    return True
