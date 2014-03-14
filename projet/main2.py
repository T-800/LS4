#! /usr/bin/env python3


class Arbre(object):

    profondeur_max = 0

    def __init__(self, arbre=None, liste=None, nb_Noeud=None):

        self.poids = 0
        self.sous_arbre  = None
        self.ecarts_Tiges  = None
        self.longueur_Tige_Total=0

        if arbre:
            self.constuct_Arbre(arbre)
        else:
            pass

    def __repr__(self):
        if self.sous_arbre == []:
            return ("Noeud: {0}, \tPoids: {1}, \t Profondeur Max {2}, ".format(self.sous_arbre != [],self.poids, self.profondeur_max))
        else:
            return ("Noeud: {0}, \tPoids: {1}, \t Profondeur Max {2},\tLongueur l: {3}, ".format(self.sous_arbre != [],self.poids, self.profondeur_max, self.longueur_Tige_Total))


    def constuct_Arbre(self,arbre):
        '''
            Construction de l'arbre a partir d'une liste d'arbre
        '''
        if type(arbre) == int:
            self.poids = arbre
        else :
            if not self.sous_arbre:
                self.sous_arbre = []
            for elt in arbre:
                self.sous_arbre += [Arbre(arbre=elt)]


            for elt in self.sous_arbre:
                self.poids += elt.poids

            Arbre.profondeur_max = max(Arbre.profondeur_max,self.profondeur())
            #print("\nINIT")
            #print(self)
            #print("---------\n")


    def constuct_Liste(self,liste, nb=-1):
        '''
            Construction de l'arbre a partir d'une liste de poids
        '''
        if type(arbre) == int:
            self.poids = arbre
        else :
            if not self.sous_arbre:
                self.sous_arbre = []
            for elt in arbre:
                self.sous_arbre += [Arbre(arbre=elt)]


            for elt in self.sous_arbre:
                self.poids += elt.poids

            Arbre.profondeur_max = max(Arbre.profondeur_max,self.profondeur())
            #print("\nINIT")
            #print(self)
            #print("---------\n")





    def profondeur(self):
        '''
            Calcul la profondeur de l'arbre courant
        '''
        if not self.sous_arbre:
            return 0
        else :
            l = [ elt.profondeur() for elt in self.sous_arbre]
            return 1+ max(l)

    def calcul_longueur(self):
        '''
            Calcul la Longueur Total de la tige
        '''
        self.longueur_Tige_Total = (Arbre.profondeur_max * (self.profondeur()))
        if not self.sous_arbre:
            return
        for elt in self.sous_arbre:
                elt.calcul_longueur()


    def afficheArbre(self):
        '''
            Affiche l'arbre recursivement
        '''
        print(self)
        if not self.sous_arbre:
            return
        for elt in self.sous_arbre:
                elt.afficheArbre()




fic = open("fic")

liste1 = fic.readline()
liste1 = eval(liste1)

a = Arbre(liste1)
a.calcul_longueur()
a.afficheArbre()
print("profondeur "+str(a.profondeur()))
print("profondeur_max "+str(a.profondeur_max))
