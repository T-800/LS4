#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from construction_arbre import *


class Arbre:
    stID = 1
    typeArbre = ""

    def __init__(self, methode, liste, i=0, ta=True):
        self.poids = 0  # son poids si c'est une feuille ou le poids total si c'est un sous-arbre
        self.pprop = 0
        self.sous_arbre = None  # plus facile pour identifier les feuilles (ajout d'un test if dans les fonctions)
        self.ecarts_Tiges = None  # pas besoin de cette variable si c'est une feuille
        self.longueur_Tige_Total = 100  # Celle la non plus
        self.barycentre = 0
        self.chaine = ""
        self.ID = Arbre.stID
        Arbre.stID += 1
        if methode == "A":
            if ta:
                Arbre.typeArbre = "Fichier Arbre"
            constuct_Arbre(self, liste)

        elif methode == "ABC":  # Arbre Binaire Complet
            if ta:
                Arbre.typeArbre = "Arbre binaire Complet"
            Arbre_Binaire_Complet(self, liste)

        elif methode == "AA":  # Arbre Alterné
            if ta:
                Arbre.typeArbre = "Arbre Alterné"
            construct_Alt_Arbre(self, liste, i)

        elif methode == "NP":  # Nombres Premiers
            if ta:
                Arbre.typeArbre = "Nombres premiers"
            Arbre_Nombre_Premier(self, liste)

        elif methode == "PI":  # Paire/Impaire
            if ta:
                Arbre.typeArbre = "Nombres paire/Impaire"
            Arbre_Nombres_Pairs(self, liste)

        elif methode == "CR":  # sag ~~ sad
            if ta:
                Arbre.typeArbre = "Croissant"
            liste.sort()
            Arbre_Binaire_Complet(self, liste)
            pass
        elif methode == "FF":  # sag ~~ sad
            if ta:
                Arbre.typeArbre = "Fort/Faible"
            liste.sort()
            liste2 = []
            i = 0
            j = 0
            while liste:
                if j % 2 == 0:
                    if i % 2 == 0:
                        liste2 += [liste[0]]
                        liste = liste[1:]
                    else:
                        liste2 += [liste[-1]]
                        liste = liste[:-1]
                        j += 1
                else:
                    if i % 2 == 0:
                        liste2 += [liste[-1]]
                        liste = liste[:-1]
                    else:
                        liste2 += [liste[0]]
                        liste = liste[1:]
                        j += 1
                i += 1
            Arbre_Binaire_Complet(self, liste2)
            pass

        elif methode == "ANC":  # Arbre n-aire 'Complet'
            if ta:
                Arbre.typeArbre = "Arbre n-aire Complet"
            Arbre_n_aire(self, liste, i)
            pass

        if self.sous_arbre:
            self.chaine += '['
            for elt in self.sous_arbre:
                self.poids += elt.poids
                self.chaine += elt.chaine+','
            self.chaine += ']'
        else:
            self.chaine = str(self.poids)
        self.chaine = self.chaine.replace(',]', ']')

    def __repr__(self):

        if self.sous_arbre:
            return "{0}]\t\t\t\tl: {1}  pos: {2}  b: {3}".format(self.poids, self.longueur_Tige_Total,
                                                                 self.ecarts_Tiges, self.barycentre)
        else:
            return "{0}".format(self.poids)

    def calcul_barycentre(self):
        if not self.sous_arbre:
            return
        if len(self.sous_arbre) == 2:
            self.barycentre = round((self.longueur_Tige_Total * self.sous_arbre[1].poids) /
                                    (self.sous_arbre[0].poids + self.sous_arbre[1].poids), 3)
        else:
            num = 0
            den = 0
            for i, elt in enumerate(self.sous_arbre):
                num += self.ecarts_Tiges[i] * elt.poids
                den += elt.poids

            self.barycentre = round(num/den, 3)
            for elt in self.sous_arbre:é a a
                elt.calcul_barycentre()

    def getMinX(self):
        if self.sous_arbre:
            return self.barycentre + self.sous_arbre[0].getMinX()
        else:
            return self.pprop//2

    def getMaxX(self):
        if self.sous_arbre:
            return (self.longueur_Tige_Total-self.barycentre) + self.sous_arbre[-1].getMaxX()
        else:
            return self.pprop // 2

    def MAJ(self):

        '''
        Met a jour les longueurs des tiges
        et re-calcul le barycentre des arbres
        '''
        self.pprop = pow(self.poids, 1 / 3) * 15
        if self.sous_arbre:
            n = []
            self.ecarts_Tiges = [0]
            for elt in self.sous_arbre:
                elt.MAJ()

            n += [self.sous_arbre[0].getMaxX() + 5]
            for elt in self.sous_arbre[1: -1]:
                m = sum(n) + elt.getMinX()
                self.ecarts_Tiges += [m]
                if elt.sous_arbre:
                    n += [elt.getMinX() + elt.getMaxX() + 5]
                else:
                    n += [elt.pprop + 5]
            n += [self.sous_arbre[-1].getMinX()]
            if len(self.sous_arbre) == 2:
                self.longueur_Tige_Total = self.sous_arbre[0].getMaxX() + 10 + self.sous_arbre[-1].getMinX()
                self.ecarts_Tiges += [self.longueur_Tige_Total]
                self.calcul_barycentre()

            else:
                self.ecarts_Tiges += [sum(n)]
                self.longueur_Tige_Total = self.ecarts_Tiges[-1]
                self.calcul_barycentre()

    def st(self):
        '''
        revoi la liste de tout les poids de l'arbre
        '''
        if self.sous_arbre:
            a = []
            for elt in self.sous_arbre:
                a.extend(elt.st())
            return a
        else:
            return [self.poids]

    def suppr(self, id):
        '''
            supprime un sous-arbre d'un arbre donné
           '''
        if self.ID != id and not self.sous_arbre:
            return False

        for elt in self.sous_arbre[::]:
            if elt.ID == int(id):
                self.sous_arbre.remove(elt)
                self.maj2()
                return

        for elt in self.sous_arbre:
            elt.suppr(id)

    def add(self, id,poid, pos):


        if self.ID == int(id):
            if not self.sous_arbre:
                self.sous_arbre = []
                self.sous_arbre += [Arbre("A", self.poids)]

            self.sous_arbre = self.sous_arbre[:pos] + [Arbre("A", poid)] + self.sous_arbre[pos:]
            return

        if self.sous_arbre:
            for elt in self.sous_arbre:
                elt.add(id, poid, pos)

    def lensa(self, id):
        '''
         retourne le nombre de sous-arbre d'un arbre donné
        '''
        a = 1
        if self.ID == int(id):
            if self.sous_arbre:
                a = len(self.sous_arbre)

        if self.sous_arbre:
            for elt in self.sous_arbre:
                a = max(elt.lensa(id), a)

        return a


    def isPoids(self, id):
        a = False
        if self.ID == int(id):
            return self.sous_arbre == None

        if self.sous_arbre:
            for elt in self.sous_arbre:
                a =elt.isPoids(id) or a

        return a

    def changepoids(self, id, poids):

        if self.ID == int(id):
            self.poids = poids
            return

        if self.sous_arbre:
            for elt in self.sous_arbre:
                elt.changepoids(id, poids)

    def maj2(self):
        '''
        Si un arbre ne contient qu'un seul sous arbre
        cette fonction remonte le sous-arbre d'un niveau
        '''
        if self.sous_arbre:
            if len(self.sous_arbre) == 1:
                self.poids = self.sous_arbre[0].poids
                self.pprop = self.sous_arbre[0].pprop
                self.sous_arbre = self.sous_arbre[0].sous_arbre
