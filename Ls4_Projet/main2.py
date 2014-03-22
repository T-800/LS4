#! /usr/bin/env python3

import math

class Arbre(object):

    profondeur_max = 0

    def __init__(self, methode, liste, i=0):
        '''
            Comme on ne peut pas definir plusieur contructeur pour notre Objet(!= java)
            et on a besoin de deux façon de contruir le module soit le fichier arbre soi le fichier liste poids
            J'ai mis le contructeur q'on a écrit dans la fonction "contruct_Arbre"
            car sinon ce contructeur serai beaucoup trop long
        '''
        self.poids = 0 # son poid si c'est une feuille ou le poids total si c'est un sous-arbre
        self.sous_arbre  = None # plus facile pour identifier les feuilles (ajout d'un test if dans les fonctions)
        self.ecarts_Tiges  = None # pas besoin de cette variable si c'est une feuille
        self.longueur_Tige_Total=0 # Celle la non plus

        if methode == "A":
            #appel pour la contruction a partir d'un fichier arbre
            self.constuct_Arbre(liste)

        elif methode == "ABC": # Arbre Binaire Complet
            self.Arbre_Binaire_Complet(liste)

        elif methode == "AA": # Arbre Alterné
            self.construct_Alt_Arbre(liste, i)

        elif methode == "NP": # Nombres Premiers
            self.Arbre_Nombre_Premier(liste)

        elif methode == "PI": # Paire/Impaire
            self.Arbre_Nombres_Pairs(liste)

        elif methode == "EQ": # sag ~~ sad
            print("EQ")
            pass

        elif methode == "ANR": # Arbre n-aire Random
            print("ANR")
            pass

        elif methode == "ANC": # Arbre n-aire 'Complet'
            print("ANC")
            pass


        if self.sous_arbre:
            for elt in self.sous_arbre:
                self.poids += elt.poids

        Arbre.profondeur_max = max(Arbre.profondeur_max,self.profondeur())

    def __repr__(self):

        if self.sous_arbre:
            return "Noeud: {0}    \tPoids: {1} \tLongueur l: {2}".format(self.sous_arbre != None,self.poids, self.longueur_Tige_Total)
        else:
            return "Noeud: {0} \tPoids: {1}".format(self.sous_arbre != None,self.poids)



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
                self.sous_arbre += [Arbre("A", elt)]


    def Arbre_Binaire_Complet(self, liste):
        '''
            Construction de l'arbre a partir d'une liste de poids
            si nb == -1 le nombre de fils f sera choisie aléatoirement pour chaque étages (soit [1:n], ou [1:n/k])
                la liste est diviser en f sous-liste
                cette fonction est appeler recursivement sur les f sous- liste
            sinon
                la liste est diviser en nb sous- liste
                cette foction est appeler recursivement sur les nb sous liste
        '''
        if len(liste) >= 2:
            liste1 = liste[:len(liste)//2]
            liste2 = liste[len(liste)//2:]
            if not self.sous_arbre:
                self.sous_arbre = []
            self.sous_arbre += [Arbre("ABC", liste1)]
            self.sous_arbre += [Arbre("ABC", liste2)]
        else:
            self.poids = liste[0]

    def construct_Random_Arbre(self):
        pass

    def Arbre_Nombre_Premier(self, liste):

        #
        prime = []
        nprime = []

        for elt in liste:
            if est_Premier(elt):
                prime += [elt]
            else:
                nprime += [elt]
        # Ajouter les tests si une des liste est vide
        if not self.sous_arbre:
            self.sous_arbre = []
        self.sous_arbre += [Arbre("ABC", prime)]
        self.sous_arbre += [Arbre("ABC", nprime)]


    def Arbre_Nombres_Pairs(self, liste):

        pair = []
        npair = []

        for elt in liste:
            if elt % 2 == 0:
                pair += [elt]
            else:
                npair += [elt]
        # Ajouter les tests si une des liste est vide
        if not self.sous_arbre:
            self.sous_arbre = []
        self.sous_arbre += [Arbre("ABC", pair)]
        self.sous_arbre += [Arbre("ABC", npair)]

    def construct_Alt_Arbre(self, liste=-75, i=1):
        if i == 0:
            if type(liste) == int:
                self.poids = liste
            elif len(liste) == 1:
                self.poids = liste[0]
            else:
                if not self.sous_arbre:
                    self.sous_arbre = []
                self.sous_arbre += [Arbre("AA", liste[0], 1)]
                self.sous_arbre += [Arbre("AA", liste[1:], 1)]

        else:
            if type(liste) == int:
                self.poids = liste
            elif len(liste) == 1:
                self.poids = liste[0]
            else:
                if not self.sous_arbre:
                    self.sous_arbre = []
                self.sous_arbre += [Arbre("AA", liste[1:], 0)]
                self.sous_arbre += [Arbre("AA", liste[0], 0)]

    def calcule_ecarts_tiges(self):
        '''
            Les distance entre les Tiges doit être fixé pour pouvoir calculer le barycentre :
                Soit on les fixe toutes donc nb_Tige//longeur total
                Soit on les choisi aléatoirement en fonction de la longueur total
        '''

        pass



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
        if not self.sous_arbre:
            return
        self.longueur_Tige_Total = (Arbre.profondeur_max * (self.profondeur()))
        for elt in self.sous_arbre:
                elt.calcul_longueur()


    def afficheArbre(self,tab='|'):
        '''
            Affiche l'arbre recursivement
        '''
        print(tab+str(self))
        if not self.sous_arbre:
            return
        for elt in self.sous_arbre:
                elt.afficheArbre(tab+'--')

    def Aff(self):
        print("Arbre:")
        self.aff_Noeud(0)


    def aff_Noeud(self, noeud_courrant):
        if self:
            if self.sous_arbre:
                self.sous_arbre[1].aff_Noeud(noeud_courrant + 1)
            for i in range(noeud_courrant):
                print("    ", end='')
            if not self.sous_arbre:
                print(self.poids)
            else:
                print(str(self.poids)+"]\t\t\t\t\t\t longueur l:"+str(self.longueur_Tige_Total))

            if self.sous_arbre:
                self.sous_arbre[0].aff_Noeud(noeud_courrant + 1)


def est_Premier(nombre):
    if nombre == 1:
        return False
    k=2
    r=math.sqrt(nombre)
    while k<=r:

        if nombre % k == 0:
            return False
        k+=1
    return True


if __name__ == '__main__':

    fic2 = open("fic2")
    liste1 = fic2.readlines()
    liste1 = [int(i) for i in liste1]
    liste1.sort()
    print(liste1)
    #liste1 = eval(liste1)
    a = Arbre(liste=liste1,nb_arrete=2)
    a.calcul_longueur()
    a.afficheArbre()
    print("profondeur "+str(a.profondeur()))
    print("profondeur_max "+str(a.profondeur_max))





    fic1 = open("fic")
    liste1 = fic1.readline()
    liste1 = eval(liste1)
    a = Arbre(liste1)
    a.calcul_longueur()
    a.afficheArbre()
    print("profondeur "+str(a.profondeur()))
    print("profondeur_max "+str(a.profondeur_max))

