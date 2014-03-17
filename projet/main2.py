#! /usr/bin/env python3


class Arbre(object):

    profondeur_max = 0

    def __init__(self, arbre=None, liste=None, nb_Noeud=-1):
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

        if arbre:
            #appel pour la contruction a partir d'un fichier arbre
            self.constuct_Arbre(arbre)

        elif liste:
            #appel pour la contruction a partir d'un fichier de poids
            #self.constuct_Liste(liste,nb_Noeud)
            pass
        else:
            # autre contructeur OU ERREUR
            pass

    def __repr__(self):

        if self.sous_arbre:
            return ("Noeud: {0}    \tPoids: {1} \tLongueur l: {2}".format(self.sous_arbre != None,self.poids, self.longueur_Tige_Total))
        else:
            return ("Noeud: {0} \tPoids: {1}".format(self.sous_arbre != None,self.poids))



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
            si nb == -1 le nombre de fils f sera choisie aléatoirement pour chaque étages (soit [1:n], ou [1:n/k])
                la liste est diviser en f sous-liste
                cette fonction est appeler recursivement sur les f sous- liste
            sinon
                la liste est diviser en nb sous- liste
                cette foction est appeler recursivement sur les nb sous liste
        '''
        pass


    def calcule_ecarts_tiges():
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




fic = open("fic")

liste1 = fic.readline()
liste1 = eval(liste1)

a = Arbre(liste1)
a.calcul_longueur()
a.afficheArbre()
print("profondeur "+str(a.profondeur()))
print("profondeur_max "+str(a.profondeur_max))
