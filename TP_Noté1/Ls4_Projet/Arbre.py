#! /usr/bin/env python3

import math


class Arbre(object):

    profondeur_max = 0
    typeArbre = ""

    def __init__(self, methode, liste, i=0, ta=True):
        self.poids = 0  # son poid si c'est une feuille ou le poids total si c'est un sous-arbre
        self.pprop = 0
        self.sous_arbre = None  # plus facile pour identifier les feuilles (ajout d'un test if dans les fonctions)
        self.ecarts_Tiges = None  # pas besoin de cette variable si c'est une feuille
        self.longueur_Tige_Total = 100  # Celle la non plus
        self.barycentre = 0
        self.chaine = ""

        if methode == "A":
            if ta: Arbre.typeArbre = "Fichier Arbre"
            self.constuct_Arbre(liste)

        elif methode == "ABC":  # Arbre Binaire Complet
            if ta :Arbre.typeArbre = "Arbre binaire Complet"
            self.Arbre_Binaire_Complet(liste)

        elif methode == "AA":  # Arbre Alterné
            if ta:Arbre.typeArbre = "Arbre Alterné"
            self.construct_Alt_Arbre(liste, i)

        elif methode == "NP":  # Nombres Premiers
            if ta:Arbre.typeArbre = "Nombres premiers"
            self.Arbre_Nombre_Premier(liste)

        elif methode == "PI":  # Paire/Impaire
            if ta:Arbre.typeArbre = "Nombres paire/Impaire"
            self.Arbre_Nombres_Pairs(liste)

        elif methode == "EQ":  # sag ~~ sad
            if ta:Arbre.typeArbre = "Arbre Equilibré"
            print("EQ")
            pass

        elif methode == "ANR":  # Arbre n-aire Random
            if ta:Arbre.typeArbre = "Arbre n-aire Complet"
            print("ANR")
            pass

        elif methode == "ANC":  # Arbre n-aire 'Complet'
            if ta:Arbre.typeArbre = "Arbre n-aire Random"
            print("ANC")
            pass

        if self.sous_arbre:
            self.chaine+='['
            for elt in self.sous_arbre:
                self.poids += elt.poids
                self.chaine += elt.chaine+','
            self.chaine += ']'
        else:
            self.chaine = str(self.poids)
        self.chaine = self.chaine.replace(',]',']')

        Arbre.profondeur_max = max(Arbre.profondeur_max,self.profondeur())


    def __repr__(self):

        if self.sous_arbre:
            return "{0}]\t\t\t\tl: {1}  pos: {2}  b: {3}".format(self.poids, self.longueur_Tige_Total,self.ecarts_Tiges,self.barycentre)
        else:
            return "{0}".format(self.poids)


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
            self.sous_arbre += [Arbre("ABC", liste1, ta=False)]
            self.sous_arbre += [Arbre("ABC", liste2, ta=False)]
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
        if prime == [] or nprime == []:
            self.Arbre_Binaire_Complet(liste)
            Arbre.typeArbre = "Arbre binaire Complet"
        else:
            self.sous_arbre += [Arbre("ABC", prime, ta=False)]
            self.sous_arbre += [Arbre("ABC", nprime, ta=False)]


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
        if pair == [] or npair == []:
            self.Arbre_Binaire_Complet(liste)
            Arbre.typeArbre = "Arbre binaire Complet"
        else:
            self.sous_arbre += [Arbre("ABC", pair, ta=False)]
            self.sous_arbre += [Arbre("ABC", npair, ta=False)]


    def construct_Alt_Arbre(self, liste, i=1):
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


    def profondeur(self):
        '''
            Calcul la profondeur de l'arbre courant
        '''
        if not self.sous_arbre:
            return 0
        else :
            l = [ elt.profondeur() for elt in self.sous_arbre]
            return 1+ max(l)


    """def calcul_longueur(self):
        '''
            Calcul la Longueur Total de la tige
        '''
        if not self.sous_arbre:
            return
        self.longueur_Tige_Total = (Arbre.profondeur_max * (self.profondeur()))*50
        for elt in self.sous_arbre:
                elt.calcul_longueur()
"""

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
                print(self)
            else:
                print(self)

            if self.sous_arbre:
                self.sous_arbre[0].aff_Noeud(noeud_courrant + 1)


    def calcul_Pos_SA(self):
        if self.sous_arbre:
            self.ecarts_Tiges = [i*(self.longueur_Tige_Total/(len(self.sous_arbre)-1)) for i in range(len(self.sous_arbre))]
            for elt in self.sous_arbre:
                elt.calcul_Pos_SA()


    def calcul_barycentre(self):
        if not self.sous_arbre:
            return
        if len(self.sous_arbre) == 2:
            self.barycentre = round((self.longueur_Tige_Total*self.sous_arbre[1].poids)/(self.sous_arbre[0].poids+self.sous_arbre[1].poids), 3)
        else:
            num = 0
            den = 0
            for i,elt in enumerate(self.sous_arbre):
                num += self.ecarts_Tiges[i]*elt.poids
                den += elt.poids

            self.barycentre = round(num/den, 3)
        for elt in self.sous_arbre:
            elt.calcul_barycentre()


    def saveArbre(self,nomFichier):
        f = open(nomFichier,'w')
        f.write(self.chaine)
        f.close()

    def getMinX(self):
        if self.sous_arbre:
            return self.barycentre + self.sous_arbre[0].getMinX()
        else: return self.pprop//2

    def getMaxX(self):
        if self.sous_arbre:
            return self.longueur_Tige_Total-self.barycentre + self.sous_arbre[-1].getMaxX()
        else:
            return self.pprop//2
    def MAJ(self):
        self.pprop = pow(self.poids,1/2)*15
        if self.sous_arbre:
            n = 0

            for elt in self.sous_arbre:
                elt.MAJ()

            for elt in self.sous_arbre[1:-1]:
                n += 5 + elt.getMinX() + elt.getMaxX() + 5

            print("n:"+str(n))
            n += self.sous_arbre[0].getMaxX() + 10 + self.sous_arbre[-1].getMinX()
            self.longueur_Tige_Total = n
            self.calcul_Pos_SA()
            self.calcul_barycentre()
            print(self)
            print("m"+str(n))
            return n
            '''
            if len(self.sous_arbre) == 2:
                l = sum(tmp)
                print("MAX : {0}".format(self.getMaxX()))
                print("Min : {0}".format(self.getMinX()))
                m = self.sous_arbre[0].getMaxX() + 10 + self.sous_arbre[-1].getMinX()
                self.longueur_Tige_Total = m
                self.calcul_barycentre()

                return m
            else:
                print("batard")
                l = (tmp[-1])*(len(tmp))
                self.longueur_Tige_Total = l +(10)*(len(tmp)-1)
                return l + (10)*(len(tmp)-1)
            '''
        else:
            return self.pprop//2

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

    #Arbre Binaire
    f = open("fic2")
    liste1 = f.readlines()
    liste1 = [int(i) for i in liste1]
    print(liste1)
    a = Arbre("ABC", liste1, 0)
    #a.calcul_longueur()
    a.calcul_Pos_SA()
    a.calcul_barycentre()
    a.Aff()
    a.saveArbre('test')

    '''

    #Arbre n-AIRE
    f = open("fic")
    liste1 = f.readline()
    liste1 = eval(liste1)
    a = Arbre("A", liste1, 0)
    a.calcul_longueur()
    a.calcul_Pos_SA()
    a.calcul_barycentre()
    a.afficheArbre()



    print("profondeur " + str(a.profondeur()))
    print("profondeur_max " + str(a.profondeur_max))

    '''